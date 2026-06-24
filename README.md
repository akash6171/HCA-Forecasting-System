# Demand Forecasting & Inventory Intelligence System
## Overview

This project is an end-to-end Machine Learning-based Demand Forecasting and Inventory Intelligence System developed during my internship at HCA.

The system helps businesses analyze historical sales data, identify demand patterns, forecast future demand, and generate intelligent inventory restocking recommendations.

The project combines Data Analysis, Business Intelligence, Machine Learning, Forecasting, and Inventory Optimization into a single solution.

## Business Problem

Businesses often face challenges such as:

Stock shortages
Overstocking
Inventory mismanagement
Demand uncertainty
Revenue loss due to poor planning

This project addresses these challenges by forecasting future demand and recommending optimal restocking quantities based on inventory levels and forecasted demand.

## Objectives
Analyze historical sales and inventory data
Discover business insights using Exploratory Data Analysis (EDA)
Build machine learning forecasting models
Compare model performance
Predict future product demand
Generate inventory restocking recommendations
Support data-driven business decisions
Dataset Features

## The dataset contains information related to:

Store Information
Product Information
Product Categories
Regional Information
Pricing Data
Discount Information
Inventory Levels
Competitor Pricing
Promotion Details
Weather Conditions
Seasonality Factors
Epidemic Impact
Demand Data
Feature Engineering

Several new features were created from date-related information:

Month
Year
Quarter
Week Number
Day of Week
Weekend Indicator

Additional business features:

Revenue
Demand Trends
Inventory Metrics
Promotional Effects
Seasonal Effects
Exploratory Data Analysis (EDA)

## The project includes extensive EDA such as:

Data Quality Analysis
Missing Value Analysis
Duplicate Record Detection
Outlier Detection
Business Analysis
Revenue Analysis
Product Performance Analysis
Category Analysis
Regional Analysis
Inventory Analysis
Time Series Analysis
Monthly Demand Trends
Quarterly Demand Trends
Seasonal Analysis
Year-over-Year Analysis
External Factors Analysis
Promotion Impact
Discount Impact
Weather Impact
Competitor Pricing Impact
Epidemic Impact
Visualizations
Histograms
Boxplots
Heatmaps
Trend Analysis
Correlation Analysis
Interactive Plotly Charts
Machine Learning Models

## The following models were trained and evaluated:

Linear Regression: Used as a baseline forecasting model.

Random Forest Regressor: Used to capture complex nonlinear relationships.

Gradient Boosting Regressor: Used for improved forecasting performance through boosting techniques.

Model Evaluation Metrics

Models were evaluated using:

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score

The best-performing model was selected for deployment.

Inventory Intelligence & Restocking Engine

The project includes an intelligent inventory recommendation system.

## Features
Forecast Demand Calculation
Safety Stock Calculation
Reorder Point Calculation
Restocking Quantity Recommendation
Inventory Risk Assessment
Inventory Status Levels
Urgent Restock
Low Stock
Sufficient Stock
Restocking Formula
Safety Stock = Forecast Demand × 20%

Reorder Point = Forecast Demand + Safety Stock

Restock Quantity = Reorder Point − Current Inventory

## Technologies Used
Programming Language
Python
Data Analysis
Pandas
NumPy
Data Visualization
Matplotlib
Seaborn
Plotly
Machine Learning
Scikit-Learn
Deployment
Streamlit

## Project Workflow
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Demand Forecasting
        ↓
Restocking Recommendation
        ↓
Deployment

## Key Features

✅ Advanced Exploratory Data Analysis

✅ Demand Forecasting

✅ Inventory Optimization

✅ Restocking Recommendation Engine

✅ Business Intelligence Dashboard

✅ Interactive Visualizations

✅ Machine Learning Model Comparison

✅ Real-Time Demand Prediction
