# start

temperatures: list[float] = []
SENTINEL: int = -999
while True:
    temperature: float = float(input('enter a temp:'))
    if temperature == -999:
        break
    if not -50 <= temperature <= 50:
        continue
    temperatures.append(temperature)
print('list_temp', temperatures)
print(temperatures.extend([-20.0, 39.1, 18.5]))

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1 + list2 = [1, 2, 3, 4, 5, 6] ---> new list
# list1.extend(list2) = None         ---> list1 = [1, 2, 3, 4, 5, 6]
#                                        list2 = [4, 5, 6]

print('max temp', max(temperatures))
print('min temp', min(temperatures))
print('18.5 in the list?', 18.5 in temperatures)
print('count(-20.0)', temperatures.count(-20.0))
print('the len:', len(temperatures))
print('sum:', sum(temperatures))

for temperature in temperatures:
    print(f'{temperature}', end=' ')
print('index (39.1)', temperatures.index(39.1))
del temperatures[0]
print(f'new list without del:{temperatures}')
del temperatures[::2]
print(f'the new second list without del[2]:,{temperatures}')

while temperatures == 18.5:
    temperatures.remove(18.5)
print('after remove the number 18.5', temperatures)
# אם לא בודקים לפני, התוכנית תקרוס

temp_last: float = temperatures.pop()
print(f'temp last:{temp_last}')

temp2 = temperatures.copy()
temp2.sort()
print('after sort:', temp2)

temp3 = temperatures.copy()
temp3.sort(reverse=True)
print('after sort reverse:', temp3)

# stop
