# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Chinese_to_number


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 숫자 하나씩은 1_10폴더에.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    converter = Chinese_to_number.ImageToChineseConverter()
    IMAGE1 = "1_10/chi_ten.png"
    #result = 숫자
    result = converter.imagefile_to_textNum(IMAGE1)
    print(result)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
