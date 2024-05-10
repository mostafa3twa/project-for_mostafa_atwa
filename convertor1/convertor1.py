from tkinter import *
import tkinter.messagebox as messagebox

a = Tk()
a.geometry("480x490+770+50")
a.resizable(False, False)
a.title("Convertor")
a.config(bg="black")


def clear():
    tx1.delete(0, "end")
    tx2.delete(0, "end")
    tx3.delete(0, "end")
    tx4.delete(0, "end")


def exit():
    close = messagebox.askyesno("Alert", "Are you sure that you want to exit?")
    if close > 0:
        a.destroy()


def dec_to_bin():
    dec_num = tx1.get()
    if not all(c in "0123456789.+-" for c in dec_num):
        messagebox.showerror("Error", "The numbers are not valid for this system")
        return None
    if "+" in dec_num:
        num1, num2 = dec_num.split("+")
        sum = float(num1) + float(num2)
    elif "-" in dec_num:
        num1, num2 = dec_num.split("-")
        sum = float(num1) - float(num2)
    else:
        sum = float(dec_num)
    if sum.is_integer():
        bin_num = bin(int(sum))[2:]
    else:
        bin_num = bin(int(sum))[2:] + "."
        frac = sum - int(sum)
        while frac != 0:
            frac *= 2
            if frac >= 1:
                bin_num += "1"
                frac -= 1
            else:
                bin_num += "0"
    return bin_num


def dec_to_oct():
    dec_num = tx1.get()
    if not all(c in "0123456789.+-" for c in dec_num):
        return None
    if "+" in dec_num:
        num1, num2 = dec_num.split("+")
        sum = float(num1) + float(num2)
    elif "-" in dec_num:
        num1, num2 = dec_num.split("-")
        sum = float(num1) - float(num2)
    else:
        sum = float(dec_num)
    if sum.is_integer():
        oct_num = oct(int(sum))[2:]
    else:
        oct_num = oct(int(sum))[2:] + "."
        frac = sum - int(sum)
        while frac != 0:
            frac *= 8
            if frac >= 1:
                oct_num += str(int(frac))
                frac -= int(frac)
            else:
                oct_num += "0"
    return oct_num


def dec_to_hexa():
    dec_num = tx1.get()
    if not all(c in "0123456789.-+" for c in dec_num):
        return None
    if "+" in dec_num:
        num1, num2 = dec_num.split("+")
        sum = float(num1) + float(num2)
    elif "-" in dec_num:
        num1, num2 = dec_num.split("-")
        sum = float(num1) - float(num2)
    else:
        sum = float(dec_num)
    if sum.is_integer():
        hexa_num = hex(int(sum))[2:]
    else:
        hexa_num = hex(int(sum))[2:] + "."

        frac = sum - int(sum)
        while frac != 0:
            frac *= 16
            if frac >= 1:
                if int(frac) < 10:
                    hexa_num += str(int(frac))
                else:
                    hexa_num += chr(int(frac) + 55)
                frac = frac - int(frac)
            else:
                hexa_num += "0"
    return hexa_num


def dec_convertor():
    bin_value = dec_to_bin()
    oct_value = dec_to_oct()
    hexa_value = dec_to_hexa()

    tx2.delete(0, "end")
    tx3.delete(0, "end")
    tx4.delete(0, "end")

    tx2.insert(0, str(bin_value))
    tx3.insert(0, str(oct_value))
    tx4.insert(0, str(hexa_value))


def bin_to_dec():
    bin_num = tx2.get()
    if not all(c in "01.-+" for c in bin_num):
        messagebox.showerror("Error", "The numbers are not valid for this system")
        return None
    if "+" in bin_num:
        num1, num2 = bin_num.split("+")
        return int(num1, 2) + int(num2, 2)
    elif "-" in bin_num:
        num1, num2 = bin_num.split("-")
        return int(num1, 2) - int(num2, 2)
    else:
        if "." in bin_num:
            integer_part, fractional_part = bin_num.split(".")
            dec_num = int(integer_part, 2)
            frac = 0
            i = 1
            for digit in fractional_part:
                if digit == "1":
                    frac += 2 ** (-i)
                i += 1
            dec_num += frac
        else:
            dec_num = int(bin_num, 2)
        return dec_num


