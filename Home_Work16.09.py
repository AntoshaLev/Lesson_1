#Задание 1


duration = int(input("Введите количество секунд: "))

s = duration % 60
m = duration // 60 % 60
h = duration // 3600 % 24
d = duration // 86400


print(d, "дн", h, 'час', m, 'мин', s, 'сек')



#Задание 2

arr = [num ** 3 for num in range(1, 1001, 2)]

final_sum = 0
for num in arr:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num

arr = [num ** 3 for num in range(1, 1001, 2)]
final_sum1 = 0
for num in arr:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum1 += num
print(final_sum)
print(final_sum1)


#Задание 3
numbs = {11, 12, 13, 14}
for i in range(100):
    i = i + 1
    if i in numbs:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif 1 < i % 10 < 5:
        print(i, "процента")
    else:
        print(i, "процентов")
