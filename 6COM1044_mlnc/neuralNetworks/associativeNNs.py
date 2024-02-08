"""
Associative Neural Networks (ANN)

Associative Neural Networks (ANN) are a type of artificial neural network that can learn associations 
between input patterns and corresponding output patterns. 

They are commonly used for tasks such as pattern recognition, classification, and prediction.

How ANN Works:
1. Data Preparation: Prepare the input-output pairs for training the ANN. Each input pattern is associated 
with a corresponding output pattern.

2. Network Architecture: Define the architecture of the ANN, including the number of input and output neurons, 
as well as the number and configuration of hidden layers.

3. Weight Initialization: Initialize the weights of the connections between neurons randomly or using specific 
techniques like Xavier or He initialization.

4. Forward Propagation: Pass the input pattern through the network to compute the output. This involves multiplying 
the input values with the corresponding weights, applying an activation function, and passing the result to the next layer.

5. Error Calculation: Compare the computed output with the expected output and calculate the error using a suitable 
loss function, such as mean squared error (MSE) or cross-entropy loss.

6. Backpropagation: Update the weights of the connections in the network to minimize the error. This is done by 
propagating the error backward through the network, adjusting the weights based on the error gradient and the learning rate.

7. Training: Repeat steps 4-6 for multiple iterations or epochs until the network learns the associations 
between input and output patterns.

8. Testing: Evaluate the performance of the trained ANN on unseen data to assess its accuracy and generalization capabilities.

***Note that a tensor is a multi-dimensional array similar to NumPy arrays, but with additional features such as
GPU acceleration and automatic differentiation for gradient-based optimization.

Example Code using PyTorch:
"""

import torch
import torch.nn as nn
import torch.optim as optim

# Define the ANN architecture
class ANN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ANN, self).__init__()  # Call the constructor of the parent class (nn.Module)
        self.fc1 = nn.Linear(input_size, hidden_size)  # Fully connected layer
        self.fc2 = nn.Linear(hidden_size, output_size)  # Fully connected layer
        self.activation = nn.ReLU()  # Activation function

    # Define the forward pass
    def forward(self, x):
        x = self.fc1(x)  # Forward pass through the first fully connected layer
        x = self.activation(x)  # Apply the activation function
        x = self.fc2(x)  # Forward pass through the second fully connected layer
        return x  # Return the output

# Prepare the input-output pairs
input_data = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)  # Input patterns in a tensor format (4x2)
output_data = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)  # Output patterns in a tensor format (4x1)

# Initialize the ANN
input_size = 2  # Number of input neurons
hidden_size = 4  # Number of neurons in the hidden layer
output_size = 1  # Number of output neurons
ann = ANN(input_size, hidden_size, output_size)  # Create an instance of the ANN

# Define the loss function and optimizer
# Mean squared error loss (standard loss function for regression tasks)
criterion = nn.MSELoss()  
# Stochastic gradient descent optimizer with learning rate 0.1 (standard optimizer for training neural networks)
optimizer = optim.SGD(ann.parameters(), lr=0.1)  

# Train the ANN
num_epochs = 1000  # Number of training epochs (iterations)
for epoch in range(num_epochs):
    optimizer.zero_grad()  # Clear the gradients
    output = ann(input_data)  # Forward pass
    loss = criterion(output, output_data)  # Compute the loss
    loss.backward()  # Backpropagation to compute the gradients
    optimizer.step()  # Update the weights based on the gradients
    
    # Print the loss at every 100 epochs for monitoring
    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


# Test the trained ANN
test_input = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)  # Test input patterns
test_output = ann(test_input)  # Predict the output
print(test_output)  # Print the predicted output

# Model evaluation
# The performance of the trained ANN can be evaluated using metrics such as accuracy, precision, recall, and F1 score 
# Accuracy:
correct_predictions = (test_output.round() == output_data).sum().item()
total_predictions = output_data.size(0)
accuracy = correct_predictions / total_predictions
print(f'Accuracy: {accuracy:.2f}')

# Precision:
true_positives = ((test_output.round() == 1) & (output_data == 1)).sum().item()
false_positives = ((test_output.round() == 1) & (output_data == 0)).sum().item()
precision = true_positives / (true_positives + false_positives)
print(f'Precision: {precision:.2f}')

# Recall:
false_negatives = ((test_output.round() == 0) & (output_data == 1)).sum().item()
recall = true_positives / (true_positives + false_negatives)
print(f'Recall: {recall:.2f}')

# F1 score:
f1_score = 2 * (precision * recall) / (precision + recall)
print(f'F1 Score: {f1_score:.2f}')