def bin_to_oct():
    bin_num = tx2.get()
    if not all(c in "01.-+" for c in bin_num):
        return None
    if "+" in bin_num:
        num1, num2 = bin_num.split("+")
        return oct(int(num1, 2) + int(num2, 2))[2:]
    elif "-" in bin_num:
        num1, num2 = bin_num.split("-")
        return oct(int(num1, 2) - int(num2, 2))[2:]
    elif "." in bin_num:
        integer_part, fractional_part = bin_num.split(".")
        dec_num = int(integer_part, 2)
        frac_num = 0
        i = 1
        for digit in fractional_part:
            if digit == "1":
                frac_num += 2 ** (-i)
            i += 1
        dec_num += frac_num

        oct_num = oct(int(dec_num))[2:] + "."
        frac = dec_num - int(dec_num)
        while frac != 0:
            frac *= 8
            if frac >= 1:
                oct_num += str(int(frac))
                frac -= int(frac)
            else:
                oct_num += "0"
    else:
        oct_num = oct(int(bin_num, 2))[2:]
    return oct_num


def bin_to_hexa():
    bin_num = tx2.get()
    if not all(c in "01.+-" for c in bin_num):
        return None
    if "+" in bin_num:
        num1, num2 = bin_num.split("+")
        return hex(int(num1, 2) + int(num2, 2))[2:]
    elif "-" in bin_num:
        num1, num2 = bin_num.split("-")
        return hex(int(num1, 2) + int(num2, 2))[2:]
    elif "." in bin_num:
        integer_part, fractional_part = bin_num.split(".")
        dec_num = int(integer_part, 2)
        frac_num = 0
        i = 1
        for digit in fractional_part:
            if digit == "1":
                frac_num += 2 ** (-i)
            i += 1
        dec_num += frac_num

        hexa_num = hex(int(dec_num))[2:] + "."
        frac = dec_num - int(dec_num)
        while frac != 0:
            frac *= 16
            if frac >= 1:
                if int(frac) < 10:
                    hexa_num += str(int(frac))
                else:
                    hexa_num += chr(int(frac) + 55)
                frac = frac - int(frac)
            else:
                hexa_num += "0"
    else:
        hexa_num = hex(int(bin_num, 2))[2:]
    return hexa_num


def bin_convertor():
    dec_value = bin_to_dec()
    oct_value = bin_to_oct()
    hexa_value = bin_to_hexa()

    tx1.delete(0, "end")
    tx3.delete(0, "end")
    tx4.delete(0, "end")

    tx1.insert(0, str(dec_value))
    tx3.insert(0, str(oct_value))
    tx4.insert(0, str(hexa_value))


def oct_to_dec():
    oct_num = tx3.get()
    if not all(c in "01234567.-+" for c in oct_num):
        messagebox.showerror("Error", "The numbers are not valid for this system")
        return
    if "+" in oct_num:
        num1, num2 = oct_num.split("+")
        return int(num1, 8) + int(num2, 8)
    elif "-" in oct_num:
        num1, num2 = oct_num.split("-")
        return int(num1, 8) - int(num2, 8)
    elif "." in oct_num:
        integer_part, fractional_part = oct_num.split(".")
        dec_num = int(integer_part, 8)
        frac = 0
        i = 1
        for digit in fractional_part:
            frac += int(digit) * (8**-i)
            i += 1
        dec_num += frac
    else:
        dec_num = int(oct_num, 8)
    return dec_num


def oct_to_bin():
    oct_num = tx3.get()
    if not all(c in "01234567.+-" for c in oct_num):
        return None
    if "+" in oct_num:
        num1, num2 = oct_num.split("+")
        return bin(int(num1, 8) + int(num2, 8))[2:]
    if "-" in oct_num:
        num1, num2 = oct_num.split("-")
        return bin(int(num1, 8) - int(num2, 8))[2:]
    if "." in oct_num:
        integer_part, fractional_part = oct_num.split(".")
        dec_num = int(integer_part, 8)
        frac = 0
        i = 1
        for digit in fractional_part:
            frac += int(digit) * (8**-i)
            i += 1
        dec_num += frac
        bin_num = bin(int(dec_num))[2:] + "."
        frac = dec_num - int(dec_num)
        while frac != 0:
            frac *= 2
            if frac >= 1:
                bin_num += "1"
                frac -= 1
            else:
                bin_num += "0"
    else:
        bin_num = bin(int(oct_num, 8))[2:]
    return bin_num


