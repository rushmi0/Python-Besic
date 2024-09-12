import os
import binascii


bits = 256
print("Bytes = " + str(bits // 8))
#random = os.urandom(bits // 8)

random_bin = binascii.hexlify("c904225c0b35a456dc94531837c6470d5db9593532b3d16beb4a0df15e818a33")
random_hex = binascii.hexlify(random_bin)

bytes = len(random_bin)
print(bytes)


if __name__ == '__main__':

    '''
    Input = input("รับค่า : ")
    res = bytes(Input, 'utf-8')

    Encript = binascii.hexlify(res)

    print(len(Encript)," ",Encript)
    '''

    # ------------------------------------------------------------------------------------




