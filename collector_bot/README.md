# 📥 Solana Data Collector Bot

This module contains the data collection system used to monitor new low-cap tokens and on-chain events in real-time on the Solana blockchain. It forms the backend infrastructure for both signal development and research-based analysis.

---

## 🔧 Overview

The collector bot:

- Connects to public Solana APIs
- Scrapes token profiles and metadata
- Caches and filters relevant assets
- Logs data for further analysis and modelling

The bot is designed to operate continuously, providing timestamped historical data and enriched context for downstream signal evaluation or statistical modelling.

---

## 🔐 About This Version

> The file `collector_public.py` offers a **safe, simplified version** of the collection process. It demonstrates key structural features but **omits signal logic, proprietary filters, and database integrations**.

**Private components removed include:**
- Alpha signal filtering criteria
- Token scoring logic
- Live database schema and saving procedures
- Price tracking and ATH management functionality

These are withheld to protect the uniqueness and performance of live trading systems built on top of this data.

---

## 📄 Files

| File | Description |
|------|-------------|
| `collector_public.py` | Public-safe example bot script |
| `__init__.py` | Placeholder module initializer |

---

## 🧠 Research Context

This collector supports a research-led MSc dissertation project focused on token modelling and DeFi market dynamics, using both statistical methods and machine learning.

---

## 📬 Contact

For collaboration or discussion about this component:

- GitHub: [@KetchupJL](https://github.com/KetchupJL)
- Email: james066lewis@gmail.com
