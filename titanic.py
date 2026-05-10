
import pandas as pd

df = pd.read_csv("tested.csv")

print("Orignal Dataset")
print(df.head())

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'], inplace=True)

df.drop_duplicates(inplace=True)

df['Survived'] = df['Survived'].astype(int)

df['Pclass'] = df['Pclass'].astype('category')

df.rename(columns={
    'PassengerId': 'Passenger_ID', # 'E'
    'Pclass': 'Pass_Class',
    'Sex': 'Gender',             # 'E'
    'SibSp': 'Sib_Sp',
    'Parch': 'Par_Ch',
    'Fare': 'Ticket_Fare'        
}, inplace=True)

print("\nClened Dataset")
print(df.head())

df.to_csv("Clened_Titanic.csv", index=False)

print("\ndonee")

