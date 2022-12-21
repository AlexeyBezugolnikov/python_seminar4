# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
path1 = '1.txt'
str = []
data1 = open('1.txt', 'r')
str = data1.readline().split()

print(str)
data1.close()

# path2 = '2.txt'
data2 = open('2.txt', 'r')
str2 = data2.readline().split()
print(str2)
data2.close()
data3 = open('3.txt', 'w')
data3.writelines(str(int(str[0]) + int(str2[0])))
# str3 = []
#
# str3[0] = (int(str[0]) + int(str2[0]))



