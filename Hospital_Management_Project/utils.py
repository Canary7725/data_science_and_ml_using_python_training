import json


def findBook(title):
    print("Book found.")


def getConfig(config_file_path):
    with open(config_file_path, 'r') as file:
        config = json.load(file)
    return config
