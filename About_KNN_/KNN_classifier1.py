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
    
    new_point = np.array([[3,3]])
    
    #model creation 
    model = KNeighborsClassifier(n_neighbors=3)
    
    model = model.fit(X,Y)
    
    Ypred = model.predict(new_point)
    
    print("predicted label :", Ypred)


if __name__ == "__main__":
    main()