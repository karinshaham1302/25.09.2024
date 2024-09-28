#start

list_num: list[int] = []
SENTINEL: int = -999
while True:
    number: int = int(input('enter a number between 1-10:'))
    if number == -999:
        break
    if not 0 <= number <= 10:
        continue
    num_counter: int = 0
    list_num.append(number)
    for digit in list_num:
        if digit == number:
            num_counter += 1
    print(f'statistics:', [number], ':',num_counter)

#stop

