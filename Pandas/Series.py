# pandas is fast data analytisc library built on the top of the numpy .


# series from list .




import matplotlib.pyplot as plt
import pandas as pd
# string type series
country=['india','pakistan','nepal','usa']
print(pd.Series(country))

print("---------------------------------------------")

# integer type series
runs=[12,23,25,86]
print(pd.Series(runs))

print("---------------------------------------------")


# custom index and then provide name also .
marks=[10,20,30,40]
subject=['c','php','.net','javascript']
print(pd.Series(marks ,index=subject ,name='khushi Ke marks'))


print("---------------------------------------------")






# Series from dictionary .

product={
    'name':'car',
    'colour':'black',
    'price':100000,
}

dic_series=pd.Series(product ,name='Car Details')
print(dic_series)

print("---------------------------------------------")







# Series Attributes .
# 1.size
# 2.dtype
# 3.is_unique
# 4.values
# 5.Index
# 6.name






# 1.Atrribute.
# size
# It returns the total number of elements in the Series.
marks=[10,20,30,40]
marks_size=pd.Series(marks)
print("size",marks_size.size)


print("---------------------------------------------")


# 2.Atrribute.
# dtype
# it return the datatype of item in series.

print("dtype",marks_size.dtype)


print("---------------------------------------------")



# 3.name
# it return the name in series.

print("name",marks_size.name)
print("name",dic_series.name)


print("---------------------------------------------")


# 4.is_unique.

# it check is there any unique value in series.
# it return true is there is no duplicate vales.
# it return false if there is duplicate vales in series.

print("unique",marks_size.is_unique)
s=pd.Series([1,1,2,2]).is_unique
print("unique",s)



print("---------------------------------------------")

# 5.index.
# it return index object means ki ye index return karta hai hamari series ka .

print("index",marks_size.index)
print("index",dic_series.index)



print("---------------------------------------------")

# 6.value.
# it return value  means ki ye value return karta hai hamari series ka 
# in the form of numpyndarray .

print("value",marks_size.values)
print("value",dic_series.values)
print("type",type(dic_series.values))








print("---------------------------------------------")


# series from the dataset
# with one column 

df = pd.read_csv('kohli_ipl.csv')
df_series= df['runs']


print(df)
print(df_series)



print("---------------------------------------------")


# ================================= Practice questions ==========================

# data analyst level Pandas
# total runs
# highest score
# average
# strike rate analysis
# visualization

# total runs
total_runs=df_series.sum()
print("Total Runs ",total_runs)


print("---------------------------------------------")

# highest score
highest_score=df_series.max()
print("highest_score",highest_score)

print("---------------------------------------------")

# average score
average_score=df_series.mean()
print(average_score)


print("---------------------------------------------")


# Runs distribution

summary=df_series.describe()
print(summary)


