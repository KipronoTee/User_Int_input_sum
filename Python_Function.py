# Python function is a modular piece of code that can be used repeatedly.
# Generally a function is a block of code which is executed when it is called from somewhere in the program.
# A function has a return value
# fucntion can be without parameter for example: 

#def add_nums():
    #print(2 + 13)

# call the  fcuntion
#add_nums()

# A fucntion can conatin arguments/parameters which specified inside the parentheses, seperated with a comma in case of many arguments entered. 

# Arguments make fucntions more dynamic and reusable.  Example 

#=def add_nums(a, b, c):
    #answer = a + b + c
    #return answer

#=total = add_nums(2, 13, 1)
#=print("total: ", total)

# Args and Kwargs

# args also known as arbitrary arguments are used when number of  arguments to be entered are unknowne.
# In such case, add an * before the argument/parameter name in the function to make the list of parameters a tupple.
# Example 

#=def add_nums(*nums):
    #=sum = 0
    #=for num in nums:
        #=sum += num
    #=return sum
#=print("total:  ", add_nums(2, 5, 6, 7, 8, 13))

# adouble ** are added before the parameter if the keyword argument/parameter are to be passed in a function
# for example **age

def  add_ages(**age):
    sum = 0
    for k, v in age.items():
        sum += v
    return sum
print("Total: ", add_ages(Mutemi=23, skinny=22, ahmed=21))
