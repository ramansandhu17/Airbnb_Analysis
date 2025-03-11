# Airbnb_Analysis
**Airbnb Analysis for Property Manager**

## Project Overview
NRS Property Management Service manages multiple short-term rental (STR) properties but lacks **data-driven insights** into **booking trends, pricing strategies, and guest behavior**. This project analyzes Airbnb data to **optimize revenue, improve occupancy rates, and enhance guest experience**.

## Problem Statement
The property manager faces challenges in **maximizing revenue and improving occupancy rates** due to a lack of structured insights. Current pricing and guest engagement strategies are **not optimized**, leading to missed revenue opportunities. This project **bridges that gap** by analyzing historical data and providing actionable insights.

## Objectives
- **Analyze** booking trends to identify peak and off-peak periods.
- **Evaluate** price variations and revenue across properties.
- **Predict** optimal pricing strategies using machine learning.
- **Perform sentiment analysis** to understand guest satisfaction.
- **Provide** actionable insights through interactive dashboards.

## Dataset
- **Airbnb Bookings (`airbnb_bookings.csv`)** – Booking data for multiple properties.
- **Guest Information (`guest_info.csv`)** – Details on guests, including phone numbers, locations, and joining years.
- **Properties (`properties.csv`)** – Property metadata (e.g., name, location).
- **Reviews (`reviews.csv`)** – Guest feedback with sentiment labels.

## Methodology
This project employs a range of **data science techniques**, including:
1. **Data Collection & Cleaning**
   - Handling missing data, correcting inconsistencies.
2. **Exploratory Data Analysis (EDA)**
   - Analyzing booking trends, pricing variations, and occupancy rates.
3. **Machine Learning Modeling**
   - **XGBoost, LightGBM** → Predicting **optimal nightly rates**.
   - **ARIMA, Prophet** → Forecasting **occupancy trends**.
   - **NLP (TextBlob, VADER)** → **Sentiment analysis on guest reviews**.
4. **Data Visualization & Insights**
   - **Power BI Dashboard** → Customer-facing property insights.
   - **Streamlit Application** → Internal tool for real-time analysis.

## Deliverables
- **Comprehensive Report** → Key findings & recommendations.
- **Sentiment Analysis** → Detects positive & negative guest reviews.
- **Power BI Dashboard** → Provides interactive customer insights.
- **Streamlit Web App** → Internal analytics for property managers.
- **Machine Learning Model** → Predicts **nightly pricing & occupancy rates**.

## Future Work
- **Customer segmentation analysis** → Grouping guests by preferences.
- **Dynamic pricing implementation** → AI-driven price optimization.
- **Expanding to other regions** → Applying insights to new markets.

---


