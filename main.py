# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy

from jupiter_root import *
import awkward


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def main():
    print("start")
    data = rootf.Rootf("results1_short100_coincidences.root")
    array_time = data.get_arr("time1")
    array_energy = data.get_arr("energy1")
    print(type(array_time))
    print(*array_time)
    print(array_time[5])
    print(array_time)

    vis.distribution_arr(array_time)
    print(*array_energy)
    vis.distribution_arr(array_energy)

    time1_arr = data.get_arr("time1")
    time2_arr = data.get_arr("time2")
    energy1_arr = data.get_arr("energy1")
    energy2_arr = data.get_arr("energy2")
    print(time1_arr[-3])
    print(time2_arr[-3])
    print(energy1_arr[-3])
    print(energy2_arr[-3])
    rstat.mmm(energy1_arr)


main()
