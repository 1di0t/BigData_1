#from tkinter import * #GUI module
import tkinter as tk

def is_prime(k) -> bool:
    """
    :param k:소수인지 판별할 양의 수
    :return: If n is Prime :true, Not Prime : False
    """
    if k == 2:return True
    elif k <= 1 or k % 2 == 0:return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i = i + 1
        return True

def primeAndOddEven():
    number =en_input_number.get()
    text =""
    iseven =""
    number =int(number)
    if is_prime(number): text = "소수"
    else : text = "소수가 아님"
    if number%2==0: iseven = "짝수"
    else : iseven = "홀수"
    lab_print_prime_and_odd_even_num.config(text=f"{number}는 {text}\n{number}는 {iseven}")


window = tk.Tk()
window.geometry("500x200")#Size
window.title("솟수")

en_input_number = tk.Entry(window)
lab_print_prime_and_odd_even_num = tk.Label(window,text="소수 판정 프로그램",border=2.4)
btn_prime_num = tk.Button(window,text="소수 판정",background="orange",border=2.4,command=primeAndOddEven)



#placement
lab_print_prime_and_odd_even_num.pack()
en_input_number.pack(fill='x')
btn_prime_num.pack(fill='x')



window.mainloop()