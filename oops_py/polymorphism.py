#In programming, it means different objects can
#use the exact same action name, but they do it in their own unique way.

#Overriding: Changing an inherited method in a child class. (Works perfectly in Python).
#Overloading: Writing multiple methods with the same name but different arguments in the same class. (Python does not support this natively, but has a workaround).

class Avenger:
    def attack(self):
        print("Basic punch! 👊")

class IronMan(Avenger):
    # Overriding the parent's attack method
    def attack(self):
        print("Fires repulsor blast! 💥")

tony = IronMan()
tony2 = Avenger()
tony2.attack()
tony.attack() 