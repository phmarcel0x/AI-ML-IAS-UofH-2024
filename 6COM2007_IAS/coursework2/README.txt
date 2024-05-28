# 6COM2007 - Coursework 2: README
# Author: Marcelo Hernandes 
# University of Hertfordshire - ID: 23033126
# April 25, 2024

Project Components
~ Exploratory Data Analysis (EDA): This Jupyter notebook (exploratoryDA.ipynb) performs initial data loading, cleaning, and visual exploration of environmental data.
~ Intelligence: This Jupyter notebook (intelligence.ipynb) applies machine learning techniques using a RandomForestRegressor to predict satisfaction levels based on environmental factors.
~ System Design: The simulation (systen.ipynb) models and predicts the effectiveness of real-time adjustments in a smart home environment, such as heating and ventilation, to optimise satisfaction.

Libraries Required
~ Pandas for data manipulation.
~ Matplotlib and Seaborn for data visualisation.
~ Scikit-learn for machine learning model development.
~ Joblib for model serialisation.
~ Tkinter and Matplotlib's animation for creating interactive simulation GUIs.

Installation and Setup
~ Install Python dependencies: pandas, matplotlib, seaborn, scikit-learn, numpy, joblib, and tkinter.
~ Clone this repository and navigate into the project directory.
~ Ensure all data files are placed in the ../data/ directory relative to the notebooks.

Open each Jupyter notebook in the following order to execute the project:
~ Run exporatoryDA.ipynb to preprocess and explore the data.
~ Execute intelligence.ipynb to build and evaluate the satisfaction prediction model.
~ Use system.ipynb to simulate system responses based on the model predictions.
~ Move on to the simulation below

Simulation Interface
~ The simulation.py script utilises a Tkinter GUI to dynamically display changes in environmental conditions and predicted satisfaction over time.
~ The simulation data is found inside ../data/SIMULATION_output.csv

Thank you for reading. 