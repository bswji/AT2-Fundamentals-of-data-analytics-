import pandas as pd

#Load data
data = pd.read_csv("/Users/brandonji/Documents/Uni/Sem 1 2023/Fundamentals of data analytics/FLY32130_DataSet_24579183.csv")

#Create dataframe and remove id and unnamed:0 columns
data.sample(1)
data = pd.DataFrame(data)
data = data.drop(columns = ["Unnamed: 0", "id"])

#Find unique values in customer type 
data['Customer Type'].unique()

