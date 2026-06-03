# input= input("enter a sentecnce :")
# words=input.split()
# reverse_word=[word[::-1] for word in words]
# output=" ".join(reverse_word)
# print(output) 

input_words = ["Apple", "Banana", "Cherry", "Kiwi", "Apple"]
output_words = []

for word in input_words:
    if len(word) == 1:
        output_words.append(word)
    else:
        new_word = word[0].lower() + word[1:-1] + word[-1].upper()
        output_words.append(new_word)

print(output_words)
