
if __name__ == '__main__':

    print("# Non Primitive : list ..\n")

    '''
    list คล้ายๆกับ array ต่างกันตรงที่ สามารถเก็บได้หลากหลายข้อมูลต่างชนิดตัวแปรกันได้
    การเข้าข้อมูลภายใน list จะเข้าถึงผ่าน Index ..
    '''


    # ------------------------------------------------------------------------------------


    '''
    # Assignment  "list"  สามารถเก็บข้อมูลรวมได้ หลายชนิด หลายค่า ในตัวแปรเดียว
    l = []
    l = [5,"olo",True,'H',0.1," ",-10,False]
    print(l)

    n = [1,5,8,3,4]
    print(n)

    m = ["Rushmi",'R','u','s','h','m','i']
    print(m)
    '''


    # ------------------------------------------------------------------------------------


    '''
    # Assignment  การกำหนดค่าและเรียงลำดับข้อมูลตัวเลข

    num = []
    odd = []
    even = []
    while True:
         i = int(input("รับค่าตัวเลข : "))
         if i == 0:
            break

         num.append(i)

    print("ค่าเริ่มต้น -> ", num)

    num.sort()   
    print("จากน้อยไปมาก -> ", num)
    
    num.reverse()
    print("จากมากไปน้อย -> ", num)   
    '''


    # ------------------------------------------------------------------------------------


    '''
    # Assignment  การหาค่ายกกำลัง
    number = [1,2,3,4,5,6,7,8,9]
    print(number)

    # แบบที่ 1 ..
    for i in range(len(number)):
        number[i] = number[i]**2
    print(number)

    # แบบที่ 2 ..
    number = [ i*i for i in number ]
    print(number)
    '''


    # ------------------------------------------------------------------------------------


    '''
    # Assignment  จับคู่คำ

    world = ["ดีว่ะ", "หมา", "หน้า", "หัวควย", "ติดหี", "ยดยา", "หิวยำ"]
    name = ["ดวง", "ก๊อบ", "ชาติ", "มิกกี้", "ไอ้โอ"]
    result = []

    # แบบที่ 1 ..
    for i in world:
        for x in name:
            result.append(x+i)
    print(result)

    # แบบที่ 2 ..
    result = [ x+i for i in world for x in name]
    print(result)
    '''


    # ------------------------------------------------------------------------------------


    '''
    # Assignment  จับคู่สินค้าและราคา

    Nomimono = ["kouhii", "Ocha", "Orenchijussu"]
    Ikura = [20, 50, 30]
    kotaete = []

    for n,i in zip(Nomimono,Ikura):
        print("สินค้า : ",n," ราคา ",i)
    '''
    

    # ------------------------------------------------------------------------------------


    '''
    # การค้นหาและการนับจำนวนในสมาชิก

    meiru = ["acdc", "cda", "62010dc", "acadc"]
    kotaete = []

    # แบบที่ 1 ..
    for mono in meiru:
        kotaete.append(mono.count("c")) 
    print(kotaete)
    
    # แบบที่ 2 ..
    kotaete = [ mono.count("c") for mono in meiru ]
    print(kotaete)
    '''


    # ------------------------------------------------------------------------------------