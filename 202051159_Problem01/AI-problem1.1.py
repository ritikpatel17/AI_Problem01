# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tchs4XyO1dmDbJNx5zE3IG9Q4AEw7Hds
"""

import numpy as np

# Define the MDP
prob_correct_answer = [0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
rewards = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000]
n_states = len(prob_correct_answer)

# Set discount factor and convergence threshold
gamma = 1
epsilon = 0.001

# Initialize the value function and policy
V = np.zeros(n_states+1)
policy = np.zeros(n_states, dtype=int)

while True:
    # Initialize the change in value function
    delta = 0
    
    # Perform a single iteration of value iteration for each state
    for s in range(n_states):
        # Calculate the expected value of each action
        stay_value = prob_correct_answer[s] * (rewards[s] + gamma * V[s+1])
        quit_value = rewards[s]
        
        # Determine the optimal value and action for this state
        max_value = max(stay_value, quit_value)
        if max_value == quit_value:
            policy[s] = 1  # 1 represents the "Quit" action
        else:
            policy[s] = 0  # 0 represents the "Stay" action
        
        # Update the value function
        delta = max(delta, abs(max_value - V[s]))
        V[s] = max_value
    
    # Check for convergence
    if delta < epsilon:
        break

# Play the game using the optimal policy
state = 0
total_reward = 0
while policy[state] == 0:
    # Player chooses to "Stay"
    if np.random.random() < prob_correct_answer[state]:
        total_reward += rewards[state]
        state += 1
        if state == n_states:
            print("Congratulations, you answered all questions correctly and earned a total reward of {} INR!".format(total_reward))
            break
    else:
        print("Sorry, your answer was incorrect. Game over. You earned a total reward of {} INR.".format(total_reward))
        break

# Player chooses to "Quit"
if policy[state] == 1:
    total_reward += rewards[state]
    print("You chose to quit the game and earned a total reward of {} INR.".format(total_reward))