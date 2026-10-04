import numpy as np
def simulate_markov_chain(transition_matrix, initial_state, num_steps):
    chain = []
    state = initial_state
    for it in range(num_steps + 1): 
        chain.append(state)
        state = np.random.choice([0, 1], p=transition_matrix[state])
    
    return chain