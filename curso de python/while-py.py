def palindromo(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True

    return False    

def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True

    return False    

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindromo(word)

    if result is True:
        print('{} sí es un palindromo'.format(word))
    else:
        print('{} no es un palíndromo'.format(word))    