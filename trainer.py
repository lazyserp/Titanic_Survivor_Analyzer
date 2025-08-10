import pandas

#Cleaning Data

pd = pandas.read_csv("train.csv")

df = pandas.DataFrame(pd)
# pd.head()

# Get mathematical details about numerical columns
print(  pd.describe() )

#checking missing values
print(pd.isnull().sum() )


# filling null values with median 
df["Age"].fillna(df["Age"].median())

#filling values with mode
df["Embarked"].fillna(df["Embarked"].mode()[0])

#Since cabin column has too many null values , dropping it
pd.drop(columns=["Embarked"])



# EDA
survival_rate = df["Survived"].mean() * 100
print(f" Overall survival rate: { survival_rate:.2f}%")

#Survival by gender
print( df.groupby("Sex")["Survived"].mean() * 100  )


# Best Part ( Plotting now)
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x="Sex",y="Survived",data=df)
plt.show()