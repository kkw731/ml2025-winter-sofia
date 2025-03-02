import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Step 1: Get the number of data points (N)
    N = int(input("Enter the number of data points (N): "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Step 2: Get the value of k
    k = int(input("Enter the value of k (number of neighbors): "))
    if k <= 0:
        print("Error: k must be a positive integer.")
        return

    # Step 3: Initialize data storage using NumPy
    X_data = np.empty((N, 1))  # Feature (X) values
    Y_data = np.empty(N)       # Labels (Y) values

    # Step 4: Read N data points
    print("Enter the data points (x, y) one by one:")
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        X_data[i] = x
        Y_data[i] = y

    # Step 5: Compute variance of labels
    variance = np.var(Y_data)
    print(f"Variance of Y labels: {variance:.4f}")

    # Step 6: Get input X for regression prediction
    X_query = float(input("Enter the X value to predict Y: "))

    # Step 7: Validate k
    if k > N:
        print("Error: k cannot be greater than N.")
        return

    # Step 8: Perform k-NN Regression using Scikit-learn
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_data, Y_data)  # Train the model

    # Step 9: Predict and output the result
    Y_pred = model.predict(np.array([[X_query]]))
    print(f"Predicted Y value for X = {X_query}: {Y_pred[0]:.4f}")

if __name__ == "__main__":
    main()
