#recursive funcotion 

#FActorial of 8 ---> 8*7*6*5*4*3*2*1

#---------> nonrecursive mathod
# |
# |

# def factorial(num):
#     if num==0 or num == 1:
#         print(f"the factorial of {num} is : 1")
    
#     else:
#          factorial = 1
#          for i in range(1,num + 1):
#             factorial = factorial*i
#          print(f"the factorial of {num} is = {factorial}")  

# number = input("Enter the number")
# factorial(number)

# |
# |
# |

#---------------> recursive mathod <--------------
# |
# |
# |
# def factorial_recu(num):
#     if num==0 or num == 1:
#         return 1
    
#     else:
#          return num* factorial_recu(num-1) #->Base condition 

# number= int(input("Enter number = "))       

# print(factorial_recu(number))
# # |
# |
# |

#----> function to add multipul no 

def addition(*num):     #*num can take sireas of parameter
    add =0
    for i in num:
        add+=i
    print("The addition for th numbers are", add) 



addition(1,2,3,4,5,6,7,8,8)


