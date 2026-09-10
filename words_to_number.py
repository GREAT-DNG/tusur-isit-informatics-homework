def words_to_number(text):
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19
    }

    tens = {
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
    }

    multiplers = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000
    }

    text = text.split() # pyright: ignore

    result = 0
    buffer = 0
    for i in range(len(text)):
        if text[i] in numbers:
            if buffer != 0:
                result += buffer
            buffer = numbers[text[i]]
        elif "-" in text[i]:
            places = text[i].split("-")
            buffer += tens[places[0]] + numbers[places[1]]
        elif text[i] in tens:
            buffer += tens[text[i]]
        elif text[i] in multiplers:
            buffer *= multiplers[text[i]]
    result += buffer
    return result

if __name__ == "__main__":
    print(words_to_number("seven hundred eighty-three thousand nine hundred and nineteen"))
