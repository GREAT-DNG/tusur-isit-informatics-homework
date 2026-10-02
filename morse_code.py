morse = dict((
('A', '.-'),
('B', '-...'),
('C', '-.-.'),
('D', '-..'),
('E', '.'),
('F', '..-.'),
('G', '--.'),
('H', '....'),
('I', '..'),
('J', '.---'),
('K', '-.-'),
('L', '.-..'),
('M', '--'),
('N', '-.'),
('O', '---'),
('P', '.--.'),
('Q', '--.-'),
('R', '.-.'),
('S', '...'),
('T', '-'),
('U', '..-'),
('V', '...-'),
('W', '.--'),
('X', '-..-'),
('Y', '-.--'),
('Z', '--..'),
('1', '.----'),
('2', '..---'),
('3', '...--'),
('4', '....-'),
('5', '.....'),
('6', '-....'),
('7', '--...'),
('8', '---..'),
('9', '----.'),
('0', '-----')))

morse_reversed = {code: letter for letter, code in morse.items()}

def to_morse(text):
    result = []
    for i in text:
        if i == " ":
            result.append("/")
        elif i in morse:
            result.append(morse[i])
    return " ".join(result)

def from_morse(code):
    code = code.split()
    result = []
    for i in code:
        if i == "/":
            result.append(" ")
        elif i in morse_reversed:
            result.append(morse_reversed[i])
    return "".join(result)
