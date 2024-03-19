# Week 3 Assignment
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount

bill = int(input("Enter original price:"  ))
discount_rate = 20 #As a percentage
# calculate discounted amount
discount_amount = bill * discount_rate/100

#Check if dosucount is 20%
if discount_amount >= 0.2 * bill: 
    print("discount applied")
    final_bill = bill - discount_amount
else:
    print("discount is not applicable")
    final_bill = bill
print("final_bill:", final_bill)
    