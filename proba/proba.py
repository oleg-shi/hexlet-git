a = int(input())
b = int(input())
c = a + b
print(c)

with open('log.txt', 'a') as file:
    file.write(str(c) + '\n')

input('Для выхода нажмите Enter')

