sentence = "hello hii "
words = sentence.split()
print(words)
output = {}

for word in words:
    output[word] = words.count(word)

print(output)

# in this split method split sentence in list like word wise and that store in words variable and that use for loop for count 
# word in this output[word] will be key and other side thing is value in int.