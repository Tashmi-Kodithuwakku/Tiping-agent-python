# -*- coding: utf-8 -*-
"""TippingAgent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kbx3qFGFE969E8VQNfuuYJtWvBb3PBvg
"""

! pip install scikit-fuzzy

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define the input variables
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')

# Define the output variable
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Create the membership functions
service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['average'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

quality['poor'] = fuzz.trimf(quality.universe, [0, 0, 5])
quality['average'] = fuzz.trimf(quality.universe, [0, 5, 10])
quality['excellent'] = fuzz.trimf(quality.universe, [5, 10, 10])

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 12.5])
tip['medium'] = fuzz.trimf(tip.universe, [0, 12.5, 25])
tip['high'] = fuzz.trimf(tip.universe, [12.5, 25, 25])

# Define the rules
rule1 = ctrl.Rule(service['poor'] | quality['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'] | quality['average'], tip['medium'])
rule3 = ctrl.Rule(service['excellent'] | quality['excellent'], tip['high'])

# Create the control system
tip_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tip_simulator = ctrl.ControlSystemSimulation(tip_ctrl)

# Prompt user for input values
s = input("Enter service rating (0-10): ")
q = input("Enter food quality rating (0-10): ")

# Convert input strings to floats
service_val = float(s)
quality_val = float(q)

# Run the simulation with user inputs
tip_simulator.input['service'] = service_val
tip_simulator.input['quality'] = quality_val

tip_simulator.compute()
print("Tip percentage: ", tip_simulator.output['tip'],"% \n")

# Plot the membership functions for service
service.view()

# Plot the membership functions for quality
quality.view()

# Plot the membership functions for tip
tip.view()

plt.show()