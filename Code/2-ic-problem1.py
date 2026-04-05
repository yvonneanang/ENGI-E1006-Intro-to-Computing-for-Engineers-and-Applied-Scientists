# In Class Set 2 - Problem 1
#submitted by Yvonne Naa Ardua Anang 
#collaborated with Joseph Duodu

#part 1
def piggify(word):
    vowels ="aeiou"
    if word[0] in vowels:
        piggified = word + "yay"
    
    elif word[0] not in vowels:
        for letter in word:
            if letter in vowels:
                index_of_letter = word.find(letter)
                spliced_consonant = (word[:index_of_letter])
                spliced_vowel = (word[index_of_letter:])
                piggified = spliced_vowel + spliced_consonant + "ay"
                break
            if letter not in vowels:
                piggified = word + "ay"
    return piggified

#part 2
while True:
    word = input("Please enter a word:>>>")
    if word != ".":
        answer = piggify(word)
        print (answer)

    if word == ".":
        break
    



    
