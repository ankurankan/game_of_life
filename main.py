from time import sleep

import numpy as np
import matplotlib.pyplot as plt


def get_initial_state(size):
    return np.random.choice([0, 1], size)

def compute_next_state(state):
    new_state = np.zeros(state.shape, dtype=int)
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            low_x, high_x = max(0, i-1), min(i+2, state.shape[0])
            low_y, high_y = max(0, j-1), min(j+2, state.shape[1])
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


def start(initial_state=None, loop_delay=1, size=(200, 200)):
    if initial_state is None:
        state = get_initial_state(size)
    else:
        state = initial_state
        size = state.shape

    age = np.zeros(size, dtype=int)
    counter = 0

    while True:
        new_state = compute_next_state(state)
        age += new_state
        age = age * new_state
        counter += 1
        plt.imshow(age, cmap='Greys')
        plt.xlim(right=size[1], left=0)
        plt.ylim(top=0, bottom=size[0])
        plt.pause(loop_delay)

        if (np.sum(new_state) == 0) or (new_state == state).all():
            print(counter)
            state = get_initial_state(size)
            age = np.zeros(size, dtype=int)
            counter = 0

        else:
            state = new_state

if __name__ == "__main__":
    start()
