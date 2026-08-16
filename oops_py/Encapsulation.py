# Key concepts of Encapsulation 

# 1. Public Member ---> kahise bhii acces
# 2. Protected Member --->
# 3. Privet Member
# 4. Gater and seter methods

# -----> 1. Public Member <------

class Ironman:
    def __init__(self,name,power,weapon):
        self.name = name
        self.power= power
        self.weapon = weapon

    def intro(self):
        print(f"Hello my name is {self.name} and i have {self.weapon}")

iron=Ironman("Amit","Chaku hai", "hahaha")

print(dir(iron))





