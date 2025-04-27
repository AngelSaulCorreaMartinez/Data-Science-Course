# k-Nearest Neighbors (kNN)

This project implements the k-Nearest Neighbors (kNN) algorithm as part of the Harvard Data Science course.

## Description

The kNN algorithm is a supervised learning method used for classification and regression. This project includes practical examples and detailed explanations to understand its operation.

## Project Structure

### Library Imports
- `pandas`: Data handling and analysis
- `numpy`: Numerical operations and arrays
- `matplotlib`: Data visualization
- `sklearn`: Machine learning algorithm implementation

### Main Components

1. **Data Preparation**
   - Reading 'Advertising.csv' dataset
   - Cleaning unnecessary data
   - Separation into predictor (TV) and target (Sales) variables

2. **Dataset Split**
   - Separation into training (60%) and test (40%) sets
   - Use of `train_test_split` for random division

3. **Finding the Best k**
   - k-value range: 1-70
   - Evaluation of each k using MSE (Mean Squared Error)
   - Visualization of different kNN models

4. **Visualizations**
   - Prediction plots for k=1, k=10, and k=70
   - MSE vs k-values plot
   - Visual representation of model fit

5. **Model Evaluation**
   - MSE calculation for each k value
   - Identification of optimal k
   - R² score calculation to evaluate model fit

## Results

The `finding_best_k_in_knn.ipynb` notebook contains the complete implementation with:
- Exploratory data analysis
- Best k selection process
- Result visualizations
- Model performance metrics