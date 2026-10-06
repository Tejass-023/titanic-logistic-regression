import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def marvellousClassifier(Datapath):

    border = "-" * 40

    # Load dataset
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(Datapath)

    print(border)
    print("Some entries from dataset")
    print(df.head())
    print(border)


def main():
    marvellousClassifier("C:/Users/tejas/Desktop/machine laearning/wine_dataset/WinePredictor.csv")


if __name__ == "__main__":
    main()