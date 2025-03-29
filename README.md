# Solana Bots

**Status:** Ongoing Research & Active Deployment  
**Note:** Key algorithmic components remain private to protect proprietary live trading strategies.

---

## Project Overview

This repository contains the implementation of two core systems designed to facilitate alpha signal detection and notification in low-cap tokens on the Solana blockchain:

1. **Data Collection Bot** — Gathers real-time token and liquidity data for targeted assets.
2. **Signal Notification Bot** — Delivers automated alerts to Discord based on private signal logic.

Together, these systems underpin an academic research initiative aimed at understanding microstructural patterns in decentralised financial markets.

> **Disclaimer:** Parts of this codebase, including signal filtering and prediction logic, remain private to preserve the uniqueness and performance of live-deployed strategies.

---

## System Deployment and Validation

Although development is ongoing, both bots have been actively deployed in a real-world setting. Their use has:

- Informed live token discovery and trade decisions
- Produced a growing repository of recorded trade history and strategy outcomes
- Enabled traceable signal-to-trade relationships for academic and analytical evaluation

Performance documentation and anonymised trade logs are available upon request for professional or academic review.

---

## Architecture Overview

### 1. `collector_bot/`
- Connects to public Solana APIs (e.g., Birdeye, Jupiter, Solscan)
- Collects time-stamped token metadata and transaction metrics
- Stores data for modelling and longitudinal signal validation

### 2. `alert_bot/`
- Monitors high-priority token activity
- Sends alerts to a secured Discord channel via Webhooks
- Modular rule design for adaptation to different triggers or strategies

> *Note: Signal scoring and model outputs are processed through private modules and not part of this repository.*

---

## Research Context

This bot suite forms the basis for MSc-level dissertation research at the University of Exeter (2025). The research investigates:

- The predictive structure of new-launch and early-stage tokens
- Statistical and machine learning approaches to token performance modelling (e.g., Random Forest, XGBoost)
- Parameter estimation and volatility analysis in decentralised token ecosystems

The project aims to contribute to academic understanding of emerging DeFi markets, with an emphasis on the dynamics of underexplored high-risk tokens.

- **Python** is used for real-time engineering and model building.
- **R** is used for exploratory statistics and hypothesis testing.

All findings will be reproducibly documented and developed under academic ethics and open research principles.

---

## Ethics and Code Access

To maintain responsible disclosure:
- Signal logic and trading heuristics are not publicly accessible
- Core structural files, pipelines, and documentation are available
- Research data will be anonymised and curated for future publication

This repository is intended for transparency, modular demonstration, and peer engagement — not trading signal dissemination.

---

## Contact and Collaboration

For collaboration, research discussion, or performance insights:

- **Email:** james066lewis@gmail.com  
- **GitHub:** [@KetchupJL](https://github.com/KetchupJL)

Documentation of live trade activity and model validation can be made available for professional review on request.

