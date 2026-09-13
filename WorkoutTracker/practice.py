import pandas as pd


data1 = {"Name": "harsh", "age" : 28}

data = {
    "Name": ["ajay", "satyam", "azaad"],
    "age": [25, 26, 27]
}

for key_in_data in data.keys():
    for key_in_data1 in data1.keys():
        if key_in_data == key_in_data1:
            data[key_in_data].append(data1[key_in_data1])

df = pd.DataFrame(data)

print(df)