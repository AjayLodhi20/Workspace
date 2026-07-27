#TODO: Create a letter using starting_letter.txt

file = open("./Output/ReadyToSend/example.txt")
message = file.readlines()

invites = open("./Input/Names/invited_names.txt")
names = invites.readlines()

filtered_message = [i.strip() for i in message]

i = 0
for i, name in enumerate(filtered_message):
    filtered_message.remove(name)
    i += 2

print(filtered_message)

filtered_names = []
for name in names:
    txt = name.strip()
    filtered_names.append(txt)

print(filtered_names)


for txt in filtered_names:
    for i in filtered_message:
        x = i.replace(txt, "Aang")
        
print(x)
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp