
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("C:\\Users\\Vishnu Prahalathan\\Desktop\\Titanic-Dataset.csv")  

print(df.head())
print(df.info())
print("Shape:", df.shape)
print("Data Types:\n", df.dtypes)
print(df.describe(include='all'))

print("Missing Values:\n", df.isnull().sum())
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)


print("Skewness:\n", df.skew(numeric_only=True))

numeric_features = df.select_dtypes(include=np.number).columns.tolist()
df[numeric_features].hist(bins=15, figsize=(15, 10))
plt.tight_layout()
plt.savefig('histograms.png')
plt.show()


for col in ['Age', 'Fare']:
    sns.boxplot(data=df, y=col)
    plt.title(f'Boxplot of {col}')
    plt.savefig(f'boxplot_{col}.png')
    plt.show()


for col in ['Sex', 'Pclass', 'Embarked', 'Survived']:
    sns.countplot(data=df, x=col)
    plt.title(f'Countplot of {col}')
    plt.savefig(f'countplot_{col}.png')
    plt.show()


plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()


selected = ['Survived', 'Age', 'Fare', 'Pclass']
sns.pairplot(df[selected], hue='Survived')
plt.savefig('pairplot_selected.png')
plt.show()


sns.violinplot(data=df, x='Pclass', y='Age', hue='Survived', split=True)
plt.title("Violin Plot: Age vs Pclass vs Survived")
plt.savefig("violinplot.png")
plt.show()

sns.swarmplot(data=df.sample(200), x='Pclass', y='Fare', hue='Survived')
plt.title("Swarm Plot: Fare vs Pclass vs Survived")
plt.savefig("swarmplot.png")
plt.show()

cor_matrix = df.corr(numeric_only=True)
high_corr = cor_matrix[(cor_matrix > 0.7) & (cor_matrix < 1.0)]
print("Potential multicollinearity:\n", high_corr)

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

sns.barplot(data=df, x='IsAlone', y='Survived')
plt.title("Survival vs IsAlone")
plt.savefig("is_alone_vs_survival.png")
plt.show()
