with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am Donald Trump ")
file.close()

with open('Codingal.txt', 'r') as file:
    data = file.read()
    print("Words in the file are....")
    for line in data:
        word = line.split()
        print(word)
file.close()
