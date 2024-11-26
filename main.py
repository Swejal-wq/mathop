
from mathop.mulop import mulValue
from mathop.divop import divValue

if __name__ == '__main__':

     V1 = int(input('enter the  1st no '))
     V2 = int(input('enter the  2nd no '))
     op = input('Enter Operation:')

    if op.lower() ==  'mul' :

        m1 = mulValue(V1,V2)
        print(f'multiplication = {m1}')
    elif op.lower() == 'div':
        m2 = divValue(V1,V2)
         print('division', m2)
    else:
        print('please choose multilpication or division only ')


    