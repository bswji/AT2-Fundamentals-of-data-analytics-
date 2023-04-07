import pandas as pd

#Load data
data = pd.read_csv("/Users/brandonji/Documents/Uni/Sem 1 2023/Fundamentals of data analytics/FLY32130_DataSet_24579183.csv")

#Create dataframe and remove id and unnamed:0 columns
data.sample(1)
data = pd.DataFrame(data)
data = data.drop(columns = ["Unnamed: 0", "id"])

#Find unique values in customer type 
data['Customer Type'].unique()

#Find unique values in type of travel
data['Type of Travel'].unique()

#Find unique values of Class
data['Class'].unique()

#Find unique values of flight distance
data['Flight Distance'].unique()

data['Inflight wifi service'].unique()
data['Departure/Arrival time convenient'].unique()
data['Ease of Online booking'].unique()
data['Gate location'].unique()
data['Food and drink'].unique()
data['Online boarding'].unique()
data['Seat comfort'].unique()
data['Inflight entertainment'].unique()
data['On-board service'].unique()
data['Leg room service'].unique()
data['Baggage handling'].unique()
data['Checkin service'].unique()
data['Inflight service'].unique()
data['Cleanliness'].unique()
data['Departure Delay in Minutes'].unique()
data['Arrival Delay in Minutes'].unique()
data['satisfaction'].unique()

sum(data['Inflight wifi service'] == 0)

#Summary statistics
#