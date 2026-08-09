#----> lambda function are one liner function

#---> using normal function

def square(num):
    return num**2

no = int(input("Enter no. = "))
output=square(no)
print(f"the square of {no} is {output}")



#---> by using lambda function

lambda_function = lambda x:x**2

no = int(input("Enter no. = "))
output=lambda_function(no)
print(f"the square of {no} is {output}")
