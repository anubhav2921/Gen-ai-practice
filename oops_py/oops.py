#class and object 
class Anubhav:
    def __init__(self,name,power,weapon,nationality):
        self.name = name
        self.weapon = weapon
        self.nationality=nationality

        
#--------> Blue print  <-----------------
    def introduction(self):
        print(f"Hello my name is {self.name}")

    def carrying_weapon(self):
        print(f"i am carrying the wepon {self.weapon}")   
#--------> Blue print  <-----------------

#-------->Object<-----------------
Iron_man = Anubhav("Iron man ","greaate and good","chakuuu ", "indean") 
#-------->Object<-----------------

#-------->Printing<-----------------
print(Iron_man.introduction())    
print(Iron_man.carrying_weapon())       
print(Iron_man.name) 
#-------->Printing<-----------------

         
    