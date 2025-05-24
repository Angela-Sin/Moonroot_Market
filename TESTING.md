---

<h1 align="center"><strong>MOONROOT MARKET</strong>

---



## [LIVE SITE](#)

## [GITHUB RESPOSITORY](https://github.com/Angela-Sin/Moonroot_Market)

## Table of Contents

* [Manual Testing](#manual-testing)
  * [User Stories Testing](#user-stories-testing)
* [Lighthouse Testing](#lighthouse-testing)
  * [Mobile Phone](#mobile-phone)
  * [Desctop](#desctop)
* [Code Validation](#code-validation)
  * [Html](#html)
  * [CSS](#css)
  * [Python](#python)
* [Browser Compatibility](#browser-compatibility)
* [Bug-Fix](#bug-fix)



# Manual Testing
## User stories testing


| **User Story** | **Testing Method** | **Expected Outcome** | **Result** |
|---------------|-------------------|---------------------|------------|


### Common Elements on All Pages



- ## Responsive Navigation for Smaller Devices


# Lighthouse 
## Mobile Phone


## Desktop


# Code validation
## [Html](https://validator.w3.org/)


## CSS
## [CSS-Valitador](#https://jigsaw.w3.org/css-validator/)

# Python
## [pep8ci](#https://pep8ci.herokuapp.com/)

# Browser Compability

The site was tested across multiple browsers for consistency and responsiveness:

| Browser           | Result  |
|------------------|--------|
| 🌍 **Google Chrome**   |   |
| 🦊 **Mozilla Firefox** |  |
| 🎭 **Microsoft Edge**  |   |
|🏴‍☠️ **Opera**            |   |



The site maintains a **consistent design** and remains **fully responsive** across different browsers.


# Bug-Fix

## ⚠️ 1-Security Notice

During the initial setup of this project, the secret key was unintentionally committed to version control. To resolve this:

- The original app was deleted.
- A new app was created with the secret key securely managed using environment variables.
- The `env.py` file is included in `.gitignore` to prevent future accidental commits.

**Important:**  
Always ensure that sensitive information like API keys, secret tokens, and credentials are stored in environment variables and never committed to the repository.

## 2-Stripe Integration Fix – jQuery and Webhook Issue

## 🧩 Problem Summary

While integrating Stripe payments, the following issues were encountered:

- Stripe elements would **not load in the browser**.
- The `$` symbol (jQuery) was **not recognized**.
- The **terminal output appeared normal**, but the browser didn’t reflect that.
- After setting up the **webhook**, the page would **freeze on order submission**:
  - No success or error messages.
  - No output in the terminal or browser console.

## 🛠️ Initial Workaround

Wrapping the code in a **loop** provided a temporary fix by making the page responsive initially.

## ✅ Final Solution

### 🔍 Root Cause

The issue was caused by the browser **not properly reading the jQuery script**, likely due to the `integrity` attribute.

### ❌ Original jQuery Script (Not Working)

```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js"
        integrity="sha384-JlY8zMqb6gci8CnmUHzbqUOdD3jZP2BfIWeUE5SrZT4TgZTrZnMzI+1SWSK+3z+s"
        crossorigin="anonymous"></script>
