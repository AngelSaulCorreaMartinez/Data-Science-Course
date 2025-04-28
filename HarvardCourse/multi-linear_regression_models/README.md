# Multi-linear vs Linear Regression

This project implements and compares simple linear and multivariate regression models as part of the Harvard Data Science course.

## Description

Linear regression is a supervised learning method used to predict continuous values. This project includes practical examples and detailed explanations to understand its operation.

## Project Structure

### Library Imports
- `pandas`: Data handling and analysis
- `numpy`: Numerical operations and arrays
- `matplotlib`: Data visualization
- `sklearn`: Machine learning algorithm implementation

### Main Components

1. **Data Preparation**
   - Reading the `Advertising.csv` dataset
   - Cleaning unnecessary data
   - Separation into predictor variables (`TV`, `Radio`, `Newspaper`) and target variable (`Sales`)

2. **Dataset Split**
   - Separation into training (80%) and test (20%) sets
   - Use of `train_test_split` for random division

3. **Regression Models**
   - Fitting simple linear regression models for each predictor
   - Fitting a multivariate regression model using all predictors

4. **Visualizations**
   - Scatter plots for training and test data
   - Fitted line for linear models
   - Comparison of predicted vs actual values

5. **Model Evaluation**
   - Calculation of R² values for each model
   - Comparison of performance between simple linear and multivariate models

## Results

The `multi-linear_vs_linear.ipynb` notebook contains the complete implementation with:
- Exploratory data analysis
- Fitting of simple linear and multivariate models
- Result visualizations
- Model performance metrics