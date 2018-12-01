fw = open('sample.txt', 'w')
fw.write('This is naveen \n')
fw.write('This is semwal \n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
