# Titanic Dataset - Exploratory Data Analysis & Feature Engineering

## Project Overview

This project performs Exploratory Data Analysis (EDA) and Feature Engineering on the Titanic dataset to prepare it for Machine Learning classification tasks.

The primary objective was to understand the dataset, identify meaningful patterns, handle missing values, engineer informative features, and transform the data into a machine-learning-ready format.

---

## Dataset

The dataset contains passenger information from the Titanic disaster, including demographic details, ticket information, cabin information, fare paid, passenger class, and survival status.

### Target Variable

* **Survived**

  * 0 = Did Not Survive
  * 1 = Survived

---

## Exploratory Data Analysis

The following analyses were performed:

* Missing value analysis
* Distribution analysis of numerical features
* Survival rate comparison across categories
* Relationship between passenger class and fare and many more relevant comparisons were made
* Cabin information exploration
* Ticket information investigation
* Correlation analysis between features

---

## Feature Engineering

### 1. Title Extraction

Passenger titles were extracted from the Name column.

Examples:

* Mr
* Mrs
* Miss
* Master
* Dr

This captures additional demographic information beyond age and gender.

---

### 2. Cabin Availability

A binary feature was created to indicate whether cabin information was available.

* 1 = Cabin information present
* 0 = Cabin information missing

This helps determine whether cabin assignment has any relationship with survival.

---

### 3. Cabin Deck Extraction

The deck letter was extracted from the Cabin column.

Examples:

* C85 → C
* E46 → E
* F33 → F

This feature was used to investigate whether deck location influenced survival probability.

---

### 4. Ticket Group Size

Passengers sharing the same ticket number were identified.

A feature was created to represent the number of passengers traveling under the same ticket.

This serves as an indicator of group travel behavior.

---

### 5. Passenger Class Transformation

Passenger class information was analyzed alongside fare and survival patterns to better represent socioeconomic status within the dataset.

---

## Data Preprocessing

### Missing Values

Missing values were identified and handled appropriately during preprocessing.

### Categorical Encoding

Categorical variables were transformed using One-Hot Encoding.

Examples include:

* Sex
* Embarked
* Title
* Cabin Deck

No ordinal encoding was used for features that lacked a meaningful natural order.

---

## Final Dataset

The final dataset consists of:

* Numerical features
* Engineered features
* One-hot encoded categorical variables

The resulting dataset is suitable for training machine learning classification models.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## Learning Outcomes

Through this project, the following concepts were practiced:

* Data Cleaning
* Missing Value Analysis
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Categorical Encoding
* Data Visualization
* Machine Learning Data Preparation

---

## Future Work

The processed dataset can be used to train and evaluate classification models such as:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost

and compare their predictive performance on Titanic survival prediction.
