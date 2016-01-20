f = open('wordlist.txt', 'r')

count = 0
while(count < 10):
    line = f.readline()
    if len(line) == 4:
        print(line)
        count+=1
