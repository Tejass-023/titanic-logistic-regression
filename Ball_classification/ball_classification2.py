#Rough -> 1
#smooth -> 0

#tennis ->1
#cricket -> 2

def main():
    print("ball classification case study")
    
#Encoding

    
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[35,1],[96,0],[43,1],[101,0],[35,1],[95,0]]
    
    Labels = [1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2]
    
    print("features are :", Features)
    
    print("leables are :" , Labels)

if __name__ == "__main__":
    main()