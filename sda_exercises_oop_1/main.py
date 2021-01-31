class Calculator:
    def __init__(self, type_calc='cisco'):
        self.type_calc = type_calc

    def show_calculator_type(self):
        print(f'calculator type: {self.type_calc}')
    @staticmethod
    def add_two_numbers(a: int, b:int) -> int:
        return a + b

def main():
    print(Calculator.add_two_numbers(2, 3))
    calculator = Calculator()
    calculator.show_calculator_type()
    print(calculator.add_two_numbers(2, 5))
if __name__ == "__main__":
    main()

