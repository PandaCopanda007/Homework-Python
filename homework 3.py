# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается 
# только одно слово, которое содержит либо только английские, либо только русские буквы.

# eng = 'qwertyuiopasdfghjklzxcvbnm'

# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
# list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}
# word = input('Введите слово на русском или английском языке: ')
# if word[0].lower() in eng:
#     summa = 0
#     for letter in word:
#         for key, value in list_English.items():
#             if letter.upper() in value:
#                 summa += key
#     print(summa)
# else:
#     if word[0].lower() in rus:
#         summa = 0
#         for letter in word:
#             for key, value in list_Russian.items():
#                 if letter.upper() in value:
#                     summa += key
#     print(summa)


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X



# length=int(input('Введите количество элементов списка:  '))
# import random
# lst = []
# for i in range(length):
#     lst.append(random.randint(1, 10))
# print(lst)

# x=int(input('Введите число:  '))
# count=0
# for i in range(length):
#     if lst[i] == x:
#        count+=1
# print(count)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# length=int(input('Введите количество элементов списка:  '))
# import random
# lst = []
# for i in range(length):
#     lst.append(random.randint(1, 10))
# print(lst)

# Flag=True
# x=int(input('Введите число:  '))
# for i in range(length):
#     while Flag:
#         if lst[i] == x + 1:
#             Flag=False
#             print(lst[i])
#         elif lst[i] == x-1:
#             Flag=False
#             print(lst[i])
#         elif lst[i] != x + 1 or lst[i] != x-1:
#             Flag=False
#             print("такого числа нет")
