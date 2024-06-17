import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def get(name, text):
    var = config[name][text]
    return var
