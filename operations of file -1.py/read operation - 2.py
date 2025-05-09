file_read = open('read.txt','r')
print("File in read mode")
print(file_read.read())
file_read.close()

file_write = open('read.txt','w')
file_write.write("Hi! I am MUNIR and I am 1.5 years old")
file_write.write("\nI am a goat")
file_write.close()

file_append = open('read.txt','a')
file_append.write("\nI am a lion")
file_append.write("\nI am a tiger")
file_append.close()