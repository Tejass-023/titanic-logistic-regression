from sklearn.datasets import load_iris
def main():
    print("-"*30)
    print("iris classification case study ")
    print("-"*30)
    
    Dataset = load_iris()
    
    
    #MetaData of the Dataset
    print("independant variales are")
    print(Dataset.features_names)
    
    print("dependant variables")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()