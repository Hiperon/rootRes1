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
