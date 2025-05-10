import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os


def build_matrix_A(N):
    A = np.eye(N) * 1.0
    for i in range(N):
        A[i, (i - 1) % N] = -1.0
    return A


def read_initial_data(filename):
    return np.loadtxt(filename)


def evolve_system(u_init, steps=255):
    N = len(u_init)
    A = build_matrix_A(N)
    u = u_init.copy()
    history = [u.copy()]

    for _ in range(steps):
        u = u - 0.5 * A @ u
        history.append(u.copy())

    return np.array(history)


def save_animation(history, filename="evolution.gif"):
    temp_dir = "temp_frames"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        frame_paths = []
        for i, frame_data in enumerate(history):
            plt.figure(figsize=(10, 6))
            plt.plot(frame_data)
            plt.ylim(history.min(), history.max())
            plt.title(f"Time Step: {i}")
            frame_path = os.path.join(temp_dir, f"frame_{i:03d}.png")
            plt.savefig(frame_path, dpi=100, bbox_inches='tight')
            plt.close()
            frame_paths.append(frame_path)

        frames = [imageio.imread(path) for path in frame_paths]
        imageio.mimsave(filename, frames, fps=15, loop=0)

    finally:
        for path in frame_paths:
            if os.path.exists(path):
                os.remove(path)
        if os.path.exists(temp_dir):
            os.rmdir(temp_dir)

    print(f"Анимация сохранена как {filename}")

if __name__ == "__main__":
    u_init = read_initial_data("3.dat")
    history = evolve_system(u_init)
    save_animation(history, "system_evolution.gif")