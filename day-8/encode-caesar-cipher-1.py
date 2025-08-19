alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#To Do 1: create a function called 'encrypt()' that takes original_text and 'shift_amount' as 2 inputs 

direction = input(f"Type 'encode' to eccrypt, type 'decode' to decrypt:\n").lower()
text = input(f"Input your message: \n").lower()
shift = int(input(f"Type the shift number: \n"))



#To Do 2: Inside the 'encrypt()' shift the letter of the 'original_text' fowards in the alphabet by the shift amount and print encrypted test.
#To Do 3: Call the 'encrypt()' and pass in the user input .You should be able to test the code and encrypt a message 
#To Do 4: What happens if you try to shift z forwards by 9 ? can you fix the code ? 


def encryption(original_text, shift_amount):

    cipher_text = ""

    for letter in original_text:

        shifted_position = alphabet.index(letter) + shift_amount
           

    
   
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]

    print(f"Here is the cipher text : {cipher_text}")

encryption(original_text=text , shift_amount=shift)









