class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c): # Python completely forgets the first 'add' method now!
        return a + b + c

calc = Calculator()
# print(calc.add(2, 3)) 