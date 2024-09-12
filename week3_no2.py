import math

def line():
    print('-'*25)

if __name__ == '__main__':

    while True:

        weight = float(input("Please enter your weight (kg.) : "))
        if weight > 20:
            break

    print()
    while True:

        height = float(input("Please enter your height (cm.) : "))
        if height > 50:
            break

    print()
    line()
    bmi = weight / math.pow(height/100,2)
    print("weight\t = {:.2f} kg".format(weight))
    print("Height\t = {:.2f} kg".format(height))
    print("Your BMI = {:.2f} kg".format(bmi))
    line()





