from sklearn import tree

def main():
    print("ball classification case study")
    

    
    Independant = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[35,1],[96,0],[43,1],[101,0]]
    #Testing = [35,1],[95,0]
    
    
    Dependant = [1,1,2,1,2,1,2,1,1,1,1,2,1,2]
    #testing = [1,2]
    
    print("Independant variables are :", Independant)
    
    print(" Dependant Variables are :" , Dependant)
    
    model = tree.DecitionTreeClassifier()
    
    model = model.fit(Independant,Dependant)
    
    result = model.predict([[35,1],[95,0]])
    
    print("pridected result of model is :" , result)

if __name__ == "__main__":
    main()