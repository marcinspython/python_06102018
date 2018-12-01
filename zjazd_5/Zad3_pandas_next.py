# .............Wróćmy do wykładu - Zmiana typów danych w czasie odczytu

# Display passengers with Age above 50
df[df.Age>50]

# Display passengers that Embarked at location S and are female
df[(df.Embarket == 'S') & (df.Sex == 'female')]

# Display passengers that paid for ticket more than 50 and are not in first class
df[(df.Fare>50) & (df.Pclass !=1)]

# Display all passengers with Names that contain 'Johnson' (it's a surname)
df[df.Name.str.contains("Johnson")]

# srednia wieku dla konbiet i mezczyzn
df.groupby("Sex").agg({'Age':['mean']})
df.groupby("Sex").agg({'Age':['mean', 'count']})


