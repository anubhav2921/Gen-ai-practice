#---> filter function with lembda <------

numbers = [10, 15, 20, 25, 30]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))

# filter() kya karta hai?
# filter() kisi list/collection me se sirf woh values 
# rakhta hai jo condition satisfy karti hain.


#------> without lembda <-------

numbers = [10, 15, 20, 25, 30]
def check_even(x):
    return x % 2 == 0
result = filter(check_even, numbers)
             #Condition , Collection
print(list(result))