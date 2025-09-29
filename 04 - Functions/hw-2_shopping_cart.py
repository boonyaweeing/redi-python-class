""""
# Shopping Cart Calculator

## Problem
You're building a shopping cart calculator for an online store. The program needs to:

1. Calculate the subtotal of items
2. Apply discounts based on different rules
3. Calculate tax
4. Add shipping costs
5. Display a formatted receipt

## Requirements
Without functions, this would involve repeating calculations and formatting code. Your task is to create functions that:

1. Eliminate repetitive calculations
2. Make the main program logic clear and easy to follow
3. Handle the price calculations step by step

## Expected Behavior
The program should allow users to add items to their cart, then display a detailed receipt with:
- Item list with prices
- Subtotal
- Discount applied (if any)
- Tax amount
- Shipping cost
- Final total

## Sample Run
```
Shopping Cart Calculator
========================

Enter item name (or 'checkout' to finish): Laptop
Enter price: 899.99

Enter item name (or 'checkout' to finish): Mouse
Enter price: 25.50

Enter item name (or 'checkout' to finish): Keyboard
Enter price: 75.00

Enter item name (or 'checkout' to finish): checkout

RECEIPT
=======
Laptop                           $899.99
Mouse                            $25.50
Keyboard                         $75.00
                               --------
Subtotal:                      $1000.49
Discount (10% for $1000+):      -$100.05
Tax (8.5%):                      $76.54
Shipping:                        $9.99
                               --------
TOTAL:                          $986.97
```

## Hints
Think about functions for:
- Calculating subtotals
- Determining and applying discounts
- Calculating tax
- Calculating shipping
- Formatting currency
- Printing receipt sections
"""

shopping_list = []

def cal_subtotal(list):
    subtotal = 0
    for item in list: 
        subtotal += item["item_price"]
    return subtotal

def cal_discount(discount, minimum, subtotal):
    if subtotal  > minimum:
        return subtotal * discount / 100
    else:
        return 0.00
    
def cal_tax(amount):
    return amount * 0.085

def cal_total(subtotal, discount, tax, shipping):
    total = subtotal - discount - tax + shipping
    return total

item = input("Enter item name (or 'checkout' to finish): ")
while item.lower() != "checkout":
    price = float(input("Enter price: "))
    shopping_list.append(dict(item_name = item, item_price = price))

    print()
    item = input("Enter item name (or 'checkout' to finish): ")

print("RECEIPT")
print("=======")
for thing in shopping_list:
    print(f"{thing['item_name'].upper()}                    ${thing['item_price']:.2f}")


print("                                           ----------")
subtotal = cal_subtotal(shopping_list)
discount = cal_discount(10, 1000, subtotal)
tax = cal_tax(subtotal-discount)
shipping = 9.99
total = cal_total(subtotal, discount, tax, shipping)
print(f"SUBTOTAL:                                   ${subtotal:.2f}")
print(f"DISCOUNT (10% for $1000+):                  -${discount:.2f}")
print(f"TAX (8.5%):                                 ${tax:.2f}")
print(f"SHIPPING:                                   ${shipping:.2f}")
print("                                           ----------")
print(f"TOTAL:                                      ${total:.2f}")