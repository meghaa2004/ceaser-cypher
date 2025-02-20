def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher with the specified shift
    """
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            ascii_base = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_base + shift) % 26
            encrypted_text += chr(shifted + ascii_base)
        else:
            encrypted_text += char
            
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    """
    Decrypts text encrypted with Caesar Cipher using the specified shift
    """
    return caesar_encrypt(encrypted_text, -shift)

def main():
    # Get user choice for encryption or decryption
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt? [E/D]: ").upper()
        if choice in ['E', 'D']:
            break
        print("Please enter 'E' for encrypt or 'D' for decrypt")

    # Get message and shift value
    message = input("Enter the message: ")
    shift_value = int(input("Enter shift value: "))
    
    # Process based on user choice
    if choice == 'E':
        # Encryption
        result = caesar_encrypt(message, shift_value)
        print(f"\nOriginal message: {message}")
        print(f"Encrypted message: {result}")
    else:
        # Decryption
        result = caesar_decrypt(message, shift_value)
        print(f"\nEncrypted message: {message}")
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
