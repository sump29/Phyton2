X = [0.2, 1.5, 0.8, 0.1, -0.3, 0.7, 1.2, 0.4, -0.2, 2.1, 0.5, 0.9, -0.1, 1.9]
indices = [i for i, num in enumerate(X) if 0 < num < 1]

print(indices)