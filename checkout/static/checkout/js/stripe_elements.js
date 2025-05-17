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

// Only initialize Stripe when card payment is selected
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
        $('#submit-button').attr('disabled', true);
        
        $('#loading-overlay').show();

        const saveInfo = Boolean($('#id-save-info').prop('checked'));
        const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        const postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        const url = '/checkout/cache_checkout_data/';

        

        $.post(url, postData).done(function () {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.full_name.value),
                        phone: $.trim(form.phone_number.value),
                        email: $.trim(form.email.value),
                        address: {
                            line1: $.trim(form.street_address1.value),
                            line2: $.trim(form.street_address2.value),
                            city: $.trim(form.town_or_city.value),
                            country: $.trim(form.country.value),
                            state: $.trim(form.county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                        state: $.trim(form.county.value),
                    }
                },
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
                $(errorDiv).html(html); 
                
        
                $('#loading-overlay').hide();
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                // Submit the form if payment is successful
                if (result.paymentIntent.status === 'succeeded') {
                    form.dispatchEvent(new Event('submit'));
                }
            }
        });
        }).fail(function () {
            location.reload(); // Reload if caching checkout data fails
        });
    });
});
