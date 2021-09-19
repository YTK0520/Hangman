#!/usr/bin/env python
# coding: utf-8


# In[2]:


import random
import time
print("Introduction:\nAll the words will be related to animals.\nYou are suppose to guess a character at a time and there is only 20 guesses for each word.")
print("Hint: start guessing with a/e/i/o/u.")
time.sleep(0.5)
word_list=["human species", "horse", "sloth", "snake", "rat", "bear", "penguin", "starfish", "fish", "squarel"]
n=random.randint(0,9)
word=word_list[n]
words=word.split(' ')
print(f"There are {len(words)} word(s).\n")
num_char=[]
space=[]
correct_lis=[]
total=0
for i in range(0,len(words)):
    word_char=list(words[i])
    num_char.append(str(len(word_char)))
    print(f"The No.{i+1} word has {len(word_char)} characters.")
    total+=len(word_char)

for m in range(0,len(num_char)):
    space.append("_ "*int(num_char[m]))
print("Word: "+"  ".join(space)+"\n")

characters=list(word)
correct_lis=["_"]*len(list(word))
for b in range(0, len(list(word))):
    if list(word)[b]==" ":
        correct_lis[b]=" "
    else:
        pass
for c in range(0,20):
    ans=str(input("Please guess a letter: "))
    for a in range(0,len(characters)):
        if characters[a]==ans:
            correct_lis[a]=ans
        else:
            pass
    print(" ".join(correct_lis))
    if correct_lis==characters:
        print("Congratulations! You got the right answer!")
        break
    else: 
        pass

print(f"The correct answer: {word}")

