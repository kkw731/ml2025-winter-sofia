import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.points = np.array([]).reshape(0, 2)  # Initialize an empty (N,2) NumPy array

    def add_point(self, x, y):
        new_point = np.array([[x, y]])
        self.points = np.vstack((self.points, new_point))  # Append new point

    def predict(self, X_query):
        if self.points.shape[0] < self.k:
            return "Error: k cannot be greater than the number of available points (N)."

        # Compute Euclidean distances
        distances = np.abs(self.points[:, 0] - X_query)  # Since it's 1D, abs(x_i - X)
        sorted_indices = np.argsort(distances)  # Sort indices based on distance
        k_nearest = self.points[sorted_indices[:self.k]]  # Select k nearest points

        # Compute predicted Y as the mean of Y values of k nearest neighbors
        predicted_Y = np.mean(k_nearest[:, 1])
        return predicted_Y

def main():
    try:
        # Read N (number of points)
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        # Read k (number of neighbors)
        k = int(input("Enter the number of nearest neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")

        knn = KNNRegression(k)

        # Read N (x, y) points
        print(f"Enter {N} points (x, y) one by one:")
        for i in range(N):
            x, y = map(float, input(f"Point {i+1} (x y): ").split())
            knn.add_point(x, y)

        # Read X query point
        X_query = float(input("Enter the X value to predict Y: "))

        # Predict Y and display result
        result = knn.predict(X_query)
        print(f"Predicted Y: {result}" if isinstance(result, float) else result)

    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    main()