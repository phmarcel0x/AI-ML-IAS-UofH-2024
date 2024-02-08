## 6COM1044-0105-Machine Learning and Neural Computing
### Math Fundamentals: Calculus

# Import the required libraries
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Calculate and graph the limit of a function
# Define the variable and the function
x = sp.symbols('x')  # Define the variable
f = x**2 - 3*x + 2  # Define the function

# Calculate the limit of the function as x approaches 1
limit_value = sp.limit(f, x, 1)  # Calculate the limit
print('The limit of the function as x approaches 1 is', limit_value)  

# Create a sequence of x values
x_values = np.linspace(-1, 3, 400)  # 400 points between -1 and 3
y_values = [f.subs(x, xv) for xv in x_values]   # Evaluate the function at each x value

# Create the plot
plt.plot(x_values, y_values, label='$f(x) = x^2 - 3x + 2$')  # Plot the function
plt.scatter(1, limit_value, color='red', label='Limit at 1')  # Plot the limit point
plt.title('Limit of $f(x) = x^2 - 3x + 2$ as x approaches 1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()


# The gradient of a function
# Define the variable and the function
x, y = sp.symbols('x y')  # Define the variables
f = x**2 + y**2  # Define the function

# Calculate the gradient of the function
gradient = sp.Matrix([f]).jacobian([x, y])  # Calculate the gradient
print('The gradient of the function is:')
print(gradient)


# The Jacobian matrix
# Define the variables and the functions
x, y = sp.symbols('x y')  # Define the variables
f1 = x**2 + y**2  # Define the first function
f2 = x**2 - y**2  # Define the second function

# Calculate the Jacobian matrix
jacobian_matrix = sp.Matrix([f1, f2]).jacobian([x, y]) # Calculate the Jacobian matrix
print('The Jacobian matrix is:')
print(jacobian_matrix)

# The Hessian matrix
# Define the variable and the function
x, y = sp.symbols('x y')  # Define the variables
f = x**2 - 3*x*y + 2*y**2 + 5  # Define the function

# Calculate the Hessian matrix
hessian_matrix = sp.hessian(f, (x, y))  # Calculate the Hessian matrix
print('The Hessian matrix is:')
print(hessian_matrix)


# Gradient descent algorithm example
# Define the variable and the function
x, y = sp.symbols('x y')  # Define the variables
f = x**2 + y**2  # Define the function

# Initialize the variables
x_value = 1  # Initial x value
y_value = 1  # Initial y value
learning_rate = 0.1  # Learning rate

# Perform 10 iterations of the gradient descent algorithm
for i in range(10):
    # Calculate the gradient of the function
    gradient = sp.Matrix([f]).jacobian([x, y])  # Calculate the gradient
    gradient_value = gradient.subs({x: x_value, y: y_value})  # Evaluate the gradient at the current point
    
    # Update the variables using the gradient descent algorithm
    x_value = x_value - learning_rate*gradient_value[0]  # Update x
    y_value = y_value - learning_rate*gradient_value[1]  # Update y
    
    # Print the current values of x, y, and the function
    print('x:', x_value, 'y:', y_value, 'f(x, y):', f.subs({x: x_value, y: y_value}))
    
    
    


