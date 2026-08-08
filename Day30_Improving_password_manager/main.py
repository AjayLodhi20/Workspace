# try:
#     file = open("a_file.txt")
#     dictionary = {"key" : "value"}
#     print(dictionary["key"])
# except FileNotFoundError:
#     # print("there was an error")
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"that key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed")
#     raise KeyError("nothing")