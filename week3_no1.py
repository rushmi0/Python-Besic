
def line():
    print('-'*30)

if __name__ == "__main__":

    get = int(input("ต้องรับตัวเลขกี่ครั้ง : "))
    line()
    group = []
    for i in range(get):
        get_in_loop = int(input("กรอกข้อมูลตัวเลขที่ {} : ".format(i+1)))
        group.append(get_in_loop)
    line()
    print("ตัวเลขมากที่สุดคือ : {}".format(max(group)))
    print("ตัวเลขน้อยที่สุดคือ : {}".format(min(group)))





