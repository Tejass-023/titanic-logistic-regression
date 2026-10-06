import pandas as pd

def main():
    
    
    sobj = pd.Series([27000,32000,35000],index = ["amit","sagar","sagar"])
    
    print(sobj) 
    
    print(sobj["sagar"])
    
if __name__ == "__main__":
    main()