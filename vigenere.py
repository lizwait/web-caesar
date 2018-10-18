def alphabet_position(letter):
    uppercaseLetter = letter.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return(alpha.find(uppercaseLetter))

def rotate_character(char, rot):
    position = alphabet_position(char)
    if position == -1:
        return (char)     
    new_pos = (position + rot) % 26
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    if uppercase.find(char) == -1:
        return (lowercase[new_pos])
    else:
        return (uppercase[new_pos])

def vigenere(text, key):
    rot_key = []
    for letter in key:
        rot_key.append (alphabet_position(letter))
    new_string = ""
    counter = 0 
    for letter in text:
        if alphabet_position(letter) == -1:
            new_string += letter 
        else:
            index = counter % len(rot_key)
            new_string += rotate_character(letter, rot_key[index])
            counter += 1
    return(new_string)

def main():
    if __name__ == "__main__":
        main()
    text = input("Type a message:")
    key = input("Encryption key:")
    print(vigenere(text, key))  