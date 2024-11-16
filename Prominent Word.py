#take input from user
a = input(("Enter a sentence: "))
a = a.split()
Len = 0 #initialise

for wrd in a: #iterate loop
  wrdLen = len(wrd) #string operation
  if wrdLen>Len: #condition 1
    Len = wrdLen

print("\nLargest Word: ")
for wrd in a: 
  wrdLen = len(wrd)
  if wrdLen==Len: #condition 2
    print(wrd) #display result
