alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#To Do 1: create a function called 'encrypt()' that takes original_text and 'shift_amount' as 2 inputs 

direction = input(f"Type 'encode' to eccrypt, type 'decode' to decrypt:\n").lower()
text = input(f"Input your message: \n").lower()
shift = int(input(f"Type the shift number: \n"))



#To Do 2: if the direction is decode then it should decode only 

## combine the encrypt function and decrypt function in one function called 'ceaser'

def encryption(original_text, shift_amount, encode_or_decode):

    cipher_text=""

    for letter in original_text:

        if encode_or_decode == "decode":

            shift_amount *= -1

        shifted_positon = alphabet.index(letter) + shift_amount
        shifted_positon %= len(alphabet)

        cipher_text += alphabet[shifted_positon]

    print(f"the value is {encode_or_decode}d : {cipher_text}")


encryption(original_text=text , shift_amount=shift , encode_or_decode=direction)




    




