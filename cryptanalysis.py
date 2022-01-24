import collections as cl


# Recieves the cyphertext and key of a vigenere encryption, and returns the plaintext that generated it.
def vigenere(text, key):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    j = 0
    for i in range(len(text)):
        if text[i] == ' ':
            plaintext += ' '
            j += 1
        else:
            plaintext += alph[alph.find(text[i]) - alph.find(key[(i-j)%len(key)])]
    return plaintext


# Returns a list of all 26 possibilities of a ceasar cipher
def caesar(text):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    array = [i + ': ' + vigenere(text, i) for i in alph]
    return array

# Recieves a plaintext and a key, and returns an encrypted ciphertext after applying the vigenere cipher
def encode(text, key):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    j = 0
    for i in range(len(text)):
        if text[i] == ' ':
            plaintext += ' '
            j += 1
        else:
            plaintext += alph[(alph.find(text[i]) + alph.find(key[(i-j)%len(key)]))%26]
    return plaintext


def changeLetters(text, ogLetters, newLetters):
    new_text = text
    for i in range(len(ogLetters)):
        new_text = new_text.replace(ogLetters[i].upper(), newLetters[i].lower())
    return new_text

# Returns the n most frequent letters of the text given and the number of times they appear in it
def freq(text, n):
    new_text = changeLetters(text, [' ', ',', ',', ';'], ['', '', '', ''])
    return (cl.Counter(new_text).most_common(n))


    

