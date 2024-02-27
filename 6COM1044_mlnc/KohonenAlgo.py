import numpy as np

def kohonen_algorithm(data, num_neurons, learning_rate, num_epochs):
    # Initialize the weight matrix
    num_features = data.shape[1]
    weights = np.random.rand(num_neurons, num_features)
    
    # Training loop
    for epoch in range(num_epochs):
        for sample in data:
            # Find the winning neuron
            distances = np.linalg.norm(sample - weights, axis=1)
            winner = np.argmin(distances)
            
            # Update the weights of the winning neuron and its neighbors
            for i in range(num_neurons):
                neighborhood = np.exp(-np.abs(i - winner))
                weights[i] += learning_rate * neighborhood * (sample - weights[i])
    
    return weights

# Example usage
data = np.array([[0.2, 0.4], [0.6, 0.8], [0.3, 0.7], [0.1, 0.9]])
num_neurons = 2
learning_rate = 0.1
num_epochs = 10000

weights = kohonen_algorithm(data, num_neurons, learning_rate, num_epochs)
print(weights)