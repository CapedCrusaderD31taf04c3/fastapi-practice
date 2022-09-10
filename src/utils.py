import re

def validate_longitude(longitude):
    return True if re.fullmatch(
        "^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$", 
        longitude
        ) else False

def validate_lattitude(lattitude):
    return True if re.fullmatch(
        "^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$",
    lattitude
    ) else False

def validate_longitude_and_lattitude(longitude="", lattitude=""):
    return True if all([
        validate_longitude(longitude),
        validate_lattitude(lattitude)
    ]) else False
