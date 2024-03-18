bill = 1900
discount = 150

if bill >= 2000:
    print ("bill is greater than 2000")
    final_bill = bill - discount
    
else:
    print("bill is less than 2000")
    final_bill = bill

print("final bill: " + str(final_bill))

## Alternative code 
bill = 2500
discount = 150

final_bill = bill - discount if bill >= 2000 else bill  # Ternary operator

print("Bill is", "greater than or equal to 2000" if bill >= 2000 else "less than 2000")
print("Final bill:", final_bill)

