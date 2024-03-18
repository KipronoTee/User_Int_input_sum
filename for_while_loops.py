# names = ["Timothy", "Chebet", "Kiprono"]
#for name in names:
    #print(name)
    
#welcome_message = "welcome to PLP"
#for i in range(5):
    #print(welcome_message)

#count = 0
#while count <= 2:
    #loop body
    #print(count)
    #count += 1
# comments to deactive "for" loops and initiate code for 'while" loops
#colors = ["blue", "green", "white", "yellow", "black", "brown"]
#color_i_want = "white"
 
#found = False 
#for color in colors:
     #if color == color_i_want:
         #print("They have the  color  I want")
         #found = True
         #break
     
#if not found:
    #print(color_i_want, "not found in the list")

colors = ["blue", "green", "white", "yellow", "black", "brown"]
color_i_want = "white"
length = len(colors)
count = 0

while count < length:
    print(colors[count])
    if colors[count] == color_i_want:
        print("They have the color I want")
        break
    count += 1
    
