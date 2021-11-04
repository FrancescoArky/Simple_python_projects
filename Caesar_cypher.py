should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  

    def caesar(direction = direction, plain_text = text, shift_amount = shift):

        def encrypt(plain_text, shift_amount):
            text = ""
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    if position + shift_amount >= len(alphabet):
                        x = (position + shift_amount) % len(alphabet)
                        letter2 = alphabet[x]
                        print(letter2, "letter2 first case")
                    else:
                        letter2 = alphabet[alphabet.index(letter) + shift_amount]
                        print(letter2, "letter2 second case")
                else:
                    letter2 = letter
                text = text + letter2
            print(text, "textprinted")

        def decrypt(plain_text, shift_amount):
            decipher_text = ""
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    if position - shift_amount < 0:
                        letter2 = alphabet[len(alphabet) - abs((position - shift_amount))]
                        print(letter2, "letter2 first case")
                    else:
                        letter2 = alphabet[alphabet.index(letter) - shift_amount]
                        print(letter2, "letter2 second case")
                else:
                    letter2 = letter
                decipher_text = decipher_text + letter2
            print(decipher_text, "textprinted")

        if direction == "encode":
            encrypt(plain_text=text, shift_amount=shift)
        elif direction == "decode":
            decrypt(plain_text=text, shift_amount=shift)

    caesar(direction=direction, plain_text=text, shift_amount=shift)
    
    inputend = input('do you want to start the program again?')
    if inputend == 'yes':
        should_continue = True
    elif inputend == 'no':
        should_continue = False
        print("program stopped")
