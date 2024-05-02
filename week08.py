# beverage = ['Espresso', 'Compagina', 'Lemonade']
# prices = [2000, 2500, 3900]

beverage_Price_Amount = {'Espresso':[2000,0],'Compagina':[2500,0],'Lemonade':[3900,0]}
total_Price = 0
keys = list(beverage_Price_Amount.keys())
def select_menu(key):
    """
    Print selected menu and increase quantity, totalPrice
    :param menu_number:
    :return: none
    """
    global total_Price
    print(f"{key} 주문완료")
    beverage_Price_Amount[key][1] += 1
    total_Price += beverage_Price_Amount[key][0]

def print_menu(keys):
    i = 0
    for i in range(len(beverage_Price_Amount)):
        print(f"{i+1}) {keys[i]:<20}{beverage_Price_Amount[keys[i]][0]:<6}")
    print(f"{len(beverage_Price_Amount)+1}) exit")

def print_recipe():
    print(f"{"움료":<10}\t{"금액":<4}\t{'수량':>3}\t{'소계':>4}\n")
    for i in range(len(beverage_Price_Amount)):
        price = beverage_Price_Amount[keys[i]][0]
        amount = beverage_Price_Amount[keys[i]][1]
        if amount != 0:
            print(f"{keys[i]:<15}\t{price:<4}\t{amount:>3}"
                  f"\t{price * amount:>10}\n")
    print(f"최종 금액 {total_Price}")

def print_Recipe():
    print(f"{"움료":<10}\t{"금액":<4}\t{'수량':>3}\t{'소계':>4}\n")
    for key,price_amount in beverage_Price_Amount.items():
        if price_amount[1] != 0:
            print(f"{key:<15}\t{price_amount[0]:<4}\t{price_amount[1]:>3}"
                  f"\t{price_amount[0] * price_amount[1]:>10}\n")
    print(f"최종 금액 {total_Price}")

while True:
    print_menu(keys)
    try:
        menu_num = int(input("메뉴를 입력하세요 : "))
    except:
        print("숫자를 입력해주세요")
        continue

    if 0 <= menu_num-1 >= (len(beverage_Price_Amount) + 2):
        print(f"{menu_num}은 존재하지 않는 메뉴입니다")
    elif menu_num == len(beverage_Price_Amount) + 1:
        print("주문확정")
        break
    else:
        select_menu(keys[menu_num-1])
print_Recipe()

