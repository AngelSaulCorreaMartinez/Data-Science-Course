# Multi-linear vs Linear Regression

This project implements and analyzes different approaches to linear regression models as part of the Harvard Data Science course.

## Description

Linear regression is a supervised learning method used to predict continuous values. This project includes practical examples and detailed explanations to understand both simple linear regression and multivariate regression models.

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
   - Simple Linear Regression (`multi-linear_vs_linear.ipynb`):
     - Individual models for each predictor (TV, Radio, Newspaper)
     - Comparison of R² values for train and test sets
     - Visualization of predictions vs actual values
   - Multiple Linear Regression Analysis (`multi-linear_model.ipynb`):
     - Evaluation of all possible predictor combinations
     - Mean Squared Error (MSE) calculation for each combination
     - Performance comparison between different predictor sets

4. **Visualizations**
   - Scatter plots for training and test data
   - Fitted lines for linear models
   - Comparison of predicted vs actual values

5. **Model Evaluation**
   - R² values for simple linear models
   - MSE values for different predictor combinations
   - Performance comparison across all model variations

## Results

The project contains two main notebooks:

1. `multi-linear_vs_linear.ipynb`:
   - Compares individual predictor performance
   - Implements simple and multivariate regression
   - Visualizes results and calculates R² metrics

2. `multi-linear_model.ipynb`:
   - Analyzes all possible predictor combinations
   - Evaluates model performance using MSE
   - Determines optimal predictor combinations