import numpy as np
import math

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)


def marvellousKNNclassifer():
    border = "-"*30
    
    Data = [
        {'point' : 'A','X' : 1 , 'Y' : 2, 'Label' : 'Red'},
        {'point' : 'B','X' : 2 , 'Y' : 3, 'Label' : 'Red'},
        {'point' : 'C','X' : 3 , 'Y' : 1, 'Label' : 'Blue'},
        {'point' : 'D','X' : 5 , 'Y' : 6, 'Label' : 'Blue'}
    ]
    
    print(border)
    print("marvellous KNN classifer ")
    print(border)
    
    for i in Data:
        
       print(Data)
     
    print(border)
    
    
    
    new_point = {'X' : 3 , 'Y' : 3}

    result = MarvellousEucDistance(Data[0] , new_point)
    
    print("distance is : " , result)
    
def main():
    marvellousKNNclassifer()



if __name__ == "__main__":
    main()