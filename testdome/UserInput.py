### User Input


### 초기 오류 답안 ( add를 sum으로 이해 )
class TextInput:
    def __init__(self):
        self.value = 0

    def add(self, character):
        self.value += int(character)

    def get_value(self):
        return str(self.value)


### 수정 답안 ( add는 그냥 글자를 합하는 것)
class TextInput:
    def __init__(self):
        self.value = []

    def add(self, character):
        self.value.append(character)

    def get_value(self):
        return str("".join(self.value))


class NumericInput(TextInput):
    def add(self, character):
        if character.isdigit():
            self.value.append(character)
            # self.value += int(character)


if __name__ == "__main__":
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())
