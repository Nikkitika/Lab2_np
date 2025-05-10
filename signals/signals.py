import numpy as np
import matplotlib.pyplot as plt
import os


def read_data(filename):
    with open(filename, 'r') as f:
        data = [float(line.strip()) for line in f if line.strip()]
    return np.array(data)


def moving_average(data, window_size=10):
    filtered = np.zeros_like(data)
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        filtered[i] = np.mean(data[start:i + 1])
    return filtered


def plot_results(original, filtered, source_filename):
    plt.figure(figsize=(12, 6))
    plt.plot(original, label="Исходный сигнал", alpha=0.5)
    plt.plot(filtered, label="Фильтрованный сигнал", color='red')
    plt.title("Сравнение сигналов")
    plt.xlabel("Время (отсчёты)")
    plt.ylabel("Значение")
    plt.legend()
    plt.grid(True)

    base_name = os.path.splitext(os.path.basename(source_filename))[0]
    output_file = f"{base_name}_graph.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"График сохранен как: {output_file}")


if __name__ == "__main__":
    input_file = "signal03.dat"  # Укажите ваш файл
    data = read_data(input_file)
    filtered_data = moving_average(data, window_size=10)
    plot_results(data, filtered_data, input_file)