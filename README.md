📊 Market Regime Analysis using Unsupervised Learning

This project identifies and analyzes market regimes in the Indian stock market (NIFTY 50 index) using unsupervised machine learning techniques.
The goal is to understand different market conditions such as high volatility bull phases and low volatility sideways phases using historical price and volume data.

🚀 Project Overview

Financial markets behave differently under varying volatility and trend conditions.
Instead of manually defining these regimes, this project uses KMeans clustering to automatically discover hidden market states based on quantitative features.

Key outcomes:

Identified distinct market regimes

Labeled regimes based on statistical characteristics

Visualized regimes directly on price charts

Built a reproducible, end-to-end data analysis pipeline

📂 Project Structure
market_regime_analysis/
│
├── data/
│   ├── clean/                 # Cleaned raw market data
│   ├── features/              # Engineered features
│   └── processed/             # Final dataset with regime labels
│
├── notebook/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_returns_and_volatility.ipynb
│   ├── 03_market_regimes.ipynb
│   └── 04_dashboard.ipynb
│
├── report/
│   └── market_regime_analysis_report.md
│
├── download_data.py            # Data download script
├── README.md
└── .gitignore

🧠 Methodology
1️⃣ Data Collection

Historical NIFTY 50 data downloaded from Yahoo Finance

Daily OHLCV data used for analysis

2️⃣ Feature Engineering

The following features were created:

Log Returns – captures price movement

Rolling Volatility (30-day) – measures market risk

Trend Strength (20 vs 50 SMA) – detects momentum

Volume Ratio – identifies abnormal trading activity

3️⃣ Clustering (Unsupervised Learning)

Applied KMeans clustering

Optimal number of clusters selected empirically

Each cluster represents a distinct market regime

4️⃣ Regime Interpretation

Clusters were interpreted using:

Average returns

Volatility

Trading volume

Example regimes:

High-Volatility Bull Market

Low-Volatility Sideways Market

📈 Market Regime Summary
Regime	Avg Return	Volatility	Avg Volume	Observations
High-Vol Bull	Higher	High	High	Strong upward moves with risk
Low-Vol Sideways	Low	Low	Moderate	Range-bound consolidation
📊 Visualization

Market regimes are overlaid directly on the NIFTY 50 price chart, making regime transitions visually intuitive.

📌 (Charts will be added below in the next step)

🛠️ Tools & Technologies

Python

Pandas, NumPy

Scikit-Learn

Matplotlib

Jupyter Notebook

Git & GitHub

🎯 Key Learnings

Applied unsupervised learning to real financial data

Designed a feature-driven clustering approach

Interpreted ML output in a business/market context

Built an end-to-end reproducible data analysis project

📌 Future Improvements

Add more regimes (bear / crash phases)

Use HMM or Gaussian Mixture Models

Backtest regime-based trading strategies

Deploy interactive dashboard (Streamlit)

👤 Author

Arif Sheikh
Aspiring Data Analyst | Python | SQL | Machine Learning
