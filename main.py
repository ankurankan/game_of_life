from time import sleep

import numpy as np


def get_initial_state(size):
    return np.random.choice([0, 1], size)

def compute_next_state(state):
    new_state = np.zeros(state.shape, dtype=int)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            low_x, high_x = max(0, i-1), min(i+1, state.shape[0])
            low_y, high_y = max(0, j-1), min(j+1, state.shape[0])
            n_live = np.sum(state[low_x: high_x, low_y: high_y]) - state[i, j]

            if (state[i, j] == 1) and (n_live < 2):
                new_state[i, j] = 0
            elif (state[i, j] == 1) and (2 <= n_live <= 3):
                new_state[i, j] = 1
            elif (state[i, j] == 1) and (n_live > 3):
                new_state[i, j] = 0
            elif (state[i, j] == 0) and (n_live == 3):
                new_state[i, j] = 1
            else:
                new_state[i, j] = state[i, j]

    return new_state


def start(loop_delay=1, size=(800, 800)):
    state = get_initial_state(size)
    age = np.zeros(size, dtype=int)
    counter = 0

    while True:
        state = compute_next_state(state)
        age += state
        age = age * state
        counter += 1
        sleep(loop_delay)

        if np.sum(state) == 0:
            print(counter)
            state = get_initial_state(size)
            age = np.zeros(size, dtype=int)
            counter = 0

if __name__ == "__main__":
    start()
