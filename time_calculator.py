# Time calculator 
##################

import math, re
from termcolor import colored, cprint
import os, sys


# subtraction mode
def subtraction():
    def subtract():
        def time_subtract():
            time1_ho = int(time1[:2]) * 60
            time1_min = int(time1[2:4])
            time1_sum = time1_ho + time1_min

            time2_ho = int(time2[:2]) * 60
            time2_min = int(time2[2:4])
            time2_sum = time2_ho + time2_min

            if time1_sum <= time2_sum:
                division = time2_sum - time1_sum
            else:
                time2_sum_zero = time2_sum + 1440
                division = time2_sum_zero - time1_sum

            division_time = division / 60

            total_ho = math.trunc(division_time)
            total_ho_str = str(total_ho)
            total_min = round((division_time - total_ho) * 60)
            total_min_str = str(total_min)

            if (len(total_ho_str) == 1):
                total_ho_str = "0" + total_ho_str

            if len(total_min_str) == 1:
                total_min_str = total_min_str + "0"

            total_sum = "= " + total_ho_str + ":" + total_min_str

            # print(time1_sum)        print(time2_sum)        print(division)        print(division_time)        print(total_ho)        print(total_min)
            cprint(total_sum, "blue")
            subtraction()


        time1 = input(f"{colored('>>', 'blue')}").replace(":", "").replace(" ", "").lower()
        if (time1 == "/1"):
            cprint("--subtraction:--", "blue")
            subtraction()
        elif (time1 == "/2"):
            cprint("--addition:--", "green")
            addition()
        elif (time1 == "/help"):
            print(help())
            subtraction()
        elif (time1 == "/exit"):
            cprint("exited successfully", "red")
            exit()
        elif ((not re.match("^[0,1,2,3,4,5,6,7,8,9]*$", time1)) or (len(time1)) != 4):
            cprint("wrong input", "red")
            cprint("restarted", "red")
            beginning()
        else:
            pass

        time2 = input(f"{colored('>>', 'blue')}").replace(":", "").replace(" ", "").lower()
        if (time2 == "/1"):
            cprint("--subtraction:--", "blue")
            subtraction()
        elif (time2 == "/2"):
            cprint("--addition:--", "green")
            addition()
        elif (time2 == "/help"):
            print(help())
            subtraction()
        elif (time2 == "/exit"):
            cprint("exited successfully", "red")
            exit()
        elif ((not re.match("^[0,1,2,3,4,5,6,7,8,9]*$", time1)) or (len(time1)) != 4):
            cprint("wrong input", "red")
            cprint("restarted", "red")
            subtraction()
        else:
            time_subtract()


    subtract()


