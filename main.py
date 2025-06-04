word = 'Brazil'
chances = 10
GueseAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GueseAdd:
            print(letter, end = " ")
        else:
            print(" ", end = "")
    myGuese = input(f"your changes Is{chances}, Guese The Letter: ")
    GueseAdd.append(myGuese.lower())
    if myGuese.lower() not in word.lower():
        chances = chances - 1
        if chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in GueseAdd:
            done = False
if done:
    print(f"yes, you have won the game, the word is {word} ")