# %% [markdown]
# # 6COM1044 - Data Classification Coursework
# - Marcelo Pedroza Hernandez
# - UH Student ID: 23033126
# - April 10, 2024

# %%
#Used Libraries
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# %% [markdown]
# ### Task 1 - Data Exploration (20 marks)
# - In this task, you need to use Principal Component Analysis (PCA) to understand the characteristics of the datasets.

# %%
# Task 1 - (a)

# Load the training and test datasets
train_df = pd.read_csv("../mlnc_DATA/wdbc_training.csv")
test_df = pd.read_csv("../mlnc_DATA/wdbc_test.csv")

# Save the 30 features and the labels in separate variables for both datasets
y_train = train_df.iloc[:, 1]
X_train = train_df.iloc[:, 2:32]
y_test = test_df.iloc[:, 1]
X_test = test_df.iloc[:, 2:32]

# %%
# Task 1 - (b)

# Show a scatter plot of the first two features of the training dataset
plt.scatter(X_train.iloc[:, 0], X_train.iloc[:, 1], c=y_train)
plt.xlabel('Feature 1', fontweight='bold')
plt.ylabel('Feature 2', fontweight='bold')
plt.title('Scatter plot of the first two features of the training dataset', fontweight='bold')
plt.show()

# %%
# Task 1 - (c)

# Normalise the training and test datasets using StandardScaler() from sklearn
X_train_norm = StandardScaler().fit_transform(X_train)
X_test_norm = StandardScaler().fit_transform(X_test)

# Report the mean and standard deviation for the first feature in the normalized test set
mean1 = np.mean(X_test_norm[:, 0])
print(mean1)  # Near 0 = OK
std1 = np.std(X_test_norm[:, 0])
print(std1)  # Near 1 (unit std) = OK

# %%
# Task 1 - (d)

# Perform a PCA analysis on the scaled training set
pca = PCA()
projections = pca.fit_transform(X_train_norm)  # The projections matrix represents the eigenvectors of the covariance matrix
print(f"PCA Projections Shape: {projections.shape}")  # Confirm the shape of the projections matrix matches the number of features

# Report how much variance has been captured in the PCA analysis
variance_ratios = pca.explained_variance_ratio_
print(f"\nVariance Captured by each PCA component:\n {variance_ratios}")  # Order of variance ratios is the order of the PCA components
variance_ratio_sum = np.sum(variance_ratios)  # Confirm the sum of the variance ratios is 1
print(f"\nSum of Variance Captured by PCA components: {variance_ratio_sum}")


# %%
# Task 1 - (d) Plots

# Two subplots in one figure
figure1, ax = plt.subplots(1, 2, figsize=(15, 5))

# Projection of the training set in PC1 and PC2
ax[0].scatter(projections[:, 0], projections[:, 1], c=y_train) 
ax[0].set_xlabel('PC1', fontweight='bold')
ax[0].set_ylabel('PC2', fontweight='bold')
ax[0].set_title('Projection of the training set in the first two principal components', fontweight='bold', fontsize=11)

# Scree plot of the variance captured by each component
ax[1].plot(range(1, 31), variance_ratios, marker='.', color='orange') 
ax[1].set_xlabel('Principal Components', fontweight='bold')
ax[1].set_ylabel('Variance Captured', fontweight='bold')
ax[1].set_title('Scree Plot', fontweight='bold')
 
plt.show()
figure1.savefig('Task1_D_Plots.png')

# %% [markdown]
# ### Task 2 - Data Preparation (5 marks)
# - In this task, you need to divide the training dataset into a smaller training set and a validation set, and normalise the data.

# %%
# Task 2 - (a)

# Divide the training set using 30% as the validation set, randomly selecting the points
X_train_II, X_val, y_train_II, y_val = train_test_split(X_train, y_train, test_size=0.3, random_state=38)
# X_train_II, X_val, y_train_II, y_val = train_test_split(X_train, y_train, test_size=0.3, random_state=38, stratify=y_train)  # Stratify the split to maintain the class distribution

