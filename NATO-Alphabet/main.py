student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabets = pandas.DataFrame(df)

letters = [row.letter for (index, row) in df.iterrows()]
code = [row.code for index,row in df.iterrows()]

nato = {k:v for k, v in zip(letters,code)}
print(nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word_input = input("Enter a word: ").upper()
nato_alphb = [nato[i] for i in word_input]
print(nato_alphb)

