import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def marvellouspredictor():
    #load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    
    print("value of independant variable X:" , X)
    print("value of Dependant Variable Y:",Y )
    
    sum_X = 0
    sum_Y = 0
    
    for i in range(len(X)):
        sum_X = sum_X + X[i]
        sum_Y = sum_Y + Y[i]
        
    mean_X = sum_X/len(X)
    mean_Y = sum_Y/len(Y)
    
    print("mean_X is :" , mean_X)
    print("mean_Y is :" , mean_Y)


def main():
    marvellouspredictor()



if __name__ == "__main__":
    main()