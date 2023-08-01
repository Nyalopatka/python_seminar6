def progressia(a,d,n):
    list1 =[]
    for i in range(n):
        list1.append(a + i * d)
    return list1




first_element = int(input("введите 1 элемент прогрессии: "))
difference = int(input("введите разность: "))
elements = int(input("введите кол-во элементов: "))
result = progressia(first_element,difference,elements)
print(result)