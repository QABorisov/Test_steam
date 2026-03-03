import json


class ConfigReader:
    PATH = "config.json"

    def __init__(self):
        with open(self.PATH, "r") as file:
            self.config = json.load(file)

    def get(self, key):
        return self.config.get(key)
