words = set()
for word in open("word list.txt", 'r'):
    word=word.lower().strip()
    #print(word,len(word.strip()))
    if len(word.strip()) == 5: words.add(word)# To remove '/n' at the end of the word.
import pickle
print(words)
pickle.dump(words,open('words list.dat','wb'))
