class Person: 
    def __init__(self,name,address,number): 
        self.__name = name 
        self.__address = address
        self.__number = number

def print_person(person):
    print(
class Customer(Person): 
    def __init__(self,name,address,number,cust_number,wish_mail_list): 
        Person.__init__(self,name,address,number)
        self.__cust_number = cust_number
        self.__wish_mail_list = wish_mail_list


