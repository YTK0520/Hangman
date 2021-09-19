#!/usr/bin/env python
# coding: utf-8

# In[39]:


import random
import time
print("Introduction:\nAll the words will be related to animals.\nYou are suppose to guess a character at a time and there is only 15 guesses for each word.")
print("Hint: start guessing with a/e/i/o/u.")
time.sleep(0.5)
word_list=["human", "horse", "sloth", "snake", "rat", "bear", "penguin", "starfish", "fish", "squarel"]
n=random.randint(0,9)
word=word_list[n]
words=word.split(' ')
print(f"There are {len(words)} word(s).\n")

for i in range(0,len(words)):
    word_char=list(words[i])
    print(f"The No.{i+1} word has {len(word_char)} characters.")
    print("Word: "+"_ "*len(word_char)+"\n")
    correct_lis=["_"]*len(word_char)
    for c in range(0,15):
        ans=str(input("Please guess a letter: "))
        for a in range(0,len(word_char)):
            if word_char[a]==ans:
                correct_lis[a]=ans
            else:
                pass
        print(" ".join(correct_lis))
        if correct_lis==word_char:
            print("Congratulations! You got the right answer!")
            break
        else: 
            pass

print(f"The correct answer: {word}")

