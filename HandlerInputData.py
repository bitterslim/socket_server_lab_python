from random import randint
class HandlerInputData():
    def __init__(self) -> None:
        self.numbersEnteredString = " "

        


    def string_to_numbers(self, numbersStr: str):
        return list(map(int, numbersStr.split(" ")))

    def generate_numbers(self, numbers):
        numbers = []
        while True:
            number = randint(0, 10)
            isNumberExists = False
            if len(numbers) > 3:
                break
            else:
                for i in numbers:
                    if i == number:
                        isNumberExists = True
            if isNumberExists == False:
                numbers.append(number)   
        return numbers
    
    def compare_input_and_generated_data(self, numbers, numbersEntered):
        bulls, cows = [], []
        for i in range(len(numbersEntered)):
            if numbers[i] == numbersEntered[i]:
                bulls.append(i)
            elif numbersEntered[i] in numbers:
                cows.append(i)
        print(f"Bulls: {bulls}\nCows: {cows}")     

    def test(self):
        self.numbersEnteredString = input("Введите 4 числа через пробел \n")
        numbersGenerated = self.generate_numbers(6)
        numbersEntered = self.string_to_numbers(self.numbersEnteredString)
        print('numbersGenerated', numbersGenerated)
        print('numbersEntered',numbersEntered)
        result = self.compare_input_and_generated_data(numbersGenerated, numbersEntered)
        print(result)

handler = HandlerInputData()
handler.test()
