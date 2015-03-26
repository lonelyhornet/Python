text_file = open("read_it.txt", "r")
text_file.close()

text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()