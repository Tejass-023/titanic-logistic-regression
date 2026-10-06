from sklearn.datasets import load_iris
def main():
    print("-"*30)
    print("iris classification case study ")
    print("-"*30)
    
    Dataset = load_iris()
    
    for i in range(len(Dataset.target)):
        print("ID %d , features %s , label %s" %(i,Dataset.data[i],Dataset.target[i]))
    
    

if __name__ == "__main__":
    main()