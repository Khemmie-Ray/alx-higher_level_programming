#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    arrx = 0

    try:
        for i in my_list:
            if arrx < x:
                print('{}'.format(my_list[arrx]), end='')
                arrx += 1

        print()
    except TypeError:
        pass
    finally:
        return arrx
