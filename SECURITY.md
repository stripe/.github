# Security Policy

### Reporting a vulnerability

Please do not open GitHub issues or pull requests - this makes the problem immediately visible to everyone, including malicious actors.   

Security issues in this open-source project can be safely reported to Stripe's [Vulnerability Disclosure and Reward Program](https://stripe.com/docs/security/stripe#disclosure-and-reward-program).
Stripe's security team will triage your report and respond according to its impact on Stripe users and systems.
// POST to your backend API or serverless function
const session = await stripe.checkout.sessions.create({
  line_items: [{
    price_data: {
      currency: 'usd',
      unit_amount: 1499,
      product_data: {
        name: 'Music Streaming Coupon',
      },
    },
    quantity: 1,
    tax_behavior: 'exclusive',
    tax_code: 'txcd_10000000',
  }],
  shipping_options: [{
    shipping_rate_data: {
      display_name: 'Standard Shipping',
      fixed_amount: { amount: 20, currency: 'usd' },
      tax_behavior: 'exclusive',
      tax_code: 'txcd_92010001',
    },
  }],
  mode: 'payment',
  automatic_tax: { enabled: true },
  success_url: 'https://viviarentals-app.netlify.app/success',
  cancel_url: 'https://viviarentals-app.netlify.app/cancel',
});
