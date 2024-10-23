numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


filtered_numbers = [num for num in numbers if num is not None]

#
sum_of_numbers = sum(filtered_numbers)
count_of_numbers = len(filtered_numbers)+1;


average_value = round(sum_of_numbers / count_of_numbers, 2)


for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average_value

# Выводим изменённый список
print("Измененный список:", numbers)

