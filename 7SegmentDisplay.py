import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

segmentA= board.get_pin('d:8:o')
segmentF= board.get_pin('d:10:o')
segmentB= board.get_pin('d:7:o')
segmentG= board.get_pin('d:12:o')
segmentE= board.get_pin('d:5:o')
segmentC= board.get_pin('d:3:o')
segmentD= board.get_pin('d:4:o')
segmentDP= board.get_pin('d:2:o')

pins = [segmentA,segmentF,segmentB,segmentG,segmentE,segmentC,segmentD,segmentDP]

n0 = [1,1,1,0,1,1,1,0]
n1 = [0,0,1,0,0,1,0,0]
n2 = [1,0,1,1,1,0,1,0]
n3 = [1,0,1,1,0,1,1,0]
n4 = [0,1,1,1,0,1,0,0]
n5 = [1,1,0,1,0,1,1,0]
n6 = [1,1,0,1,1,1,1,0]
n7 = [1,0,1,0,0,1,0,0]
n8 = [1,1,1,1,1,1,1,0]
n9 = [1,1,1,1,0,1,0,0]

numbers = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]

# COUNT
# for iNumber in range(10):
#     for iPin in range(8):
#         pins[iPin].write(numbers[iNumber][iPin])
#     time.sleep(1)

# USER DEFINED
index = int(input('Select a Number [0-9]: '))
n = numbers[index]
for iPin in range(8):
    pins[iPin].write(n[iPin])


