MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ' ': '/'  # برای فاصله بین کلمات از / استفاده می‌کنیم
}

def text_to_morse(text):
    text = text.upper()
    morse_code = ""
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += '? '  # اگر کاراکتر ناشناس بود
    return morse_code.strip()

# مثال
user_input = input("لطفاً متن انگلیسی را وارد کنید: ")
morse_result = text_to_morse(user_input)
print("کد مورس:")
print(morse_result)
