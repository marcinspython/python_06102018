import pandas as pd

df = pd.read_csv("files/titanic_train.csv")
df.head()

df[['Survived', 'Pclass']]

# Out[6]:
#
# 0    549
# 1    342
# Name: Survived, dtype: int64

df.Survived.value_counts()
# pobiera ostatni wiersz tabeli
df[-1:]
# pobiera pierwszy wiersz tabeli
df.head(1)

# wyswietla metody obiektu survived
dir(df.Survived)
# wyswietla wszystkie metody
dir(df)

# srednia wieku tytanica
df.Age.mean()

# mediana wieku
df.Age.median()

### Wybieranie przez labe;e - loc[]


------------------
# Load 'titanic_train.csv' CSV file and save last 5 rows in Excel format
#
import pandas as pd
df = pd.read_csv("files/titanic_train.csv")
df.tail(5).to_excel("files/titanic_last5_train.xlsx")
# Load Excel file from previous exercise and save it again with only first four columns
df = pd.read_excel("files/titanic_last5_train.xlsx")
df.iloc[:,:4].to_excel("files/last_5_4.xlsx")
---
