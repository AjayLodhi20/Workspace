# with open("weather_data.csv") as csv_file:
#     modified_csv = csv_file.readlines()
#     new_list = [i.strip() for i in modified_csv]
#     print(new_list)

import pandas

new_file = pandas.read_csv("weather_data.csv")
print(new_file)

# print(new_file.to_dict())
temp_list = new_file["day"].to_list()
print(temp_list)

# monday = new_file[new_file["temp"] == new_file["temp"].max()]
# print(monday)

highest_temp = new_file[new_file["temp"] == 15]
print(highest_temp["day"])
