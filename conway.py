import numpy
import time
import os
#0 is dead 1 is alive
#make second board with new states
def init():
    a = numpy.empty((10, 10))
    a.fill(0)
    '''
    a[0][1] = 1
    a[0][2] = 1
    a[0][3] = 1
    a[1][3] = 1
    a[4][5] = 1
    a[5][6] = 1
    a[5][5] = 1
    '''
    #a[4][5] = 1
    '''
    a[5][4] = 1
    a[5][5] = 1
    a[5][6] = 1
    '''
    '''
    a[0][2] = 1
    a[1][0] = 1
    a[1][2] = 1
    a[2][1] = 1
    a[2][2] = 1
    a[8][0] = 1
    a[8][1] = 1
    a[8][2] = 1
    '''
    a[4][4] = 1
    a[4][5] = 1
    a[4][3] = 1
    a[3][4] = 1
    a[3][5] = 1
    a[3][3] = 1
    a[5][3] = 1
    a[5][4] = 1
    a[5][5] = 1
    return a
def numneighbors(grid,x_coord,y_coord):
    result = 0
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if 0 <= x < len(grid) and 0 <= y < len(grid):
            if grid[(x,y)] == 1:
                result += 1
    return result
def nextboard(array):
    b = numpy.empty((10, 10))
    b.fill(0)
    num = 0 
    for idx,x in numpy.ndenumerate(array):
        num = numneighbors(array,idx[0],idx[1])
        #print(idx,num)
        #print(array[idx])
        if (num == 2 or num == 3) and array[idx] == 1:
            #print("It lives")
            b[idx] = 1
        elif num == 3 and array[idx] == 0:
            #print("It lives")
            b[idx] = 1
        else:
            #print("dies")
            b[idx] = 0
    return b
def main():
    a = init()    
    print(a)
    print('\n')
    while True:
        time.sleep(1)
        newboard = nextboard(a)
        os.system('cls')
        print(newboard)
        print('\n')
        a = newboard
    #print(numneighbors(a,0,0))
if __name__ == '__main__':
    main()
