import pandas
# with open("./weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv('weather_data.csv')
# data.temp.tolist()
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 9/5 + 32)

# """creating a dataframe from scratch"""
# dict_student = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(dict_student)
# data.to_csv("new_data.csv")

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_count = 0
# red_count = 0
# black_count = 0
# list_data = data["Primary Fur Color"].tolist()
# for i in list_data:
#     if i == "Gray":
#         grey_count += 1
#     elif i == "Cinnamon":
#         red_count += 1
#     elif i == "Black":
#         black_count += 1

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

color = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_count, red_count, black_count]
}

solution = pandas.DataFrame(color)
solution.to_csv("squirrel_count.csv")
# print(grey_count)
# print(red_count)
# print(black_count)
