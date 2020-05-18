import pandas as pd
df = pd.read_csv("/Users/alee/PycharmProjects/P2_SP20/Notes/NotesB/titanic.csv")

df.groupby('Sex')["Survived"].sum().plot.bar()

df.groupby('Sex')["Fare"].mean()
# group by multiple columns (in order shown)
df.groupby(['Sex', 'Pclass'])['Survived']
df.groupby(['Sex', 'Pclass'])['Survived'].mean()
df.groupby(['Sex', 'Pclass', 'Survived'])['Age'].mean().plot.bar()
df.groupby('Age')['Survived'].sum()
grouped = df.groupby(['Sex', 'Pclass'])['Survived'].mean()
print(grouped['female'])
print(grouped['female'][1])
print(type(grouped['female']))
grouped = df.groupby(['Sex', 'Pclass'])['Survived'].mean().plot()