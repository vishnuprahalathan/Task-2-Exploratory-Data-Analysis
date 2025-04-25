# Task-2-Exploratory-Data-Analysis\

This project is part of the AI & ML Internship Task 2 and focuses on performing **Exploratory Data Analysis (EDA)** on the Titanic dataset to discover patterns and insights using Python libraries such as Pandas, Matplotlib, Seaborn, and Plotly.

---
 Objectives

- Understand the dataset using descriptive statistics and visualizations
- Identify missing values, distributions, and correlations
- Explore patterns related to survival rate
- Engineer new features like `FamilySize` and `IsAlone`
- Practice data storytelling through visual exploration

---
 Tools Used

- Python 3.x
- Jupyter Notebook / VS Code
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly (optional, interactive visuals)

---

Dataset

- Dataset Name: **Titanic - Machine Learning from Disaster**
- Source: [Kaggle Dataset Link](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- File Used: `Titanic-Dataset.csv`

---

 EDA Process

1. Data Loading & Cleaning
- Loaded the dataset using `pandas.read_csv()`
- Handled missing values:
  - `Age`: filled with median
  - `Embarked`: filled with mode

2. Descriptive Statistics
- Used `.describe(include='all')` to analyze data types and distributions
- Identified skewness in numeric features
- Checked dataset shape, column types, and missing values

3. Visual Analysis

 Univariate Visuals:
- **Histograms**: Age, Fare, etc.
- **Boxplots**: Detected outliers in `Age` and `Fare`
- **Countplots**: Categorical variables like `Sex`, `Embarked`, `Pclass`, and `Survived`

Bivariate/Multivariate Visuals:
- Correlation heatmap to detect linear relationships
- Pairplot to understand joint distributions
- Violin plot to show distribution split by survival
- Swarm plot for passenger class vs fare vs survival

Feature Engineering:
- Created `FamilySize = SibSp + Parch + 1`
- Created `IsAlone` (1 if no family, 0 otherwise)
- Compared survival rate with `IsAlone` using a barplot

---

Key Insights

- Females had a higher survival rate than males.
- Passengers in higher classes (`Pclass=1`) were more likely to survive.
- Being alone (`IsAlone=1`) decreased survival probability.
- Age and Fare had notable outliers and slight right-skewed distributions.

---

Output Files

- `task2.py` – Python script with full EDA
- `.png` visualizations:
  - `histograms.png`
  - `boxplot_Age.png`, `boxplot_Fare.png`
  - `countplot_Sex.png`, `countplot_Pclass.png`, etc.
  - `correlation_heatmap.png`, `pairplot_selected.png`
  - `violinplot.png`, `swarmplot.png`
  - `is_alone_vs_survival.png`

---


