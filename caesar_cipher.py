#!/usr/bin/env python3

def get_shifted_alphabet(shift):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  shifted_alphabet = {}
  
  for idx, letter in enumerate(alphabet):
    shifted_alphabet[letter] = alphabet[idx - shift]

  return shifted_alphabet

def decrypt_text(encrypted_text, shift):
  shifted_alphabet = get_shifted_alphabet(shift)
  decrypted_text = ""

  for shifted_letter in encrypted_text:
    if shifted_letter == '.' or shifted_letter == ' ':
      decrypted_text += shifted_letter
    else:
      decrypted_text += shifted_alphabet[shifted_letter]

  print(decrypted_text)



encrypted_text = "VNWRWJ BQJAXW YXBBDR BJWPDN ANJU. YANLRBJVXB MNUJ YJAJ ANBBDBLRCJA X NGNALRCX MN VXACXB N RWRLRJA J MNBCADRLJX CXCJU MN OJBMJU."

decrypt_text(encrypted_text, 9)