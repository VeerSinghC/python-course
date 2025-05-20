file = open('read.txt','r')
print(file.read())
file.close()

file = open('read.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('read.txt','a')
file.write("Hi! I am MUNIR and I am 1.5 years old")
file.close()   