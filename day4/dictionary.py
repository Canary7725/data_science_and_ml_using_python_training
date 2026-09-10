
student_record = {
    "roll": 101,
    "name": "Adam",
    "grade": 9
}


# # print(student_record["role"]) #Accessing value by key similar to list.
# # print(student_record.get("rol")) #Safe access of value; if key doesn't exists then returns None or the default value

# student_record["name"] = "Chloe"  # Updating value using key
# student_record["age"] = 16  # Adding a new entry onto the dictionary


# print(student_record)


students_records = [
    {
        "roll": 101,
        "name": "Adam"
    },
    {
        "roll": 102,
        "name": "Chloe"
    },
    {
        "roll": 103,
        "name": "Oliver",
        "age": 18
    }
]

print(students_records[0]["name"])


sample = {
    101: {"name": "Adam", "age": 17},
    102: {"name": "Chloe", "age": 18}
}


print(sample[101])
