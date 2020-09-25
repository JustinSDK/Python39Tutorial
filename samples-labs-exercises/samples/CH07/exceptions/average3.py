total = 0
count = 0

while number_str := input('輸入數字（直接 Enter 結束）：'):
    try:
        number = int(number_str)
        total += number
        count += 1
    except ValueError as err:
        print('非整數的輸入', number_str)

print('平均', total / count)
