alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cipher_text=[]
def encrypt(tap_text, shift_amount):
  global cipher_text
  for letter in tap_text:
   position=alphabet.index(letter)
   new_position=position+shift_amount
   new_letter=alphabet[new_position]
   cipher_text+= new_letter

print(f"The encoded text is {cipher_text}")
encrypt(tap_text=text, shift_amount=shift)
