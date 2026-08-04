# list

list = [1,2,3,4,5,6,7,8]
lists = ['anubhav','agrawal','deepanshu',]

print(list[3])
print(len(lists))

print(list[-1])

#list Slicing
#  here actuly we cqan cut the list
lists_4 = ['anubhav','agrawal','deepanshu','kashish','abhinav']

print(lists_4[1:4])
#reverse
print(list[::-1])
print(lists[::-1])
print(lists_4[::-1])

#list are mutable 
# means we can replace the value present in the list

#list = [1,2,3,4,5,6,7,8]

list[2] = "apple"
print(list)  # [1, 2, 'apple', 4, 5, 6, 7, 8]

# looping consept for list

for item in list:
    print(item)
for item in lists:
    print(item)
for item in lists_4:
    print(item)


# list.insert(insex,item)
list.insert(3,34)


#append in list
list.append("ram")
print(list)

list.pop(2)
print(list)
list3 = [1,3,5,6,7,8,6,4,3]

#list comprihention

list_item = [x**2 for x in range(1,20) if x%3==0]

print(list_item)

##function in list comprihention 

list_fruits = ['apple','bananna','grapes','gavava']
length_list =[len(word) for word in list_fruits]
print(length_list)
#nested list comprihention
#pairin kr sakte hai yaha aishe 

pair = [[i,j] for i in list_fruits for j in length_list]
print(pair)





