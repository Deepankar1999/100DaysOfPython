# """
# with open("./day25/weather_data.csv") as file:
#     data=file.readlines()
#     print(data)"""
# """
# import csv
# with open("./day25/weather_data.csv") as file:
#     data_file=csv.reader(file)
#     temperature=[]
#     for data in data_file:
#         if data[1]!="temp":
#             temperature.append(int(data[1]))
#     print(temperature)
#     """
# import pandas
# data=pandas.read_csv("./day25/weather_data.csv")
# print(data[data.temp == data.temp.max()])

import pandas

data=pandas.read_csv("./day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels,red_squirrels,black_squirrels]
}

df=pandas.DataFrame(data_dict)
df.to_csv("./day25/squirrel_count.csv")

