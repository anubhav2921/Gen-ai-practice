# Dictionarie in python 
#dictionarie is key value pair

dictionarie = {
    'name':'amit','phone': 8052828893,
    'name':'Anubhav','phone':12334

}
print(dictionarie['name'])
print(dictionarie['phone'])

#delet in dictionary
del dictionarie['phone']
print(dictionarie)


#insertion is possible


#Mathods in dictionary

dictionaryy={
 "Name":"Anubhav","class":"btech","section":"B","list":[1,2,3,4,5,5],
 "key_1":23,"key_2":45

}
print(dictionaryy)
print(dictionaryy.keys())   #dict_keys(['NAme', 'class', 'section', 'list', 'key_1', 'key_2'])

print(dictionaryy.values())   #dict_values(['Anubhav', 'btech', 'B', [1, 2, 3, 4, 5, 5], 23,45])

print(dictionaryy.items()) #dict_items([('Name', 'Anubhav'), ('class', 'btech'), ('section', 'B'), ('list', [1, 2, 3, 4, 5, 5]), ('key_1', 23), ('key_2', 45)])

print(dictionaryy.get("Name"))  #Anubhav

#nested dic ---> i want to store the information of multiple students

nested_dic = { "Student_1":{"Name":"Anuhav","sec":"B"},
              "Student_2":{"Name":"deepanshu","Sec":"B"},
              "Student_3":{"Name":"Anuhav","sec":"B"}

}
print(nested_dic)
print(nested_dic.values())
print(nested_dic.keys())

#itaration in these 
for outer_key,outer_value in nested_dic.items():
    print(f"outer key is:{outer_key} and uter value is : {outer_value}")
    for key_11,value_1 in outer_value.items():
     print(f"Inerr key is:{key_11} and inner value is : {value_1}")

#mmearge dictionary
M_dic1 = {"a":1,"b":3,"c":4}
M_dic2 = {"d":6,"e":7,"f":8} 
mmearge_dictionary = {**M_dic1,**M_dic2}
print(mmearge_dictionary)

# Some  bultion function in our python dictionary
# sum()  , max(),  len() etc









