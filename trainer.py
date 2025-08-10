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

print(df.groupby("Pclass")["Survived"].mean() * 100)
sns.barplot(x="Pclass",y="Survived",data=df)
plt.show()


df["AgeGroup"] = pandas.cut(df["Age"], bins=[0,12,18,35,50,80], labels=["Child", "Teen", "Young Adult", "Adult", "Senior"])

print(df.groupby("Age")["Survived"].mean() * 100)
sns.barplot(x='AgeGroup',y="Survived",data=df)
plt.show()


# SHowing Probability
P_female = df[df["Sex"] == "female"]["Survived"].mean()
print(f"Female survival probability: { round(P_female*100 )}")

P_male = df[df['Sex'] == "male"]["Survived"].mean()
print(round(P_male*100))

