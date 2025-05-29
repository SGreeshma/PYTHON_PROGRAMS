def lemonadeChange(bills, five=0, ten=0):
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False, five, ten
        elif bill == 20:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False, five, ten
    return True, five, ten

# Keep track of ₹5 and ₹10 notes across multiple inputs
five, ten = 0, 0

while True:
    bills = list(map(int, input("Enter bills: ").split()))
    result, five, ten = lemonadeChange(bills, five, ten)
    print(result)
    if not result:  # Stop when False is returned
        break
