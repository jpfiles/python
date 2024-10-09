def computepay(hrs, rt):
    try:
        if hrs > 40:
            reg_pay = 40 * rt
            ot_hrs = hrs - 40
            ot_pay = ot_hrs * (rt * 1.5)
            total_pay = reg_pay + ot_pay
        else:
            total_pay = hrs * rt
        return f"Your paycheck is ${total_pay:.2f}!"
    except:
        return "Please enter valid numbers."
 
hrs = float(input("Enter hours: "))
rt = float(input("Enter rate: "))
 
print(computepay(hrs, rt))