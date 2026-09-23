with open("day9/sample.txt", "a") as file:
    file.write("This is a sample file_handling program.\n")
    file.write("This is a sample file_handling program.\n")
    file.write("This is a sample file_handling program.\n")
    file.write("This is content that is to be added onto the sample file.\n")


with open("day9/sample.txt", "r") as file:
    text = file.read()
print(type(text))
