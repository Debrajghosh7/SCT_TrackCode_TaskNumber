import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
file_path = r"C:\Users\HP\OneDrive\Desktop\DEBRAJ INTERNSHIP\DEBRAJ INTERNSHIP\2\train.csv"  # Replace with the actual path to your dataset
df = pd.read_csv(file_path)

# Data Cleaning
# 1. Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())  # Fill missing 'Age' with the median value
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Fill missing 'Embarked' with the mode
df.drop('Cabin', axis=1, inplace=True)  # Drop the 'Cabin' column

# 2. Convert categorical variables to numerical
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Exploratory Data Analysis (EDA)
# 1. Survival by gender
plt.figure(figsize=(8, 5))
sns.countplot(x='Sex', hue='Survived', data=df, palette='coolwarm')
plt.title('Survival by Gender')
plt.xlabel('Gender (0 = Male, 1 = Female)')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right')
plt.show()

# 2. Survival by passenger class
plt.figure(figsize=(8, 5))
sns.countplot(x='Pclass', hue='Survived', data=df, palette='viridis')
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(title='Survived', loc='upper right')
plt.show()

# 3. Age distribution of passengers
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='blue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 4. Correlation heatmap (only numeric columns)
plt.figure(figsize=(10, 6))
numeric_columns = df.select_dtypes(include=[np.number])  # Select only numeric columns
corr = numeric_columns.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap (Numeric Columns Only)')
plt.show()

# 5. Survival rate by age group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 35, 50, 100], labels=['Child', 'Young Adult', 'Adult', 'Elderly'])
plt.figure(figsize=(8, 5))
sns.barplot(x='AgeGroup', y='Survived', data=df, palette='muted', hue='AgeGroup', legend=False)
plt.title('Survival Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate')
plt.show()
