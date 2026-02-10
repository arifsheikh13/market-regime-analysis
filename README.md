# 📊 Market Regime Analysis — NIFTY 50

## 🔍 Objective
Identify and analyze distinct market regimes in the NIFTY 50 index using statistical features and unsupervised learning, and evaluate their persistence and risk characteristics.

## 🧠 Methodology
- Daily returns and log returns
- Rolling volatility estimation
- Rule-based regime classification
- K-Means clustering for latent regime detection
- Regime persistence & transition analysis
- Regime-wise drawdown comparison

## 📈 Key Findings
- Two statistically distinct and persistent market regimes were identified.
- High-volatility regimes exhibit significantly deeper drawdowns (~29%) compared to low-volatility regimes (~19%).
- Regime transitions show temporal persistence, indicating non-random structure in market behavior.

## ⚠️ Limitations
- Analysis is index-specific (NIFTY 50).
- K-Means assumes convex clusters.
- Transaction costs not considered.

## 🚀 Future Work
- Hidden Markov Models (HMM)
- Regime-aware portfolio strategies
- Macro variable integration (VIX, rates)

## 🛠 Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn