# Morse code translator
import string


# English to Morse code
def english_to_morse(message):
    # Morse code dictionary
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
        '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }

    # initialize an empty string
    morse_message = ""

    # loop through the message
    for letter in message:
        if letter != " ":
            # get the morse code for the letter
            morse_message += morse_code[letter.upper()] + " "
        else:
            morse_message += " "

    return morse_message

# Morse code


# Morse code to English
def morse_to_english(message):
    # Morse code dictionary
    morse_code = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
        "-----": "0", "--..--": ",", ".-.-.-": ".", "..--..": "?",
        "-..-.": "/", "-....-": "-", "-.--.": "(", "-.--.-": ")"
    }

    english_message = ""
    words = message.split("   ")
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            english_message += morse_code[letter]
        english_message += " "
    return english_message.strip()


def is_morse_code(message):
    valid_morse_code = set('.- ')
    message_set = set(message)
    if message_set.issubset(valid_morse_code):
        return True
    else:
        return False


print('This program is a morse code translator which can translate both morse code to English and vice-versa.')
message = input("Please write your text in English or morse code:\n")
if is_morse_code(message):
    print(morse_to_english(message))
else:
    print(english_to_morse(message))
