/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

document.addEventListener('DOMContentLoaded', function () {
    // Extract Stripe public key and client secret from the DOM
    const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
    const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1);

    // Initialize Stripe and Elements
    const stripe = Stripe(stripePublicKey);
    const elements = stripe.elements();

    // Define custom style for Stripe card input
    const style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    // Create a Card element with the defined style
    const card = elements.create('card', {style: style});
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        const errorDiv = document.getElementById('card-errors');
        if (event.error) {
            const html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            errorDiv.innerHTML = html;
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit
    const form = document.getElementById('payment-form');

    form.addEventListener('submit', function (ev) {
        ev.preventDefault();

        // Disable the card input and submit button
        card.update({ 'disabled': true });
        document.getElementById('submit-button').disabled = true;

        // Confirm the payment using the client secret
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card
            }
        }).then(function (result) {
            if (result.error) {
                // Show error message if payment fails
                const errorDiv = document.getElementById('card-errors');
                const html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
                errorDiv.innerHTML = html;

                // Enable the card input and submit button again
                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;
            } else {
                // Submit the form if payment is successful
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });
});
