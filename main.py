# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import rootf

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
    print(array_time)
main()
