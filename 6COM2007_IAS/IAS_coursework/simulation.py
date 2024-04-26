# 6COM2007 - Coursework 2: Simulation Design 
# Author: Marcelo Hernandez 
# University of Hertfordshire - ID: 23033126
# April 25, 2024

# Libraries
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.animation as animation

# Load your dataset
df = pd.read_csv('C:/Users/marsp/OneDrive/Escritorio/UK/code-AI-ML-IAS/6COM2007_IAS/IAS_DATA/output.csv', parse_dates=['Datetime'], index_col='Datetime')

# Set up the tkinter window
root = tk.Tk()
root.wm_title("Smart Home Simulation")

# Create the figure for plotting with a specific layout
fig = Figure(figsize=(12, 8), dpi=100)

# Creating subplots for each condition
temp_ax = fig.add_subplot(131)  # Temperature plot
hum_ax = fig.add_subplot(132)  # Humidity plot
co2_ax = fig.add_subplot(133)  # CO2 plot

# Setting the positions of each subplot for clear separation
temp_ax.set_position([0.3, 0.7, 0.6, 0.2])
hum_ax.set_position([0.3, 0.4, 0.6, 0.2])
co2_ax.set_position([0.3, 0.1, 0.6, 0.2])

# Setting up the satisfaction gauge on the left
satisfaction_ax = fig.add_axes([0.05, 0.1, 0.15, 0.8])  # Satisfaction gauge
satisfaction_ax.set_title('Satisfaction Levels', color='black')

# Plotting initial data
temp_line, = temp_ax.plot(df.index, df['Indoor Temperature'], 'r-', label='Temperature')
hum_line, = hum_ax.plot(df.index, df['Indoor Humidity'], 'b-', label='Humidity')
co2_line, = co2_ax.plot(df.index, df['Predicted Satisfaction'], 'g-', label='Satisfaction')

# Customize each subplot with titles and axes labels
temp_ax.set_title('Indoor Temperature')
temp_ax.set_ylabel('Temp (°C)')
hum_ax.set_title('Indoor Humidity')
hum_ax.set_ylabel('Humidity (%)')
co2_ax.set_title('Satisfaction')
co2_ax.set_ylabel('Satisfaction Level')
co2_ax.set_xlabel('Time')

for ax in [temp_ax, hum_ax, co2_ax]:
    ax.grid(True)  # Enable grid
    ax.label_outer()  # Only show bottom and left labels and tick labels

# Initialize the satisfaction gauge and labels
satisfaction_ax.set_xlim(0, 1)
satisfaction_ax.set_ylim(0, 100)
satisfaction_bar = satisfaction_ax.barh(0, 100, color='green')
satisfaction_ax.xaxis.set_visible(False)

def skip_to_end():
    global ani
    ani.event_source.stop()  # Stop the animation
    update_graph(len(df))  # Update the graph with the final frame
    
def restart_animation():
    global ani
    ani.event_source.start()  # Restart the animation
    update_graph(0)  # Update the graph with the initial frame

# Create a "Restart" button
restart_button = tk.Button(root, text='Restart', command=restart_animation)
restart_button.pack(side=tk.BOTTOM)  # Place the button at the bottom of the window

# Create a "Skip to End" button
skip_button = tk.Button(root, text='Skip to End', command=skip_to_end)
skip_button.pack(side=tk.BOTTOM)  # Place the button at the bottom of the window

# Function to update the graph data
def update_graph(num):
    temp_line.set_data(df.index[:num], df['Indoor Temperature'][:num])
    hum_line.set_data(df.index[:num], df['Indoor Humidity'][:num])
    co2_line.set_data(df.index[:num], df['Predicted Satisfaction'][:num])

    # Update satisfaction gauge based on current value
    satisfaction_value = df['Predicted Satisfaction'].iloc[num-1]
    satisfaction_color = 'yellow' if satisfaction_value < 9.00 else 'green'
    satisfaction_bar[0].set_width(1)
    satisfaction_bar[0].set_height(satisfaction_value)
    satisfaction_bar[0].set_color(satisfaction_color)
    
    # Redraw the canvas
    canvas.draw()

# Embed the plot in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Animation function
ani = animation.FuncAnimation(fig, update_graph, frames=len(df), interval=100, repeat=False)

root.mainloop()