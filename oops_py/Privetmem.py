class Avenger:
    def __init__(self,name,phoneno):
        self.name = name
        self.__phoneno = phoneno

avenger = Avenger("captain", "8052828893")
print(dir(avenger))
print(avenger.name)
print(avenger.get__phoneno)  #AttributeError: 'Avenger' object has no attribute '__phoneno'

#geeter mathod ---> help to acs the privet data

