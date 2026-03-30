# ML-FASTAPI
This project is an end-to-end Machine Learning application that performs customer segmentation on wholesale customers using the K-Means clustering algorithm.

It includes:

Data preprocessing and feature engineering
K-Means clustering model training
Cluster interpretation
Model deployment using FastAPI
A simple HTML web interface for predictions
Background task logging

🚀 Features
Clean and preprocess wholesale customer dataset
Train K-Means clustering model
Save and load trained model using joblib
Predict customer cluster from user input
Interpret clusters with business meaning
Web interface using HTML form
API built with FastAPI
Background logging of user inputs
🧠 Problem Statement

The goal is to segment wholesale customers into different groups based on their purchasing behavior so that businesses can:

Understand customer types
Target marketing strategies
Improve decision-making
📂 Dataset Features

The dataset includes the following features:

Channel – Customer channel (Hotel/Restaurant or Retail)
Region – Customer region
Fresh – Annual spending on fresh products
Milk – Annual spending on milk products
Grocery – Annual spending on grocery items
Frozen – Annual spending on frozen products
Detergents_Paper – Spending on detergents & paper products
Delicassen – Spending on delicatessen products
⚙️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn (K-Means, Pipeline, StandardScaler)
FastAPI ⚡
HTML (Frontend form)
Joblib (Model serialization)
🏗️ Project Workflow
Data Cleaning
Feature Engineering
Handling missing/invalid values
Scaling numerical features
Training K-Means clustering model
Determining optimal number of clusters
Saving the trained model
Building FastAPI backend
Creating HTML form for input
Making predictions via API
Interpreting clusters into business categories
📊 Cluster Interpretation (Example)

Cluster	Meaning
0	Retail customers with high grocery & detergent spending
1	Hotel/Restaurant customers with high fresh & milk spending
2	Low spending budget customers
3	Balanced spending customers
🌐 API Endpoints
🔹 Home
GET /home

Returns welcome message.

🔹 Form UI
GET /

Displays HTML form for input.

🔹 Prediction
POST /submit

