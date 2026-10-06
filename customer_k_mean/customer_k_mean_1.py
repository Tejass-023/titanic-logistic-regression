import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans




def main():
    #step 1 : load the data 
    df = pd.read_csv("C:/Users/tejas/Desktop/machine laearning/customer_k_mean/Mall_Customers (1).csv")
    print(df.head())
    
    print("missing values :")
    print(df.isnull().sum())
    
    #step 2 : fature selecction 
    
    X = df[["AnnualIncome","SpendingScore"]]
    print("selected features :")
    print(X.head())
     
    #step 3 : scale the data 
    scalar = StandardScaler()
    
    X_scaled = scalar.fit_transform(X)
    
    print("scaled data :")
    print(X_scaled[:5])
    
    #step 4 : elbow method
    
    WCSS = []
    for k in range (1,11):
        model = KMeans(
            n_clusters= k,
            random_state=42,
            n_init=10
        )
        
        model.fit(X_scaled)
        
        WCSS.append(model.inertia_)
        
    print("values of WCSS :")
    for i in range(len(WCSS)):
        print(f"{i + 1} : {WCSS[i]}")
        
        
    # step 5 : vizualisation
    
    plt.plot(range(1,11),WCSS,marker = "o")
    plt.xlabel("Number of clusters : K")
    plt.ylabel("WCSS")
    plt.title("Marvellous Elbow Mwthod ")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    #step 6 : final model 
    
    model = KMeans(
                n_clusters= 4,
                random_state=42,
                n_init=10
            )
            
    clusters = model.fit_predict(X_scaled)
    df["Cluster"] = clusters
    
    print("dataset with clusters : ")
    print(df.head(20))
            



if __name__ == "__main__":
    main()