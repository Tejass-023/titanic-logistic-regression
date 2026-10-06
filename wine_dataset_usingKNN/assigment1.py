# ============================================================
# Assignment 3 - Deep Learning
# Forward Propagation and Backpropagation using TensorFlow/Keras
# Analyze the effect of Learning Rate and Number of Epochs
# Dataset: Wine Dataset
# ============================================================


# -------------------------------
# 1. Import Required Libraries
# -------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


# -------------------------------
# 2. Load Wine Dataset
# -------------------------------

wine = load_wine()

X = wine.data
y = wine.target

print("Dataset loaded successfully!")

print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of classes:", len(np.unique(y)))

print("\nFeature names:")
print(wine.feature_names)

print("\nTarget classes:")
print(wine.target_names)


# -------------------------------
# 3. Split Dataset
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# -------------------------------
# 4. Feature Scaling
# -------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nData scaling completed.")


# ============================================================
# Function to Create Neural Network
# ============================================================

def create_model(learning_rate):

    model = tf.keras.Sequential([
        
        # Input + Hidden Layer 1
        tf.keras.layers.Dense(
            16,
            activation='relu',
            input_shape=(13,)
        ),

        # Hidden Layer 2
        tf.keras.layers.Dense(
            8,
            activation='relu'
        ),

        # Output Layer
        # Wine dataset has 3 classes
        tf.keras.layers.Dense(
            3,
            activation='softmax'
        )
    ])

    # Optimizer
    optimizer = tf.keras.optimizers.Adam(
        learning_rate=learning_rate
    )

    # Compile model
    model.compile(
        optimizer=optimizer,
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


# ============================================================
# Experiment 1
# Effect of Learning Rate
# ============================================================

learning_rates = [0.001, 0.01, 0.1]

learning_rate_results = []

print("\n======================================")
print("EXPERIMENT 1: LEARNING RATE")
print("======================================")


for lr in learning_rates:

    print("\n--------------------------------------")
    print("Training with Learning Rate:", lr)
    print("--------------------------------------")

    # Create a new model
    model = create_model(lr)

    # Train model
    history = model.fit(
        X_train,
        y_train,
        epochs=30,
        batch_size=16,
        validation_split=0.2,
        verbose=0
    )

    # Evaluate model
    test_loss, test_accuracy = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    learning_rate_results.append(test_accuracy)

    print("Test Loss:", round(test_loss, 4))
    print("Test Accuracy:", round(test_accuracy * 100, 2), "%")


# -------------------------------
# Display Learning Rate Results
# -------------------------------

print("\n\nLearning Rate Results")
print("======================")

for lr, accuracy in zip(
    learning_rates,
    learning_rate_results
):

    print(
        "Learning Rate:",
        lr,
        " | Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


# -------------------------------
# Plot Learning Rate Results
# -------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    learning_rates,
    learning_rate_results,
    marker='o'
)

plt.xlabel("Learning Rate")
plt.ylabel("Test Accuracy")
plt.title("Effect of Learning Rate on Model Performance")

plt.grid(True)

plt.show()


# ============================================================
# Experiment 2
# Effect of Number of Epochs
# ============================================================

epochs_list = [5, 10, 20, 50]

epoch_results = []

print("\n======================================")
print("EXPERIMENT 2: NUMBER OF EPOCHS")
print("======================================")


for epochs in epochs_list:

    print("\n--------------------------------------")
    print("Training with Epochs:", epochs)
    print("--------------------------------------")

    # Use a fixed learning rate
    model = create_model(0.01)

    # Train model
    history = model.fit(
        X_train,
        y_train,
        epochs=epochs,
        batch_size=16,
        validation_split=0.2,
        verbose=0
    )

    # Evaluate
    test_loss, test_accuracy = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    epoch_results.append(test_accuracy)

    print("Test Loss:", round(test_loss, 4))
    print("Test Accuracy:", round(test_accuracy * 100, 2), "%")


# -------------------------------
# Display Epoch Results
# -------------------------------

print("\n\nEpoch Results")
print("======================")

for epochs, accuracy in zip(
    epochs_list,
    epoch_results
):

    print(
        "Epochs:",
        epochs,
        " | Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )


# -------------------------------
# Plot Epoch Results
# -------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    epochs_list,
    epoch_results,
    marker='o'
)

plt.xlabel("Number of Epochs")
plt.ylabel("Test Accuracy")
plt.title("Effect of Number of Epochs on Model Performance")

plt.grid(True)

plt.show()


# ============================================================
# Final Model
# ============================================================

print("\n======================================")
print("FINAL MODEL")
print("======================================")


final_model = create_model(0.01)

history = final_model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)


# -------------------------------
# Final Evaluation
# -------------------------------

test_loss, test_accuracy = final_model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nFinal Test Loss:", round(test_loss, 4))

print(
    "Final Test Accuracy:",
    round(test_accuracy * 100, 2),
    "%"
)


# ============================================================
# Predictions
# ============================================================

y_pred_probability = final_model.predict(
    X_test,
    verbose=0
)

y_pred = np.argmax(
    y_pred_probability,
    axis=1
)


# -------------------------------
# Classification Report
# -------------------------------

print("\n======================================")
print("CLASSIFICATION REPORT")
print("======================================")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=wine.target_names
    )
)


# ============================================================
# Training and Validation Accuracy Graph
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history['accuracy'],
    label='Training Accuracy'
)

plt.plot(
    history.history['val_accuracy'],
    label='Validation Accuracy'
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.title("Training vs Validation Accuracy")

plt.legend()

plt.grid(True)

plt.show()


# ============================================================
# Training and Validation Loss Graph
# ============================================================

plt.figure(figsize=(8, 5))

plt.plot(
    history.history['loss'],
    label='Training Loss'
)

plt.plot(
    history.history['val_loss'],
    label='Validation Loss'
)

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.title("Training vs Validation Loss")

plt.legend()

plt.grid(True)

plt.show()


print("\n======================================")
print("PROGRAM COMPLETED SUCCESSFULLY!")
print("======================================")