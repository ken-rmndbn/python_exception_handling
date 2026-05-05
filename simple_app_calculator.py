class MathOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide number by zero!")
        return a / b

class SimpleAppCalculator(MathOperations):
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0M"

    def get_number(self, prompt):
        while True:
            try:
                return float(input(f"{self.YELLOW}{prompt}{self.RESET}"))
            except ValueError:
                print(f"{self.RED}Invalid input! Please enter a number.{self.RESET}")