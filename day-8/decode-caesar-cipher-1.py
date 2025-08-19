alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#To Do 1: create a function called 'encrypt()' that takes original_text and 'shift_amount' as 2 inputs 

direction = input(f"Type 'encode' to eccrypt, type 'decode' to decrypt:\n").lower()
text = input(f"Input your message: \n").lower()
shift = int(input(f"Type the shift number: \n"))

#To Do 2: Decode the value 

# encode function 

cipher_text = ""


def encryption(original_text, shift_amount):
    
    for letter in original_text:

        shifted_position = alphabet.index(letter) + shift_amount
            
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the cipher text : {cipher_text}")



# decode function 

def decryption (original_text, shift_amount):

    decode_text = ""

    for letter in original_text:

        shifted_postion = alphabet.index(letter) - shift_amount
        decode_text += alphabet[shifted_postion]

    print(f"the decrypt value is : {decode_text}")

decryption(original_text=text , shift_amount=shift)






