from random import randint
def search_index(list1,min_num,max_num):
    for i in range(len(list1)):
        if min_num <= list1[i] <= max_num:
            print(i)

n = int(input("введите колво элементов списка: "))
list1_min = int(input("введите минимальное число в списке: "))
list1_max = int(input("введите максималтное число в списке: "))
min_num = int(input("введите минимум для диапозона: "))
max_num = int(input("введите максимум для диапозона: "))
my_list = list(randint(list1_min,list1_max) for i in range(n+1))
print(search_index(my_list,min_num,max_num))