def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Keep non-alphabet characters unchanged
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# --- User Input ---
def main():
    print("Caesar Cipher Program")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'e':
        encrypted = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
