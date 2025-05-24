# Linear vs Non-Linear Regression Analysis

This project demonstrates and compares linear and polynomial regression approaches as part of the Harvard Data Science course.

## Description

This analysis explores how non-linear relationships in data can be modeled using polynomial regression, comparing its performance against simple linear regression. The project includes practical implementations and visual analysis of both approaches.

## Project Structure

### Library Imports
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computations
- `matplotlib`: Data visualization
- `sklearn`: Machine learning implementations
  - `LinearRegression`
  - `PolynomialFeatures`
  - `train_test_split`

### Main Components

1. **Data Preparation**
   - Reading the `poly.csv` dataset
   - Converting data to numpy arrays
   - Initial data visualization

2. **Dataset Split**
   - Training (80%) and test (20%) set separation
   - Use of `train_test_split` with fixed random state

3. **Regression Models**
   - Linear Regression:
     - Basic linear model implementation
     - Predictions on test data
     - Visualization of linear fit
   - Polynomial Regression:
     - Polynomial feature transformation (degree 3)
     - Model fitting and predictions
     - Comparison with linear approach

4. **Residual Analysis**
   - Distribution of residuals:
     - Histograms for both models
     - Frequency analysis
   - Residuals vs Predicted Values:
     - Scatter plots for both models
     - Zero residual reference line
     - Visual comparison of model performances

5. **Visualizations**
   - Raw data scatter plots
   - Model predictions comparison
   - Comprehensive residual analysis
   - Side-by-side model performance comparisons

## Results

The project contains one main notebook:

1. `poly.ipynb`:
   - Implements both linear and polynomial regression
   - Provides visual comparison of both approaches
   - Includes detailed residual analysis
   - Demonstrates why polynomial regression is more appropriate for non-linear relationships