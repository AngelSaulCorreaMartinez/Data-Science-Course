# Dummy/Indicator Variables in Linear Regression

This project implements linear regression models using dummy variables for categorical predictors as part of the Harvard Data Science course.

## Description

Linear regression with dummy variables is a method to incorporate categorical predictors into regression models. This project includes practical examples and detailed explanations to understand how to handle qualitative data in regression analysis.

## Project Structure

### Library Imports
- `pandas`: Data handling and analysis
- `numpy`: Numerical operations and arrays
- `seaborn`: Advanced data visualization
- `sklearn`: Machine learning algorithm implementation

### Main Components

1. **Data Preparation**
   - Reading the `credit.csv` dataset
   - Cleaning unnecessary data
   - Identification of numeric and categorical variables
   - Creation of dummy variables for categorical predictors

2. **Initial Model**
   - Fitting a linear regression model with only numeric predictors
   - Understanding the limitations of excluding categorical variables
   - Evaluation of model performance

3. **Dummy Variable Creation**
   - Converting categorical variables to dummy/indicator variables
   - Understanding the concept of reference categories
   - Proper handling of categorical data in regression

4. **Advanced Model**
   - Fitting a model with both numeric and categorical predictors
   - Analysis of coefficient interpretations
   - Understanding the impact of categorical variables

5. **Visualizations**
   - Coefficient plots for feature importance
   - Separate regression lines for different categorical values
   - Visual representation of categorical effects

6. **Model Evaluation**
   - Analysis of categorical variable effects
   - Interpretation of dummy variable coefficients
   - Comparison of models with and without categorical predictors

## Results

The `dummy_indicator_variables.ipynb` notebook contains the complete implementation with:
- Handling of categorical variables
- Creation and use of dummy variables
- Visual analysis of categorical effects
- Model performance comparison