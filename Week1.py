

if __name__ == "__main__":

    # 1
    p_price = float(input("Enter product price \t: "))
    p_quantity = float(input("Enter product quantity  : "))
    print("----------------------------------")
    print("Total Price \t = {:13.2f}".format(p_price * p_quantity))
    vat = (p_price * p_quantity) * (7/100)
    print("VAT (7%) \t = {:13.2f}".format(vat))
    print("Net Prince \t = {:13.2f}".format(p_price + vat))
    print("----------------------------------")


    #----------------------------------------------------------------------------------------------


    # 2
    adults = int(input("Enter the number of adults \t: "))
    children = int(input("Enter the number of children \t: "))
    print("------------------------------------------")
    p_adults = 399 * adults
    p_children = 200 * children
    p_total = p_adults + p_children
    vat = p_total * (7 / 100)
    print("Total Price \t\t = {:8.2f}".format(p_total) + " Baht")
    print("VAT (7%) \t\t = {:8.2f}".format(vat) + " Baht")
    print("Net Prince \t\t = {:8.2f}".format(p_total + vat) + " Baht")
    print("------------------------------------------")


    # ----------------------------------------------------------------------------------------------


    # 3
    kg = float(input("Enter your weight (kg) : "))
    cm = float(input("Enter your height (cm) : "))
    print("----------------------------------")
    bmi = kg / ((cm/100) * (cm/100))
    print("Your BMI : {:.2f} ".format(bmi))
    print("----------------------------------")


    # ----------------------------------------------------------------------------------------------


    # 4
    p_product = float(input("Enter product price of the product \t : "))
    p_number = float(input("Enter the number product \t\t : "))
    p_amount = int(input("Amount recieved (Baht) \t\t\t : "))
    print("*******************************************************")
    x = p_product * p_number
    y = x * (7/100)
    z = x - y
    k = p_amount - z
    print("sub Total \t = {:30.2f}".format(x))
    print("VAT (%7) \t = {:30.2f}".format(y))
    print("Net Total \t = {:30.2f}".format(z))
    print("*******************************************************")
    print("Recieved \t = {:30.2f}".format(p_amount))
    print("Change \t\t3 = {:30.2f}".format(k))


    # ----------------------------------------------------------------------------------------------


    # 5
    salary = int(input("กรอกข้อมูลเงินเดือน : "))
    # print('*'*41)
    print("*****************************************")
    x = salary * (7 / 100)
    y = salary * (3 / 100)
    z = salary - (x + y)
    print("Salary   = {:20.2f}".format(salary))
    print("VAT \t = {:20.2f}".format(x))
    print("social3  = {:20.2f}".format(y))
    print("Income \t = {:20.2f}".format(z))
    print("*****************************************")