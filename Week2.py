
import math

def line():
    print("-" * 50)

#----------------------------------------------------------------------------------------------

def func(f):
    if function == 'c' or function == 'C':
        print("\n You choose \"Circle\"")
        radius = float(input("Input radius : "))
        x = math.pi * math.pow(radius, 2)
        print("\nThe circle area is {:.2f}".format(x))

    elif function == 's' or function == 'S':
        print("\n Your choose \"Square\"")
        width = float(input("Input width : "))
        length = float(input("Input length : "))
        SArea = width * length
        print("\nThe square area is {:.1f}".format(SArea))

    else:
        print('Don\'t have choice')

#----------------------------------------------------------------------------------------------

def cel(c):
    farenheit = (celsius * 9 / 5) + 32
    kevin = celsius + 273.15
    print("{:.2f} Celsius = ".format(celsius)
          + "{:.2f} Farenheit = ".format(farenheit)
          + "{:.2f} Kevin".format(kevin))

# ----------------------------------------------------------------------------------------------

def coupon_count(point):
    s = 0
    h = 0
    c = 0
    while point > 99:
        if point >= 1000:


        elif point >= 600:
            h += 1
            point = point  - 600

        elif point >= 600:
            h += 1
            point = point  - 100

    print("{} of SMOKYBIKE COUPON".format(s))
    print("{} of HAMBURGER COUPON".format(h))
    print("{} of CHOCO STICK COUPON".format(c))
    print("Point balance : {}".format(p))



if __name__ == "__main__":

   '''
    # Slide 75
    line()
    print("Press \"c/C\" : Find a circle area \n")
    print("Press \"s/S\" : Find a square area \n")
    line()
    function = input("input choice: ")
    func(function)
    line()
   '''

   '''
   # Slide 76
   celsius = float(input("input celsiun : "))
   cel(celsius)   
   '''

   # Silde 79
   p = int(input("Input your point : "))
   print("Your point: {} You can exchange....".format(p))
   coupon_count(p)
    # ----------------------------------------------------------------------------------------------









