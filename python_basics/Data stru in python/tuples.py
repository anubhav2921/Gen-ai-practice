#tupal padhenge bhaiiiiii hahahahah
#see yeh immutable hota hai mtlab change nahi
#  kar sakta value kishiki 
#like = item = "apple"
#you can't do item = "banana"

# indexing hoti hai bhaii

a= tuple()
print(type(a))

tuple = (1,2,3,2,2,2,4,5,6,7)
print(tuple)


# tuple[1] = 43
#     ~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# tuple[1] = 43
# print(tuple)

print(tuple[::-1])
print(tuple.count(2))

#paking and un paking in tuple

a= 1,2,3,4,5,6,6,6,7,8,9,10

print(type(a))
print(a)
print(a.count(6))

#unpaking

A1,b,c,d,e = (1,2,3,4,6)

print(type(A1))  #<class 'int'>

#nested list padhoge yaha

nested = [[1,2,3,4,5],[2,3,4,5,6],[7,8,9,78]]
print(nested[2][3])

#tuples insides the list

nested_list = [(1,2,3,4,5),(2,3,4,5,6),(7,8,9,78)]

print(type(nested_list))

#tuple













