fin = open("sample2.txt", "a")

fin.write('\nThis is newly appended text.')

fin.close()

fin2 = open("sample2.txt", "r")

print(fin2.read())