def oct_to_hex():
    oct_num = tx3.get()
    if not all(c in "01234567.-+" for c in oct_num):
        return None
    if "+" in oct_num:
        num1, num2 = oct_num.split("+")
        return hex(int(num1, 8) + int(num2, 8))[2:]
    if "-" in oct_num:
        num1, num2 = oct_num.split("-")
        return hex(int(num1, 8) - int(num2, 8))[2:]
    if "." in oct_num:
        integer_part, fractional_part = oct_num.split(".")
        dec_num = int(integer_part, 8)
        frac = 0
        i = 1
        for digit in fractional_part:
            frac += int(digit) * (8**-i)
            i += 1
        dec_num += frac
        hexa_num = hex(int(dec_num))[2:] + "."
        frac = dec_num - int(dec_num)
        while frac != 0:
            frac *= 16
            if frac >= 1:
                if int(frac) < 10:
                    hexa_num += str(int(frac))
                else:
                    hexa_num += chr(int(frac) + 55)
                frac = frac - int(frac)
            else:
                hexa_num += "0"
    else:
        hexa_num = hex(int(oct_num, 8))[2:]
    return hexa_num


def oct_convertor():
    dec_value = oct_to_dec()
    hex_value = oct_to_hex()
    bin_value = oct_to_bin()

    tx1.delete(0, "end")
    tx2.delete(0, "end")
    tx4.delete(0, "end")

    tx1.insert(0, str(dec_value))
    tx2.insert(0, str(bin_value))
    tx4.insert(0, str(hex_value))


def hexa_to_dec():
    hexa_num = tx4.get()
    dec_num = 0
    if not all(c in "0123456789ABCDEFabcdef." for c in hexa_num):
        messagebox.showerror("Error", "The numbers are not valid for this system")
        return None
    if "." in hexa_num:
        integer_part, fractional_part = hexa_num.split(".")
        dec_num += int(integer_part, 16)
        frac = 0
        i = 1
        for digit in fractional_part:
            if digit.isdigit():
                frac += int(digit) * (16**-i)
            elif digit.upper() in "ABCDEF":
                frac += (ord(digit.upper()) - 55) * (16**-i)
            i += 1
        dec_num += frac
    else:
        for digit in hexa_num:
            if digit.isdigit():
                dec_num = 16 * dec_num + int(digit)
            elif digit.upper() in "ABCDEF":
                dec_num = 16 * dec_num + (ord(digit.upper()) - 55)
    return dec_num


def hexa_to_bin():
    hexa_num = tx4.get()
    dec_num = 0
    if not all(c in "0123456789ABCDEFabcdef." for c in hexa_num):
        return None
    if "." in hexa_num:
        integer_part, fractional_part = hexa_num.split(".")
        dec_num += int(integer_part, 16)
        frac_dec = 0
        i = 1
        for digit in fractional_part:
            if digit.isdigit():
                frac_dec += int(digit) * (16**-i)
            elif digit.upper() in "ABCDEF":
                frac_dec += (ord(digit.upper()) - 55) * (16**-i)
            i += 1
        dec_num += frac_dec

        bin_num = bin(int(dec_num))[2:] + "."
        frac = dec_num - int(dec_num)
        while frac != 0:
            frac *= 2
            if frac >= 1:
                bin_num += "1"
                frac -= 1
            else:
                bin_num += "0"
    else:
        for digit in hexa_num:
            if digit.isdigit():
                dec_num = 16 * dec_num + int(digit)
            elif digit.upper() in "ABCDEF":
                dec_num = 16 * dec_num + (ord(digit.upper()) - 55)
        bin_num = bin(int(dec_num))[2:]
    return bin_num