# Report the number of points in each set
print(f"Number of points in the smaller training set: {X_train_II.shape[0]}")
print(f"Number of points in the validation set: {X_val.shape[0]}")

# %%
# Task 2 - (b)

# Normalise the smaller training set (II)
X_train_II_norm = StandardScaler().fit_transform(X_train_II)
mean2 = np.mean(X_train_II_norm[:, 0])
print(mean2)  # Near 0 = OK
std2 = np.std(X_train_II_norm[:, 0])
print(std2)  # Near 1 (unit std) = OK

# Normalise the validation set
X_val_norm = StandardScaler().fit_transform(X_val)
mean3 = np.mean(X_val_norm[:, 0])
std3 = np.std(X_val_norm[:, 0])
print(std3)  # Near 1 (unit std) = OK

# %% [markdown]
# ### Task 3 - SVM Classification (12 marks)
# - In this task, you need to build a support vector classifier using SVC from sklearn library.

# %%
# Task 3 - (a) Linear Kernel

# Evaluate performance using a linear kernel with three different C values 
print("\nClassification Reports for Linear Kernel with Different C Values:")
svc1_lin = SVC(kernel='linear', C=2)  # Smallest C value
model1_lin = svc1_lin.fit(X_train_II_norm, y_train_II)
y_pred1_lin = model1_lin.predict(X_val_norm)
print(f"Classification Report for C=2:\n{classification_report(y_val, y_pred1_lin)}")

svc2_lin = SVC(kernel='linear', C=27)  # Middle C value
model2_lin = svc2_lin.fit(X_train_II_norm, y_train_II)
y_pred2_lin = model2_lin.predict(X_val_norm)
print(f"Classification Report for C=27:\n{classification_report(y_val, y_pred2_lin)}")

svc3_lin = SVC(kernel='linear', C=52)  # Largest C value
model3_lin = svc3_lin.fit(X_train_II_norm, y_train_II)
y_pred3_lin = model3_lin.predict(X_val_norm)
print(f"Classification Report for C=52:\n{classification_report(y_val, y_pred3_lin)}")

# %%
# Task 3 - (a) RBF Kernel
# Define parameter grid for the GridSearchCV for finding the best C and gamma values
# param_grid = {'C': np.arange(2, 52, 1), 'gamma': np.arange(0.01, 12, 0.025)} 

# svm_rbf = SVC(kernel='rbf')

# # Perform a grid search to find the best C and gamma values
# grid_search = GridSearchCV(svm_rbf, param_grid=param_grid, cv=20, scoring='accuracy', n_jobs=-1)
# grid_search.fit(X_train_II_norm, y_train_II)

# # Find the best parameter combination
# best_params = grid_search.best_params_
# best_score = grid_search.best_score_

# print(f"Best Parameters: {best_params}")
# print(f"Best Mean Cross-Validated Score (accuracy): {best_score:.3f}")

# # Extract and report the top three combinations of C and gamma values based on rank
# results = grid_search.cv_results_
# sorted_indices = np.argsort(results['mean_test_score'])[::-1]  # Sorting in descending order

# print("\nTop Three Combinations of C and gamma Values with Classification Reports:")

# for rank, index in enumerate(sorted_indices[:3], start=1):  # Just the top 3
#     best_C = results['param_C'][index]
#     best_gamma = results['param_gamma'][index]
    
#     # Since GridSearchCV refits the best model, only detail the top combination here
#     if rank == 1:
#         best_model = grid_search.best_estimator_  # The model refitted with the best parameters
#         y_pred = best_model.predict(X_val_norm)
#     else:
#         # Manually train models for the 2nd and 3rd best parameter sets
#         best_model = SVC(kernel='rbf', C=best_C, gamma=best_gamma)
#         best_model.fit(X_train_II_norm, y_train_II)
#         y_pred = best_model.predict(X_val_norm)
    
