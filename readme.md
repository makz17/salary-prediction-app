# Software Developer Salary Prediction Application

## Project Overview

This project utilizes Stack Overflow Annual Developer Survey [dataset](https://insights.stackoverflow.com/survey) to build a machine learning model for predicting software engineer salaries. This is facilitated by taking in users inputs such as  education, experience, and location through Streamlit UI. It also provides some salary stats based location and level of experience. 

## Project Execution

### 1. Data Cleaning

- **Initial Filtering:** Loaded Stack Overflow survey data and selected columns: `Country`, `EdLevel`, `YearsCodePro`, `Employment`, and `ConvertedComp` (salary).
- **Missing Data:** Removed rows with missing or null salary values and dropped incomplete entries.
- **Employment Filter:** Focused on full-time employed respondents for consistency.
- **Outlier Removal:** Kept only salaries between \$10,000 and \$250,000 to reduce skewness and improve model reliability.
- **Country Grouping:** Merged countries with low representation into an "Other" category for statistical significance.
- **Feature Normalization:** Standardized experience (e.g., "More than 50 years" → 50, "Less than 1 year" → 0.5) and consolidated education levels.

### 2. Feature Selection

- **Final Features:** Used `Country`, `EdLevel`, and `YearsCodePro` as predictors for salary.

### 3. Model Training

- Tried multiple regression models including Linear Regression, Decision Tree, and Random Forest.
- Used GridSearchCV to optimize model parameters (e.g., Decision Tree depth).
- Selected the best-performing regressor based on validation metrics and saved the model pipeline for deployment.

### 4. Model Saving

- Saved the trained model and preprocessing steps using `pickle` for reusing in the web application.

### 5. Streamlit Web Application

- The app features two main pages - **Explore** (visualize salary trends) and **Predict** (get salary estimates) accessible through a sidebar.
- Users can visualize salary distributions by country, education and experience using interactive plots.
- Users input their details, and the app displays a real-time salary prediction using the trained model.

### 6. Performance Optimization

- **Caching:** Used Streamlit's built-in caching that makes the app load instantly instead of re-processing everything each time.
