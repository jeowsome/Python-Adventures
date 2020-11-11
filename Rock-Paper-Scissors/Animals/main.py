# read animals.txt
file_old = open('animals.txt', 'r')
file_new = open('animals_new.txt', 'w')

# and write animals_new.txt
for animal in file_old.readlines():
    file_new.write(animal.rstrip() + ' ')


file_old.close()
file_new.close()