def hexa_to_oct():
    hexa_num = tx4.get().upper()
    dec_num = 0
    if not all(c in "0123456789ABCDEFabcdef." for c in hexa_num):
        return None
    if "." in hexa_num:
        integer_part, fractional_part = hexa_num.split(".")
        dec_num += int(integer_part, 16)
        frac_dec = 0
        i = 1
        for digit in fractional_part:
            if digit.isdigit():
                frac_dec += int(digit) * (16**-i)
            elif digit.upper() in "ABCDEF":
                frac_dec += (ord(digit.upper()) - 55) * (16**-i)
            i += 1
        dec_num += frac_dec

        oct_num = oct(int(dec_num))[2:] + "."
        frac = dec_num - int(dec_num)
        while frac != 0:
            frac *= 8
            if frac >= 1:
                oct_num += str(int(frac))
                frac -= int(frac)
            else:
                oct_num += "0"
    else:
        for digit in hexa_num:
            if digit.isdigit():
                dec_num = 16 * dec_num + int(digit)
            elif digit.upper() in "ABCDEF":
                dec_num = 16 * dec_num + (ord(digit.upper()) - 55)
        oct_num = oct(int(dec_num))[2:]
    return oct_num


def hexa_convertor():
    dec_value = hexa_to_dec()
    oct_value = hexa_to_oct()
    bin_value = hexa_to_bin()

    tx1.delete(0, "end")
    tx2.delete(0, "end")
    tx3.delete(0, "end")

    tx1.insert(0, str(dec_value))
    tx2.insert(0, str(bin_value))
    tx3.insert(0, str(oct_value))


bit1 = Button(
    text="convert",
    command=dec_convertor,
    fg="black",
    bg="sky blue",
    cursor="heart",
    width=10,
    height=2,
    font=("Arial", 18),
)
bit1.grid(row=0, column=4)
bit2 = Button(
    text="convert",
    command=bin_convertor,
    fg="black",
    bg="sky blue",
    cursor="heart",
    width=10,
    height=2,
    font=("Arial", 18),
)
bit2.grid(row=1, column=4)
bit3 = Button(
    text="convert",
    command=oct_convertor,
    fg="black",
    bg="sky blue",
    cursor="heart",
    width=10,
    height=2,
    font=("Arial", 18),
)
bit3.grid(row=2, column=4)
bit4 = Button(
    text="convert",
    command=hexa_convertor,
    fg="black",
    bg="sky blue",
    cursor="heart",
    width=10,
    height=2,
    font=("Arial", 18),
)
bit4.grid(row=3, column=4)

bit5 = Button(
    text="Exit",
    command=exit,
    fg="black",
    bg="sky blue",
    cursor="heart",
    width=10,
    height=2,
    font=("Arial", 18),
)
bit5.grid(row=6, column=2)
bit6 = Button(
    text="Clear",
    command=clear,
    fg="black",
    bg="sky blue",
    cursor="heart",
    width=10,
    height=2,
    font=("Arial", 18),
)
bit6.grid(row=5, column=2)

lab1 = Label(
    text="Decimal", fg="black", bg="sky blue", width=10, height=2, font=("Arial", 18)
)
lab1.grid(row=0, column=0)
lab2 = Label(
    text="Binary", fg="black", bg="sky blue", width=10, height=2, font=("Arial", 18)
)
lab2.grid(row=1, column=0)
lab3 = Label(
    text="Octal", fg="black", bg="sky blue", width=10, height=2, font=("Arial", 18)
)
lab3.grid(row=2, column=0)
lab4 = Label(
    text="Hexadecimal",
    fg="black",
    bg="sky blue",
    width=10,
    height=2,
    font=("Arial", 18),
)
lab4.grid(row=3, column=0)

tx1 = Entry(a, justify="center", width=20, font=("Arial", 12))
tx1.grid(row=0, column=2)
tx2 = Entry(justify="center", width=20, font=("Arial", 12))
tx2.grid(row=1, column=2)
tx3 = Entry(justify="center", width=20, font=("Arial", 12))
tx3.grid(row=2, column=2)
tx4 = Entry(justify="center", width=20, font=("Arial", 12))
tx4.grid(row=3, column=2)

a.mainloop()
