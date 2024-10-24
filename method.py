# Modify the mission class 
# Add a method that returns an instance of the Mission class 
# Data extracted from mission.csv (pandas) 

class hello: 
    def __init__(self, config): 
        self.name = config['name'] 
        self.age = config['age']

    def what_name(self) : 
        return "Hello" + self.name 
    
    def what_age(self): 
        return "You are" + str(self.age) + "years old"


config = {'name' : 'Jia Yi', 'age': 21}

dev = hello(config)

print(dev.what_age())