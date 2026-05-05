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

    def run(self):
        print(f"{self.YELLOW}Simple App Calculator{self.RESET}")

        while True:
            print("\nChoose an Operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            user_choice = input(f"{self.YELLOW}Enter choice (1/2/3/4): {self.RESET}")

            if user_choice in ("1", "2", "3", "4"):
                number_1 = self.get_number("Enter First Number: ")
                number_2 = self.get_number("Enter Second Number: ")
                