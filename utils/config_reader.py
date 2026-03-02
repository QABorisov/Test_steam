import json


class ConfigReader:
    def __init__(self):
        PATH = "config.json"
        with open(PATH, "r") as file:
            self.config = json.load(file)

    def get(self, key):
        return self.config.get(key)
