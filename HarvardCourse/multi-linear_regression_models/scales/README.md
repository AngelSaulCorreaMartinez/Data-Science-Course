# Features on Different Scales in Linear Regression

This project explores how different scales in predictor variables affect linear regression models as part of the Harvard Data Science course.

## Description

This project demonstrates how scaling and unit conversion of predictor variables impacts the interpretation of regression coefficients. It provides practical examples to understand feature scaling effects in linear regression models.

## Project Structure

### Library Imports
- `pandas`: Data handling and analysis
- `numpy`: Numerical operations and arrays
- `matplotlib`: Data visualization
- `sklearn`: Machine learning algorithm implementation

### Main Components

1. **Data Preparation**
   - Reading the `Advertising.csv` dataset
   - Initial analysis with original dollar scale
   - Converting predictors to different currencies:
     - TV budget to Sri Lankan Rupees
     - Radio budget to South Korean Won
     - Newspaper budget to Ghanaian Cedi

2. **Initial Model**
   - Fitting a linear regression with dollar-scaled predictors
   - Analysis of coefficient interpretations
   - Understanding the relationship between predictors and sales

3. **Scale Transformation**
   - Converting predictor variables to different currencies
   - Understanding the impact of different scales
   - Analysis of coefficient changes under scaling

4. **Visualizations**
   - Bar plots of regression coefficients
   - Comparison of coefficients across different scales
   - Visual interpretation of scaling effects

5. **Model Comparisons**
   - Analysis of R² values across different scales
   - Understanding coefficient interpretation changes
   - Impact of scaling on model interpretability

## Results

The `features_on_different_scales.ipynb` notebook contains:
- Complete analysis of scaling effects
- Visual comparisons of coefficient interpretations
- Practical examples of currency conversions
- Implications for model interpretation