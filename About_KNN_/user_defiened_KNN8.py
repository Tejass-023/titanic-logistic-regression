import numpy as np
import math

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    
    return Ans


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
    
    print("Distances from all points is : ")
    print(border)
    
    new_point = {'X' : 3 , 'Y' : 3}
    
    for d in Data:
        d['distance'] = MarvellousEucDistance(d , new_point)
       
        
    for d in Data:
        print(d['distance'],d['Label'])
        
    sorted_data = sorted(Data,key = lambda item : item['distance'])
    print(border)
    print("sorted data : ")
    print(border)
    
    for d in sorted_data:
        print(d)
        
    k = 3
    
    nearest = sorted_data[:k]
    print(border)
    print("nearest k negibor:")
    print(border)
    
    for d in nearest:
        print(d)
        
    #voting
    
    votes = {}
    
    for neighors in nearest:
        Label = neighors['Label']
        votes[Label] = votes.get(Label,0) + 1
        
    print(border)
    print("voting score is :")
    print(border)
    
    for d in votes:
        print("Name : " , d , "number of votes :" , votes[d])
        
    print(border)

def main():
    marvellousKNNclassifer()



if __name__ == "__main__":
    main()