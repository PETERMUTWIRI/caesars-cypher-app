### Caesar Cipher App

This is a simple command-line application that encrypts and decrypts messages using the Caesar cipher algorithm.
### How to Use

    Clone this repository to your local machine.
    Navigate to the project directory in your terminal.
    Run python caesar_cipher.py.
    Follow the prompts to either encrypt or decrypt a message.
    Enter the shift value (an integer between 1 and 25) when prompted.
    Enter the message you wish to encrypt or decrypt.
    The encrypted or decrypted message will be displayed in the console.

### How it Works

The Caesar cipher is a substitution cipher that works by shifting the letters of the alphabet a certain number of places down the alphabet. For example, with a shift value of 3, "A" would be replaced by "D", "B" would become "E", and so on.

The application takes in a shift value and a message from the user. If the user chooses to encrypt the message, each letter in the message is shifted forward in the alphabet by the given shift value. If the user chooses to decrypt the message, each letter in the message is shifted backwards in the alphabet by the given shift value.

If a letter is shifted past the end of the alphabet, it wraps around to the beginning of the alphabet. For example, with a shift value of 3, "X" would become "A".
### Dependencies

This application was written in Python 3.8. It does not have any external dependencies.
