my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

for key, values in my_family.items():
    print(f"{values['name']} is my {key} and is {str(values['age'])} years old")