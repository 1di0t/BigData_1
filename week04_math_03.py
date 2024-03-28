def is_prime(k) -> bool:
    """

    :param k:소수인지 판별할 양의 수
    :return: If n is Prime :true, Not Prime : False
    """
    is_prime_num = True
    if k < 2 or k % 2 == 0:
        return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i = i + 1
        return True
def power(base, exponent) -> int:
    return base ** exponent

while(True):
    menu = (input("1 : 소수 \t 2 : 거듭제곱 \t 3 : 몫과 나머지\t 4 : 종료\n: "))
    if menu == '4':
        print()
        break
    elif menu == '1':
        number = int(input("정수 입력"))
        if is_prime(number):
            print("소수")
        else:
            print("소수 아님")
    elif menu == '2':
        base = int(input("input base : "))
        exponent = int(input("input exponent : "))
        print(f"{base}의 {exponent}제곱은 {power(base, exponent)}")
    elif menu == '3':
        dividend = int(input("input dividend : "))
        divisor = int(input("input divisor : "))
        print(f"{dividend} // {divisor} = {divmod(dividend, divisor)[0]}")
        print(f"{dividend} % {divisor} = {divmod(dividend, divisor)[1]}")
    else:
        print(f"{menu}는 잘못된 값입니다")
