from time import sleep

import numpy as np
import matplotlib.pyplot as plt


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
                print("i am here")
            else:
                new_state[i, j] = state[i, j]

    return new_state


def start(initial_state=None, loop_delay=1, size=(100, 100)):
    if initial_state is None:
        state = get_initial_state(size)
    else:
        state = intial_state

    age = np.zeros(size, dtype=int)
    counter = 0

    while True:
        state = compute_next_state(state)
        age += state
        age = age * state
        counter += 1
        plt.imshow(state.repeat(4, axis=0).repeat(4, axis=1))
        plt.pause(loop_delay)

        if np.sum(state) == 0:
            print(counter)
            state = get_initial_state(size)
            age = np.zeros(size, dtype=int)
            counter = 0

if __name__ == "__main__":
    start()
