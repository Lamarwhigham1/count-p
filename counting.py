'''
Created on Feb 3, 2018

@author: ITAUser
'''
'''

f = open("poem.txt", "r")
#print(f.read())
print(f.readline())
text = f.read()
words =text.split()
print(words)
print(len(words))
f.close

f.read(())
'''
'''
fw = open("new.txt", "w")
fw.write("pineapples DOES go on pizza!")
'''
filename = "constituton.txt"
numberfile = open("constituton.txt", "r+")

numberwords = 0;
numberchar = 0
for line in numberfile:   
    
    words = line.split(); 
    numberwords = len(words)+ numberwords;
    for word in words:
        word.count("p") 

        numberchar = word.count("p") + numberchar;
print(numberchar);

    
    