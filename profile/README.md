# 🏠 viviarentals

Modern property management infrastructure with listing syndication, automated billing, and secure Stripe-powered payments. Built for landlords, renters, and devs alike.

---

## 🚀 What is VIVIA?

**viviarentals** is a developer-first rental platform that:

* Syncs listings to Zillow, Facebook Marketplace, Flexmls, and Redfin
* Handles rent payments, deposits, and invoicing via Stripe Connect
* Supports OAuth, webhooks, SAML, and XML feed integrations
* Offers a renter UX optimized for speed, mobile, and accessibility

---

## 💠 Tech Stack

* **Frontend**: React + Tailwind CSS
* **Backend**: Node.js + Express
* **Database**: MongoDB + Stripe
* **Infra**: Netlify, Cloudflare, GitHub Actions

---

## 🔌 Key Integrations

| Service        | Purpose                        |
| -------------- | ------------------------------ |
| Stripe         | Rent, deposits, invoicing      |
| Flexmls        | MLS listing sync               |
| Zumper         | Tenant applications            |
| Zillow API     | Listing syndication            |
| Netlify        | Hosting & serverless functions |
| GitHub Actions | CI/CD, security workflows      |

---

## 📦 Installation

```bash
git clone https://github.com/viviarentals/viviarentals-com.git
cd viviarentals-com
npm install
npm run dev
```

Set up your `.env` file:

```env
STRIPE_SECRET_KEY=sk_test_...
MONGO_URI=mongodb://localhost:27017/vivia
API_BASE_URL=https://api.viviarentals.com
```

---

## 🦪 Running Tests

```bash
npm run test
```

---

## 📄 License

[MIT License](LICENSE)

---

## 📆 Releases

* 🔖 [v1.4.3](https://github.com/viviarentals/viviarentals-com/releases/tag/v1.4.3) – Security fix + crypto onramp integration
* 🥪 [v1.4.2](https://github.com/viviarentals/viviarentals-com/releases/tag/v1.4.2) – Renter app workflow + Stripe Connect setup

---

> Need help with deployment, API usage, or integration?
> Visit [viviarentals.com](https://viviarentals.com) or contact the team.
