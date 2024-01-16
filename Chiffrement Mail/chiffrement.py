
def encrypt_vigenere(plaintext, key):
    encrypted_text = ''
    key_length = len(key)
    
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            
            if char.isupper():
                encrypted_char = chr((ord(char) + key_shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) + key_shift - ord('a')) % 26 + ord('a'))
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    decrypted_text = ''
    key_length = len(key)
    
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            
            if char.isupper():
                decrypted_char = chr((ord(char) - key_shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - key_shift - ord('a')) % 26 + ord('a'))
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

# Exemple d'utilisation avec saisie utilisateur
if __name__ == "__main__":
    mode = input("Voulez-vous chiffrer (e) ou déchiffrer (d) ? ").lower()

    if mode == 'e':
        plaintext = input("Saisissez le texte à chiffrer : ")
        key = input("Saisissez la clé : ")
        result = encrypt_vigenere(plaintext, key)
        print(f"Texte chiffré : {result}")
    elif mode == 'd':
        ciphertext = input("Saisissez le texte à déchiffrer : ")
        key = input("Saisissez la clé : ")
        result = decrypt_vigenere(ciphertext, key)
        print(f"Texte déchiffré : {result}")
    else:
        print("Mode non reconnu. Veuillez choisir 'e' pour chiffrer ou 'd' pour déchiffrer.")
