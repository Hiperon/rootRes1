"""Module for basic visualization of data

Functions exported by vis.py:
    *   plt_arr - Draw base plot from one dimension data to STDOUT"""
import matplotlib.pyplot as plt


def plt_arr(array):
    """Draw base plot from one dimension data to STDOUT

    :param array: one dimensional array of numbers
    """
    plt.plot(array)
    plt.show()

def distribution_arr(array, n=10):
    """Draw distribution from array, it will have n points

    :param array: one dimensional awkward array of numbers
    :param n: default 10, number of points on graph
    """
    np_arr = array.to_numpy() #na numpy znam funkcje
    np_arr.sort()
    delta = np_arr[-1] - np_arr[0]
    dx = delta/n
    print("minimum: {}".format(np_arr[0]))
    print("dx: {}".format(dx))
    print(np_arr.size)
    data_x = []
    data_y = []
    arr_i = 0 #licznik miejsca w liście na którym jestem
    #żeby tylko raz przeiterować listę
    for i in (range(n)):
        dxi = dx*(i+1) + np_arr[0]
        data_x.append(dxi - 0.5*dx)
        licznik = 0 #licznik zliczające nam wystąpienia w danym rozkładzie
        while np_arr[arr_i] <= dxi:
            licznik += 1
            arr_i += 1
            if(arr_i == np_arr.size):
                break
        data_y.append(licznik)

    print(*data_x)
    print(*data_y)
    sum = 0
    for record in data_y:
        sum += record
    print(sum)

    plt.plot(data_x, data_y)
    plt.show()


