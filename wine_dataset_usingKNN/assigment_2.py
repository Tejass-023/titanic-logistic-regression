import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def marvellousClassifier(Datapath):

    border = "-" * 40

    # ============================================================
    # STEP 1 : LOAD DATASET
    # ============================================================

    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(Datapath)

    print("Some entries from dataset")
    print(df.head())
    print(border)


    # ============================================================
    # STEP 2 : CLEAN DATASET
    # ============================================================

    print(border)
    print("Step 2 : Clean the dataset")
    print(border)

    df.dropna(inplace=True)

    print("Shape of dataset :", df.shape)
    print("Total rows :", df.shape[0])
    print("Total columns :", df.shape[1])
    print(border)


    # ============================================================
    # STEP 3 : SEPARATE INDEPENDENT AND DEPENDENT VARIABLES
    # ============================================================

    print(border)
    print("Step 3 : Separate independent and dependent variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print("Input columns :", X.columns.tolist())
    print("Output column : Class")
    print(border)


    # ============================================================
    # STEP 4 : SPLIT DATASET
    # ============================================================

    print(border)
    print("Step 4 : Split dataset for training and testing")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Details of training and testing data")

    print("Shape of X_train :", X_train.shape)
    print("Shape of Y_train :", Y_train.shape)
    print("Shape of X_test  :", X_test.shape)
    print("Shape of Y_test  :", Y_test.shape)

    print(border)


    # ============================================================
    # STEP 5 : FEATURE SCALING
    # ============================================================

    print(border)
    print("Step 5 : Feature scaling")
    print(border)

    scaler = StandardScaler()

    # Learn scaling parameters only from training data
    X_train_scaled = scaler.fit_transform(X_train)

    # Apply the same scaling to test data
    X_test_scaled = scaler.transform(X_test)

    print("Feature scaling completed")
    print(border)


    # ============================================================
    # STEP 6 : BUILD MLP MODEL
    # ============================================================

    print(border)
    print("Step 6 : Build the MLP model")
    print(border)

    model = MLPClassifier(
        hidden_layer_sizes=(10, 10),
        activation='relu',
        solver='adam',
        max_iter=1000,
        random_state=42
    )

    print("MLP classification model is created")
    print(border)




    # ============================================================
    
    
    # STEP 7 : TRAIN THE MODEL
    
    
    # ============================================================

    print(border)
    print("Step 7 : Train the model")
    print(border)

    model.fit(X_train_scaled, Y_train)

    print("Model training completed")
    print(border)


    # ============================================================
    # STEP 8 : TEST THE MODEL
    # ============================================================

    print(border)
    print("Step 8 : Test the model")
    print(border)

    # Predict using TEST data
    Y_pred = model.predict(X_test_scaled)

    print("Predicted values :", Y_pred)
    print("Actual values    :", Y_test.values)

    print(border)


    # ============================================================
    # STEP 9 : CALCULATE ACCURACY
    # ============================================================

    print(border)
    print("Step 9 : Calculate accuracy")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy :", accuracy)
    print("Accuracy percentage :", accuracy * 100, "%")

    print(border)


    # ============================================================
    # STEP 10 : CONFUSION MATRIX
    # ============================================================

    print(border)
    print("Step 10 : Confusion Matrix")
    print(border)

    cm = confusion_matrix(Y_test, Y_pred)

    print("Confusion Matrix :")
    print(cm)

    print(border)


    # ============================================================
    # STEP 11 : DISPLAY CONFUSION MATRIX
    # ============================================================

    plt.imshow(cm, interpolation='nearest')
    plt.title("MLP Confusion Matrix")
    plt.colorbar()

    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")

    plt.xticks(range(len(sorted(Y.unique()))), sorted(Y.unique()))
    plt.yticks(range(len(sorted(Y.unique()))), sorted(Y.unique()))

    # Display values inside matrix
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j],
                     horizontalalignment="center")

    plt.show()


# ================================================================
# MAIN FUNCTION
# ================================================================

def main():

    marvellousClassifier(
        r"C:/Users/tejas/Desktop/machine laearning/wine_dataset_usingKNN/WinePredictor.csv"
    )


if __name__ == "__main__":
    main()