# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("../../OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# with open("my_file.txt", mode="w") as file:
#     file.write("new text.")


# with open("my_file.txt", mode="a") as file:
#     file.write("hi my name is ajay singh lodhi.")

# with open("new_file.txt", mode="w") as file:
#     file.write("new text.")