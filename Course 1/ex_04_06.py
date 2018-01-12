
def computepay():
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    if hours > 40:
        normal_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = normal_pay + overtime_pay
        return(total_pay)
    else:
        total_pay = hours * rate
        return(total_pay)

print("Pay",computepay())
