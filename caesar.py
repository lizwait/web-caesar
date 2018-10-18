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

def caesar(text, rot):
    new_string = ""
    for letter in text:
        new_string += rotate_character(letter, rot)
    return(new_string)

def main():
    if __name__ == "__main__":
        main()
    text = input("Type a message:")
    rot = int(input("Rotate by:"))
    print(caesar(text, rot))