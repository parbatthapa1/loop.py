user=(input('enter a word:'))
vowels_found=set()
vowels='a','e','i','o','u'
for i in user.lower():
    if i in vowels:
        vowels_found.add(i)
print('unique vowels found:',vowels_found)
print('total number of vowels:',len(vowels_found))

import random

quiz_questions = {
    "q1": {
        "question": "What is the capital of Nepal?",
        "options": {"A": "Pokhara", "B": "Kathmandu", "C": "Lalitpur", "D": "Biratnagar"},
        "answer": "B"
    },
    "q2": {
        "question": "Which language is used for web development?",
        "options": {"A": "Python", "B": "HTML", "C": "C", "D": "Java"},
        "answer": "B"
    },
    "q3": {
        "question": "What is 2 + 2?",
        "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
        "answer": "B"
    }
}

score = 0
keys = list(quiz_questions.keys())
random.shuffle(keys)

for key in keys:
    q = quiz_questions[key]
    print("\n" + q["question"])

    for opt, val in q["options"].items():
        print(opt, ":", val)

    user_ans = input("Enter your answer (A/B/C/D): ").upper()

    if user_ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nFinal Score:", score)

dictionary={}
unique_word=set()
user_input=int(input('how many words do you want to add:'))
for i in range(1,user_input+1):
    choice=int(input('press 1. add 2. display 3. remove 4. exit'))
    if choice==1:
        word=input('enter a word')
        if word in unique_word:
            print(f'{word} already exists')
        else:
            meaning=input('enter the meaning of the word:')
            dictionary[word]=meaning
            unique_word.add(word)
    elif choice==2:
        for i,j in dictionary.items():
            print(i,' ',j)
    elif choice==3:
       word=input('enter a word you want to remove')
       if word not in unique_word:
           print(f'{word} doesnot exists') 
       else:
           dictionary.pop(word)
           unique_word.remove(word)
    else:
        break
print(unique_word)
n = int(input("Enter number of items: "))

prices = []

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    prices.append(price)

total = sum(prices)

print("Total cost:", total)

sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set()

for word in words:
    unique_words.add(word.lower())

print("Total number of words:", len(words))
print("Number of unique words:", len(unique_words))

sentence = input("Enter a sentence: ")

words = sentence.split()
freq = {}

for word in words:
    word = word.lower()
    freq[word] = freq.get(word, 0) + 1

for word in sorted(freq):
    print(f"{word}: {freq[word]}")