# addition mode
def addition():
    def add_time(time):
        time_ho = int(time[:2]) * 60
        time_min = int(time[2:4])
        time_sum = time_ho + time_min
        return time_sum


    check = re.compile("[+]")

    def menu_check():
        if ((a or b or c or d or e or f) == "/1"):
            cprint("--subtraction:--", "blue")
            subtraction()
        elif ((a or b or c or d or e or f) == "/2"):
            cprint("--addition:--", "green")
            addition()
        elif ((a or b or c or d or e or f) == "/help"):
            print(help())
            addition()
        elif ((a or b or c or d or e or f) == "/exit"):
            cprint("exited successfully", "red")
            exit()
        else:
            pass

    try:
        a = input(f"{colored('>>', 'green')}").lower()
        menu_check()
        if not check.search(a) == None:
            a = a.replace(":", "").replace(" ", "").replace("+", "")
            if (len(a) == 4):
                a_t = add_time(a)
                total_time = a_t
                b = input(f"{colored('>>', 'green')}").lower()
                menu_check()
            elif (len(a) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'a'", "red")
        elif check.search(a) == None:
            a = a.replace(":", "").replace(" ", "").replace("+", "")
            if (len(a) == 4):
                a_t = add_time(a)
                total_time = a_t
            elif (len(a) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'a'", "red")


        if not check.search(b) == None:
            b = b.replace(":", "").replace(" ", "").replace("+", "")
            if (len(b) == 4):
                b_t = add_time(b)
                total_time = a_t + b_t
                c = input(f"{colored('>>', 'green')}").lower()
                menu_check()
            elif (len(b) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'b'", "red")
        elif check.search(b) == None:
            b = b.replace(":", "").replace(" ", "").replace("+", "")
            if (len(b) == 4):
                b_t = add_time(b)
                total_time = a_t + b_t
            elif (len(b) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'b'", "red")


        if not check.search(c) == None:
            c = c.replace(":", "").replace(" ", "").replace("+", "")
            if (len(c) == 4):
                c_t = add_time(c)
                total_time = a_t + b_t + c_t
                d = input(f"{colored('>>', 'green')}").lower()
                menu_check()
            elif (len(c) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'c'", "red")
        elif check.search(c) == None:
            c = c.replace(":", "").replace(" ", "").replace("+", "")
            if (len(c) == 4):
                c_t = add_time(c)
                total_time = a_t + b_t + c_t
            elif (len(c) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'c'", "red")


        if not check.search(d) == None:
            d = d.replace(":", "").replace(" ", "").replace("+", "")
            if (len(d) == 4):
                d_t = add_time(d)
                total_time = a_t + b_t + c_t + d_t
                e = input(f"{colored('>>', 'green')}").lower()
                menu_check()
            elif (len(d) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'd'", "red")
        elif check.search(d) == None:
            d = d.replace(":", "").replace(" ", "").replace("+", "")
            if (len(d) == 4):
                d_t = add_time(d)
                total_time = a_t + b_t + c_t + d_t
            elif (len(d) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'd'", "red")


        if not check.search(e) == None:
            e = e.replace(":", "").replace(" ", "").replace("+", "")
            if (len(e) == 4):
                e_t = add_time(e)
                total_time = a_t + b_t + c_t + d_t + e_t
                f = input(f"{colored('>>', 'green')}").replace(" ", "").replace("+", "").lower() # exception for last 'addition'
                menu_check()
            elif (len(e) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'e'", "red")
        elif check.search(e) == None:
            e = e.replace(":", "").replace(" ", "").replace("+", "")
            if (len(e) == 4):
                e_t = add_time(e)
                total_time = a_t + b_t + c_t + d_t + e_t
            elif (len(e) == 1):
                cprint("finished", "red")
            else:
                cprint("Error: sector 'e'", "red")


        if (len(f) == 4):
            f_t = add_time(f)
            total_time = a_t + b_t + c_t + d_t + e_t + f_t
        elif (len(f) == 1):
            cprint("finished", "red")
        else:
            cprint("Error: sector 'f'", "red")

    except (NameError, ValueError) as err:
        pass


    def add_time_total():
        division_time = total_time / 60
        
        total_ho = math.trunc(division_time)
        total_ho_str = str(total_ho)
        total_min = round((division_time - total_ho) * 60)
        total_min_str = str(total_min)

        if (len(total_ho_str) == 1):
            total_ho_str = "0" + total_ho_str
        if (len(total_min_str) == 1):
            total_min_str = total_min_str + "0"

        total_sum = "= " + total_ho_str + ":" + total_min_str

        # print(division_time)   print(total_ho)    print(total_min)    print()
        return total_sum


    cprint(add_time_total(), "green") 
    addition()


# Start menu
def option_text():
    option_text = f"""
{colored("For time subtraction type: '/1'", "blue")}
{colored("For addition type: '/2'", "green")}
{colored("For help type: '/help'", "yellow")}
{colored("For exit type: '/exit'", "red")}
"""
    return option_text


def help():
    help_txt = f"""
{colored("For time subtraction: choose 2 times to subtract", "blue")}
{colored("For addition: choose times and add '+' at the end to add more numbers", "green")}
"""
    return help_txt


def beginning():
    cprint(option_text())

    option = input("> ")

    if option == "/help":
        print(help())
    elif option == "/exit":
        cprint("exited successfully", "red")
        exit()
    elif option == "/1": 
        subtraction()
    elif option == "/2":
        addition()
    else:
        cprint("Option doesn't exist", "red")
        beginning()


try:
    beginning()
except KeyboardInterrupt:
    cprint("exited successfully", "red")
    exit()