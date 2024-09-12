
def line():
    print('-'*30)

def cal(x, y):
    ratio = x * (y /100)
    print(" |> เป็นจำนวน {:.8f}".format(ratio))

def ratio(x, y):
    p = (x /y)*100
    print(" |> เป็นสัดส่วน {:.2f}".format(p))

if __name__ == '__main__':

   while True:
    select = input(" |> เลือกการคำนวน : ")
    line()

    if select == 'C' or select == 'c':
        cost = float(input(" |> เงินทั้งหมด : "))
        per = int(input(" |> สัดส่วน : "))
        cal(cost, per)
        print(" |> สัดส่วน {}%".format(per))
        cal(cost, per)
        line()

    if select == 'p' or select == 'P':
        per = float(input(" |> จำนวนเงินที่ต้องการรู้ สัดส่วน : "))
        cost = float(input(" |> เงินทั้งหมด : "))
        ratio(cost, per)
        print(" |> มีสัดส่วนเป๋น {}".format(per))
        line()

    if select == 'n' or select == 'N':
        print()
        print("\t<Exit. while-loop>")
        print()
        line()
        break
