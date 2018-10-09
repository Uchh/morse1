class MorseDecoder:
    codes = {
        "._": "A",
        "_...": "B",
        "_._.": "C",
        "_..": "D",
        ".": "E",
        ".._.": "F",
        "__.": "G",
        "....": "H",
        "..": "I",
        ".___": "J",
        "_._": "K",
        "._..": "L",
        "__": "M",
        "_.": "N",
        "___": "O",
        ".__.": "P",
        "__._": "Q",
        "._.": "R",
        "...": "S",
        "_": "T",
        ".._": "U",
        "..._": "V",
        ".__": "W",
        "_.._": "X",
        "_.__": "Y",
        "__..": "Z"
    }

    def decode(self, cipher):
        for i in range(len(cipher)):
            if cipher[i].isalpha():
                return "ERROR - вы ввели букву? Пожалуйста, введите шифр\n"
            elif cipher[i].isalnum():
                return "ERROR - вы ввели цифру? Пожалуйста, введите шифр\n"
        otvets = ""
        otvet = ""
        for letter in cipher.split(" "):
            otvets += self.codes.get(letter)
        for i in range(len(otvets)):
            l1 = len(otvets)
            if l1 - i == 1:
                otvet += otvets[i]
            else:
                otvet += otvets[i] + " "
        return otvet


if __name__ == "__main__":
    decoder = MorseDecoder()
    p = 1
    while p == 1:
        print("Каждую букву в шифре(даже последнюю) отделять пробелом!\n")
        decoded_word = decoder.decode(input("Введите шифр для расшифровки:\n"))
        print(decoded_word)
        p = int(input("Повторить? 1 - да , 0 - нет\n")) #1