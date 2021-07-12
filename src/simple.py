import hashlib


with open('contract', 'rb') as file1:
    f1 = file1.read()
    h = hashlib.md5(f1).hexdigest()
    print("Хеш файла1: ", h)

# вносим изменения в файл contarct добавляем ('westen')

line = repr(input('введи слово: '))
with open('contract', 'ab') as file2:
    file2.write(line.encode('utf-8'))

with open('contract', 'rb') as file3:
    f3 = file3.read()
    h2 = hashlib.md5(f3).hexdigest()
    print("Хеш файла2: ", h2)
