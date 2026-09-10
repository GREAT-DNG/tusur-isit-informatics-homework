def to_jaden_case(text: str) -> str:
    jadenized = []
    for word in text.split():
        jadenized.append(word[0].upper() + word[1:])
    return " ".join(jadenized)

if __name__ == "__main__":
    print(to_jaden_case("How can mirrors be real bla bla bla"))
