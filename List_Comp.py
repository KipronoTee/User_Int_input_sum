#nums = [4, -11, 69, 53, -69]
#doubled = []
#for num in nums:
    #doubled.append(num * -2)
#print(doubled)

nums = [4, -11, 69, 53, -69]
doubled = [num * -2 for num in nums]
print(doubled)