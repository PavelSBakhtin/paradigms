import math


def correlation(data_1, data_2):

    n = len(data_1)
    mean_1 = sum(data_1) / n
    mean_2 = sum(data_2) / n

    variance_1 = sum([(x - mean_1) ** 2 for x in data_1])
    variance_2 = sum([(y - mean_2) ** 2 for y in data_2])

    covariance = sum([(x - mean_1) * (y - mean_2) for x, y in zip(data_1, data_2)])
    correlation = covariance / (math.sqrt(variance_1 * variance_2))

    return correlation


if __name__ == '__main__':

    array_1 = [4, 6, 9, 16, 19, 24, 32, 37, 43]
    array_2 = [3, 4, 5, 8, 13, 18, 24, 29, 34]

    print(f"Корреляция Пирсона: {round(correlation(array_1, array_2), 4)}")
