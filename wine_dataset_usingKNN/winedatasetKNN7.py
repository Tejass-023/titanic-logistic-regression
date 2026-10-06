import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def marvellousClassifier(Datapath):

    border = "-" * 40


##############################################################################################




    # step 1 : Load dataset
    
    
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(Datapath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)
    
    
#######################################################################################################
   
   
   
    #step 2 : clean datase
    
    
    print(border)
    print("step 2 : clean the dataset")
    print(border)
    
    df.dropna(inplace = True)
    
    print(border)
    print("shape of dataset : " , df.shape)
    
    print("total rows : " , df.shape[0])
    print("total colums : " , df.shape[1])
 
 
 
    
################################################################################################################################# 
  
  
  
  
    #step 3 : sepratre the variables 
    
    
    print(border)
    print("step 3 : seprate independant and depenadt variable ")
    print(border)
    
    X = df.drop(columns = ['Class'])
    Y = df['Class']
    
    print("shape of X : " , X.shape)
    print("shape of Y : " , Y.shape)
    
    
    print(border)
    print("input columns : " , X.columns.tolist())
    print("output columns : class ")
    print(border)
    
 ###############################################################################################################################################
 
    #step 4 : split dataset for training and testing
    
    
       
    print(border)
    print("step 4 : split datset for training and testing ")
    print(border)
    
    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    
    
    print(border)
    print("details of testing and training data ")
    print("shape of X_train :", X_train.shape)
    print("shape of Y_train :", Y_train.shape)
    print("shape of X_test :" ,X_test.shape)
    print("shape of Y_test :" ,Y_test.shape)
    
    
##############################################################################################################################
   
   
    
    #step 5 : feature scaling 
    
    
    print(border)
    print("step 5 : feature scaaling")
    print(border)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    
    print("feature scaling done")
    print(border)
   
   
    
    
##################################################################################


    
    #step 6 : built the model
    
    print(border)
    print("step 6 : bulit the model ")
    print(border)
    
    model = KNeighborsClassifier(n_neighbors=5)
    
    print("classification model is created")
    
    model = model.fit(X_train_scaled,Y_train)




##############################################################################################################




    #step 7 : train the model
    
    print(border)
    print("step 7 : train the model ")
    print(border)
    
    print("model training completed")
    print(border)
    
    

def main():
    
    marvellousClassifier("C:/Users/tejas/Desktop/machine laearning/wine_dataset/WinePredictor.csv")


if __name__ == "__main__":
    main()