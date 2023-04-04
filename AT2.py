import pandas as pd

data = pd.read_csv("/Users/brandonji/Documents/Uni/Sem 1 2023/Fundamentals of data analytics/FLY32130_DataSet_24579183.csv")

data.sample(1)

data = data.drop(columns = ["Unnamed: 0", "id"])
data.sample(1)

