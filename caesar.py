#this module encrypts the message the user enters

def encrypt (plain_message, offset):

    encrypted_message = ''

    #Encrypting the plain message
    for i in range(len(plain_message)):
        if plain_message[i] == ' ':
            encrypted_message += ' '
        else:
            encrypted_message += chr((ord(plain_message[i])-65 - offset)%26 + 65)

    return encrypted_message
#Decrypting the Message
def decrypt (encrypted_message, offset):

    decrypted_message = ''
    

    #Encrypting the plain message
    for i in range(len(encrypted_message)):
        if encrypted_message[i] == ' ':
            decrypted_message += ' '
        else:
            decrypted_message += chr((ord(encrypted_message[i])-65 + offset)%26 + 65)
            
    return decrypted_message
while True:
    #Welcome the User
    print('\nShhhhh! Welcome ! Enter Your Message to Be Encrypted\n'
            'Make Sure No Other Eyes Are Looking. Shhhhh!\n\n\n'
            'What Do You Want to Do:\n' 
            '1. Encrypt a Plain Message\n' 
            '2. Decrypt an Encrypted Message\n'
            '3. Quit\n')

    action_selection = input('Operation: ')

    if action_selection == '1':
        #Requesting for message to be encrypted
        plain_message = input('Your Plain Message to Be Encrypted, Here: ').upper()
        offset = int(input('Please Enter the Offset For the Encryption: '))
        print(encrypt(plain_message,offset))
        
    elif action_selection == '2':
        #Requesting for message to be decrypted
        encrypted_message = input('Your Encrypted Message to Be Decrypted, Here: ').upper()
        offset = int(input('Please Enter the Cipher Offset: '))
        print(decrypt(encrypted_message, offset))

        #Quit the program
    elif action_selection == '3':
        break
        
        #Wrong Input
    else:
        print('It Seems You Have Entered a Wrong Input, Try Again')
        continue