# Parent Class
class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduction(self):
        print(f"My name is {self.name}.")    

# Child Class
class Iron(Avenger):
    def __init__(self, name, power, weapon):
        super().__init__(name, power)     
        self.weapon = weapon   

    def show_weapon(self):
        print(f"I use {self.weapon}.")

# Instance 1: Child Class Object (Has access to Parent + Child methods)
tony = Iron("Tony Stark", "Genius Intellect", "Mark 85 Suit")
print(tony.name)          # Output: Tony Stark
tony.introduction()       # Output: My name is Tony Stark.
tony.show_weapon()        # Output: I use Mark 85 Suit.

print("-" * 20)

# Instance 2: Parent Class Object (Only accepts 2 arguments, no weapon method!)
tony2 = Avenger("To Stark", "Ge Intellect") 
print(tony2.name)         # Output: To Stark
tony2.introduction()      # Output: My name is To Stark.
# tony2.show_weapon()     # REMOVED: This line would cause an AttributeError!
