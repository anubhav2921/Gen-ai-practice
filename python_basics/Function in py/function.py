#function padh rahe hai yaha 

def translater(English_text):
    """This function use for translate the english to hindi"""
    if English_text == "hello" or English_text=="Hello":
        print(f"the translater for {English_text} is Namaste")

    if English_text == "help" or English_text=="Help":
        print(f"the translater for {English_text} is Sahayta")


#Function calling is just like to calll the vater for food
#  itme in fuction we do function call()   

input_en = input("Enter your english word  ")  
translater(input_en)
