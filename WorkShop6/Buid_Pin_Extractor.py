# Completed Build a PIN Extractor as part 
# of my #freeCodeCamp journey! 🚀 Practiced Python string processing, functions, 
# and data extraction by building a program that identifies and extracts PIN codes.




def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
        poem = [poem, poem2, poem3]
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))

