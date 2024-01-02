# --------Reverse Cipher algorithm-------- #
message = "Super Secure Message"
encrypted = ''  # Declared/Instantiated variable to hold finished crack
index = len(message) - 1  # Offset at the end of the string array, len = 42, last index = 41
while index >= 0:
    encrypted = encrypted + message[index]  # Start at the end, append to 'cracked'
    index = index - 1  # Increment the index backwards
print(f"Encrypted message: {encrypted}")

# Cracking just uses the same method, example:
cracked = ''
index = len(encrypted) - 1
while index >= 0:
    cracked = cracked + encrypted[index]  # Strings are nothing more than Array's of characters
    index = index - 1  # Increment the index backwards through the 'array'
print(f"Cracked message: {cracked}")
# --------Reverse Cipher algorithm-------- #
# --------Caesar cipher algorithm-------- #
message = "SuperSecureMessage"
shift = 4
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P,', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Caesar Cipher Encryption
def encrypt(raw_text, cipher_shift):
    encrypted_char = ""
    for index in range(len(raw_text)):
        char = raw_text[index]  # Get the character value of the specified index
        # print(char)  # Show the message via the assigned value from the index
        # print(f"Original {char} Unicode #: {ord(char)}") # Show the unicode hex value
        if char.isupper():
            # encrypted_char = chr((ord(char) + 32))  # Convert to lowercase
            encrypted_char += chr((ord(char) + cipher_shift - 65) % 26 + 65)  # 65 is unicode 'A'
            # 97-lower #65-upper
        else:
            encrypted_char += chr((ord(char) + cipher_shift - 97) % 26 + 97)  # 97 is unicode 'a'
    return encrypted_char


print("Caesar cipher demo")
print(f"Plain text: {message}")
print(f"Shift Pattern: {shift}")
print(f"Cipher: {encrypt(message, shift)}")
print(chr(52))

encrypted_message = "WytivWigyviQiwweki"
# Cracking Caesar cipher
for key in range(len(letters_list)):
    cracked = ''
    # print(key)
    for letter in encrypted_message:
        if letter in letters_list:
            index = letters_list.index(letter)
            index = index - key  # Key is acting as the shifter going reverse against the 'array'
            if index < 0:
                index = index + len(letters_list[index])
            # print(f"Letter {letter}, Index: {index}")
            cracked = cracked + letters_list[index]
        else:
            cracked = cracked + letter
        if ',' in cracked:
            cracked = cracked.replace(',', '')
    print(f"Reverse Iteration #{key}: {cracked}")
# --------Caesar cipher algorithm-------- #
# --------ROT13 (Caesar cipher 13 rotate)-------- #
# Rotate 13 is just the caesar cipher with a 13 shift, using a string table will produce the same result
# The algorithm above would achieve the same result too
text = "hello"
grab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rep = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
replaced = text.translate(str.maketrans(grab, rep))
print(replaced)

# --------ROT13 (Caesar cipher 13 rotate)-------- #
# --------Transposition cipher algorithm-------- #

key_text = 'HACK'

"""
Key values are sorted by their decimal values
Columns = 4
Rows = 5
=================
| A | C | H | K |
=================
| S | u | p | e |
| r | S | e | c |
| u | r | e | M |
| e | s | s | a |
| g | e | - | - |
=================
"""


def encrypt(message):
    cipher_text = ''
    key_indexes = 0
    message_length = len(message)
    message_list = list(message)
    key_list = sorted(list(key_text))
    # Columns of Matrix
    columns = len(key_text)  # Length of the encryption key
    rows = round(int(message_length / columns), 0)  # generate the rows by the encryption key
    #  Take the rows and columns minus the total message to get the remaining leftover spaces
    fill_null = int((rows * columns) - message_length)  # '-' inverses to a positive number for the list-list
    if fill_null < 0:  # Validate if the remaining spaces are negative, inverses it
        fill_null = -fill_null
    # Adds empty characters to the table to make it even, remainder was 4.5, this rounds it to 5
    message_list.extend('*' * fill_null)

    print(f"Fill Null: {fill_null}")
    print(f"Key list: {key_list}")
    print(f"Message Length: {message_length}")
    print(f"Message List: {message_list}")
    # Matrix/Table creation
    # Takes the slice index to index and then add the offset (4) to get the record
    # iterates like this 0, 4, 8, 12, 16
    matrix = []
    for index in range(0, len(message_list), columns):
        temp_list = message_list[index:index + columns]  # Store slice in temp list 0-4, 5-8, etc
        matrix.append(temp_list)  # Appends the slice results to separate lists in the matrix list
        # print(matrix)
    # This is the list compression version of the same for loop
    # matrix = [message_list[index:index + columns] for index in range(0, len(message_list), columns)]

    # Read values column wise, not row wise
    for i in range(columns):
        current_index = key_text.index(key_list[key_indexes])
        for row in matrix:
            temp = row[current_index]
            cipher_text = cipher_text + temp
        key_indexes += 1

    print(f"Matrix: {matrix}")
    print(f"Cipher Text: {cipher_text}")


def decrypt(cipher):
    key = 'HACK'
    decrypted_message = ''
    key_index = 0  # Matrix incrementation

    # Matrix indices
    message_index = 0
    message_length = len(cipher)
    message_list = list(cipher)

    # Calculate columns of matrix
    columns = len(key)
    # Calculate rows of the matrix
    rows = round(int(message_length / columns), 0)

    # Make Key into list, alphabetically
    key_list = sorted(list(key))

    # Create local Matrix for decryption
    # Builds with no values, just sets the structure
    decryption_cipher = []
    for index in range(rows):
        decryption_cipher = decryption_cipher + [[None] * columns]  # Make a list under the main list for the columns
    # print(decryption_cipher)

    # Set Matrix column wise based on the
    # permutation order by adding values into the new matrix
    for column_iter in range(columns):
        column_index = key.index(key_list[key_index])
        for row_index in range(rows):
            decryption_cipher[row_index][column_index] = message_list[message_index]
            message_index += 1  # Increment the message list iterator
        key_index += 1  # Increment the column index by the key
    print(f"Matrix: {decryption_cipher}")

    # Convert the decrypted message matrix into a string value
    # Using a nested for-loop to extract values from matrix
    decrypted_message = ''
    for values in range(len(decryption_cipher)):
        for value in decryption_cipher[values]:
            # print(value)
            if value == '*' or value == '_':
                pass
            else:
                decrypted_message = decrypted_message + value
    print(decrypted_message)


message = "SuperSecureMessage"  # Spaces will be place with '*'
encrypted_message = "uSrsepees*SruegecMa*"
encrypt(message)
decrypt(encrypted_message)

# --------Transposition cipher algorithm-------- #
# --------File Encryption-------- #
import optparse
# --------File Encryption-------- #
