sentence = input('Enter a sentence: ')
sentence = sentence.split()

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range (len(sentence)):
    j = sentence[i]
    if j[0] in vowels:
        print (sentence[i] + 'way', end =' ')
    else:
        for k in range (len(j)):
            if j[k] in vowels:
                print (sentence[i][k:]+sentence[i][:k] + 'ay', end = ' ')
                break

print (' ')