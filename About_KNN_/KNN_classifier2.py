



#pandas pd works on dataframe simlarly numpay works using np.array


import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    #Independant 
    X = np.array(
        [
            [1,2],
            [2,3],
            [3,1],
            [5,6]
        ]
    )
    #Dependant Variable
    Y = np.array(["Red","Red","Blue","Blue"])
    
    
    
    print("Independant variables are :")
    print(X)
    
    print("Dependant variables are :")
    print(Y)
    
    

if __name__ == "__main__":
    main()