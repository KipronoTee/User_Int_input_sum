# Local scope refers to a variable declared inside a function.
# in the example below, the variable total is only avilable to the code within the get-total fucntion
#def add_nums(a, b):
    #answer = a +b
    ##return answer
#print(add_nums(2, 13))

# Enclosing scope refers to a fcuntion inside another fucntion (or a nested fucntion)
# In the  example below, double is a  nested fucntion inside add_nums
# An enclosing function may not have affect on the code

#def add_nums(a, b):
    #answer = a + b
    #def double_it():
        #double = answer * 2
        #print(double)
    #double_it
    #return answer
#print(add_nums(2, 13))

# global scope is when a variable is declared outside of a function, meaning it can be accessed from anywhere.
# in the example bewlo, global var is a global variable which can be accessed both within the add_nums and double_it fucntions

global_var = 13

def add_num(a, b):
    #enclosed scope variable inside a function
    total = a + b
    print("global_var in outter fucntion: ", global_var)
    def double_it():
        double = total * 2
        print("global_var in inner function: ", global_var)
    double_it()
    return total
add_num(13,5)