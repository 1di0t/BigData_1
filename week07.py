#
beverage = ['Espresso', 'Compagina', 'Lemonade']
prices = [2000, 2500, 3900]
total_Price = 0
quantity = [0, 0, 0]


def select_menu(menu_num):
    """
    Print selected menu and increase quantity, totalPrice
    :param menu_num:
    :return: none
    """
    global total_Price
    print(f"{beverage[menu_num]} 주문완료")
    quantity[menu_num] += 1
    total_Price += prices[menu_num]


while True:
    for i in range(len(beverage)):
        print(f"{i + 1}) {beverage[i]} : {prices[i]} \n")
    menu_num = int(input(f"{len(beverage) + 1}) exit\n 메뉴를 입력하세요 : "))

    if menu_num == len(beverage) + 1:
        print("주문확정")
        break
    else:
        select_menu(menu_num-1)

print(f"움료\t가격\t수량\t{'소계':>6}\n")
for i in range(len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\t{prices[i]}\t{quantity[i]}\t{prices[i] * quantity[i]:>6}\n")
print(f"최종 금액 {total_Price}")
