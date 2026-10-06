import pandas as pd
import joblib

def loadModel(filename):
    model = joblib.load(filename)
    print("model loaded successfully ")
    print(model.features_name_in_)
    
    return model


def predictpassenger(model):
    print("enter the information :")
    Pclass = int(input("Enter pclass (1/2/3)" ))
    sex = int(input("enter sex : (0 - M / 1 : F)"))
    Age = int(input("enetr the age : "))
    siblib = int(input("entyer the siblib"))
    parch = int(input("enter the parch : "))
    Fare = int(input("enetr the fare :"))
    Embarked = int(input ("enetr the embarked : (0/1/2)"))
    
    passenger = pd.DataFrame([
        "Pclass" :Pclass,
        "sex : " :Sex,
        "age"    :Age,
        "siblib" :siblib,
        "parch"  :parch,
        "fare"   :fare,
        "Emabarked_2.0" : 1 if model == 2 then class 0 ,
        "Emabarked_2.0" : 1 if model == 2 then class 0 ,
     ])
    
    passenger = passenger[model.feature_names_in_]
    result = model.predict(passenger)
    print(result)
def main():
    model = loadModel("MarvellousTitanic.pkl")
    
if __name__ == "__main__":
    main()