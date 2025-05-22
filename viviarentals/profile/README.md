# VIVIA CONNECT

> Residential Property Management & Rental Syndication Platform
> Powered by Stripe Connect, integrated with Zillow, Zumper, and more.

![License](https://img.shields.io/github/license/viviarentals/viviarentals-com)
![Node.js](https://img.shields.io/badge/node.js-20.x-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 🏠 Overview

**VIVIA CONNECT** is a modern property management platform enabling landlords and property managers to:

* Manage rentals and lease terms
* Collect rent and deposits via Stripe
* Syndicate listings to major rental platforms like **Zillow**, **Realtor.com**, and **Facebook Marketplace**
* Handle applications through **Zumper** and communicate with renters in real time

---

## 🔌 Integrations

| Service                  | Purpose                                 |
| ------------------------ | --------------------------------------- |
| **Stripe Connect**       | Payments, billing, and payouts          |
| **Zillow API**           | Rental listing syndication              |
| **Facebook Marketplace** | Lead generation and visibility          |
| **Zumper**               | Rental applications and screening       |
| **Algolia Crawler**      | Search indexing and dynamic content     |
| **Cloudflare**           | DNS, TLS, Zero Trust network protection |
| **Google Cloud**         | Storage for lease PDFs and documents    |

---

## 🛠️ Tech Stack

* **Frontend**: Tailwind CSS, React *(optional)*
* **Backend**: Node.js, Express, MongoDB
* **Infra**: Docker, GitHub Actions, Cloudflare
* **Search**: Algolia Crawler
* **Payments**: Stripe API, Stripe Connect

---

## 🚀 Getting Started

### Prerequisites

* Node.js v20+
* MongoDB
* Stripe account (with Connect enabled)
* `.env` file configured

### Installation

```bash
git clone https://github.com/viviarentals/viviarentals-com.git
cd viviarentals-com
npm install
npm run dev
```

Create a `.env` file:

```
STRIPE_SECRET_KEY=sk_test_...
MONGO_URI=mongodb://localhost:27017/vivia
ALGOLIA_API_KEY=...
CLOUDINARY_URL=...
```

---

## 📱 Webhooks

Be sure to set up the following webhook routes for integrations:

| Partner              | Route                            |
| -------------------- | -------------------------------- |
| Zillow               | `/callback/zillow`               |
| Facebook Marketplace | `/callback/facebook_marketplace` |
| Realtor.com          | `/callback/realtor`              |

---

## 📁 Project Structure

```
routes/
  syndicationCallback.js
controllers/
  stripeController.js
models/
  Lease.js
utils/
  generatePDF.js
.env
```

---

## 📄 License

[MIT License](LICENSE)

---

## 🙌 Contributing

Contributions, bug reports, and feature requests are welcome. Please open issues or pull requests via GitHub.

---

## 🌐 Links

* 🔗 [VIVIA Website](https://viviarentals.com)
* 🛆 [NPM Package Registry](https://npm.pkg.github.com/viviarentals)
* 📘 [Docs](https://docs.viviarentals.com)
