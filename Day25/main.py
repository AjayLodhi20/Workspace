# with open("./weather_data.csv") as csv_File:
#     modified_csv = csv_File.readlines()
#     csv_files = []
#     for csv in modified_csv:
#         stripped_csv = csv.strip()
#         csv_files.append(stripped_csv)
#     print(csv_files)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # avg = round((sum(temp_list)/len(temp_list)), 2)
# # print(avg)
#
# print(data.temp.mean())
#
# print(data["temp"].max())
#
# # get datas in columns
# print(data["condition"])
# # or
# print(data.condition)
#
# # get datas which are in rows
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# print(monday_temp)
# print((monday_temp * 1.8) + 32)

# create a df from scratch

# data_dict = {
#     "students": ["amy", "james", "angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])

fur_color_list = data["Primary Fur Color"].to_list()
print(fur_color_list)

Gray = fur_color_list.count("Gray")
Cinnamon = fur_color_list.count("Cinnamon")
Black = fur_color_list.count("Black")


data_dict = {
    'color': ["Gray", "Cinnamon", "Black"],
    'counting': [Gray, Cinnamon, Black]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("fur_colors.csv")