#     accuracy = accuracy_score(y_val, y_pred)
    
#     print(f"\nRank: {rank}")
#     print(f"Parameters - C: {best_C}, gamma: {best_gamma}")
#     print(f"Accuracy: {accuracy:.3f}")
#     print("Classification Report:")
#     print(classification_report(y_val, y_pred))



######################################################################################################
# Evaluate performance using an RBF kernel with the top three best combinations of C and gamma values found from the randomised search

# Define parameter grid for the randomised cross-validation search for the best C and gamma values
param_grid = {'C': np.arange(2, 52, 1), 'gamma': np.arange(0.01, 12, 0.01)} 

svm_rbf = SVC(kernel='rbf')

# Perform a randomised search for the best C and gamma values
random_search = RandomizedSearchCV(svm_rbf, param_distributions=param_grid, n_iter=200, cv=100, random_state=38, n_jobs=-1)
random_search.fit(X_train_II_norm, y_train_II)

# Extract the results
results = random_search.cv_results_

# Sort the scores and get indices of top three combinations
top_three_indices = np.argsort(results['mean_test_score'])[-3:]

# Report the top three combinations of C and gamma values
print("\nTop Three Combinations of C and gamma Values:")
for rank, index in enumerate(top_three_indices, start=1):
    print(f"{rank}. Mean validation score: {results['mean_test_score'][index]:.3f} (std: {results['std_test_score'][index]:.3f})")
    print(f"   C: {results['param_C'][index]}, gamma: {results['param_gamma'][index]}")

######################################################################################################
# Define parameter grid for the cross-validation search for the best C and gamma values
# svm1_rbf = SVC(kernel='rbf', C=2, gamma=0.01)  # Smallest C and gamma values
# model1_rbf = svm1_rbf.fit(X_train_II_norm, y_train_II)
# y_pred1_rbf = model1_rbf.predict(X_val_norm)
# print(f"Classification Report for C=2 and gamma=0.01:\n{classification_report(y_val, y_pred1_rbf)}")

# svm2_rbf = SVC(kernel='rbf', C=27, gamma=0.35)  # Middle C and geometric mean of gamma values
# model2_rbf = svm2_rbf.fit(X_train_II_norm, y_train_II)
# y_pred2_rbf = model2_rbf.predict(X_val_norm)
# print(f"Classification Report for C=27 and gamma=0.35:\n{classification_report(y_val, y_pred2_rbf)}")

# svm3_rbf = SVC(kernel='rbf', C=52, gamma=12)  # Largest C and gamma values
# model3_rbf = svm3_rbf.fit(X_train_II_norm, y_train_II)
# y_pred3_rbf = model3_rbf.predict(X_val_norm)
# print(f"Classification Report for C=52 and gamma=12:\n{classification_report(y_val, y_pred3_rbf)}")

# %%
"""train an SVM model with the suitable parameter values discovered
in Task 3 (b) on the normalised whole training set (I). Report the classification report and confusion matrix"""

# Task 3 - (c) Further Evaluation of the Best-Performing Model (RBF Kernel with C=2 and gamma=0.02)

# Train the best-performing model on the normalised whole training set (I)
# svm_best = SVC(kernel='rbf', C=27, gamma=0.2) # Best C and gamma values from Task 3 (a)
svm_best = SVC(kernel='rbf', C=20, gamma=0.2)
model_best = svm_best.fit(X_train_norm, y_train)
y_pred_best = model_best.predict(X_train_norm)
print(f"Classification Report for the best-performing model:\n{classification_report(y_train, y_pred_best)}")

model_test = svm_best.fit(X_test_norm, y_test)
y_pred_test = model_test.predict(X_test_norm)
print(f"Classification Report for the best-performing model on the test set:\n{classification_report(y_test, y_pred_test)}")


# %%



