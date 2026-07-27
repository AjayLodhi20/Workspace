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
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])