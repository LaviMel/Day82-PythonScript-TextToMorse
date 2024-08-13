morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}
reversed_morse_code = {v: k for k, v in morse_code.items()}


def text_to_morse(text):
    words = text.split()
    message = []
    for word in words:
        list_word = list(word)
        decoded_word = '   '.join(morse_code[letter] for letter in list_word)
        message.append(decoded_word)
    return '       '.join(message)


def morse_to_text(morse):
    words = morse.split('       ')  # Split the code between each word using the 7 spaces
    message = []
    for word in words:
        letters = word.split('   ')
        decoded_word = ''.join(reversed_morse_code[letter] for letter in letters)
        message.append(decoded_word)
    return ' '.join(message)


number = input("If you'd like to translate text-to-morse, enter 1. If you'd like to translate morse-to-text, enter 2. ")

if number != '1' and number != '2':  # Minimal error handling
    print("Input is invalid. Please try again.")
else:
    sentence = input("\nEnter the text you'd like to translate: ")
    if number == '1':
        morse_text = text_to_morse(sentence.upper())
        print(f"Your translation is: {morse_text}")
    elif number == '2':
        morse_text = morse_to_text(sentence)
        print(f"Your translation is: {morse_text}")