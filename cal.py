class CustomAdvancedCalculator:
    def __init__(self):
        self.history = []
        # Defining PI manually since we cannot import math
        self.PI = 3.141592653589793
        self.E = 2.718281828459045

    def add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")
        if len(self.history) > 10:
            self.history.pop(0)

    # --- Basic Operations ---
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, base, exponent):
        # Handles integer exponents directly; returns float approximations for simplicity
        try:
            return base ** exponent
        except ZeroDivisionError:
            raise ValueError("0 cannot be raised to a negative power.")

    # --- Advanced Implementations From Scratch ---
    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        if x == 0:
            return 0.0
        
        # Newton-Raphson approximation method
        guess = x / 2.0
        for _ in range(50):  # 50 iterations provides extreme accuracy
            guess = 0.5 * (guess + x / guess)
        return guess

    def ln(self, x):
        """Calculates natural logarithm using Taylor series expansion."""
        if x <= 0:
            raise ValueError("Logarithm undefined for values less than or equal to zero.")
        
        # Argument reduction to make the Taylor series converge quickly
        count = 0
        while x > 1.5:
            x /= self.E
            count += 1
        while x < 0.5:
            x *= self.E
            count -= 1
            
        # Taylor series for ln(1 + z) where z = x - 1
        z = x - 1.0
        total = 0.0
        term = z
        for i in range(1, 100): # 100 terms for fine accuracy
            total += term / i
            term = -term * z
            
        return total + count

    def log(self, x, base=None):
        if base is None:
            base = self.E
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be greater than 0 and not equal to 1.")
        
        # Change of base formula: log_b(x) = ln(x) / ln(b)
        return self.ln(x) / self.ln(base)

    # --- Trigonometric Functions From Scratch ---
    def _abs(self, x):
        return -x if x < 0 else x

    def sin(self, deg):
        # Convert degrees to radians manually
        rad = deg * (self.PI / 180.0)
        
        # Bring angle within -2PI to 2PI range
        two_pi = 2 * self.PI
        rad = rad - int(rad / two_pi) * two_pi
        
        # Taylor series expansion for sin(x)
        total = 0.0
        term = rad
        sign = 1
        for i in range(1, 30, 2):  # 1, 3, 5, 7...
            total += sign * term
            # Compute next term sequentially to avoid large factorial calculations
            term = term * rad * rad / ((i + 1) * (i + 2))
            sign = -sign
        return total

    def cos(self, deg):
        # Rely on the identity: cos(x) = sin(x + 90)
        return self.sin(deg + 90.0)

    def tan(self, deg):
        c = self.cos(deg)
        # Handle division by zero where cos(x) approaches 0 (e.g., 90°, 270°)
        if self._abs(c) < 1e-10:
            raise ValueError("Tangent is undefined for this angle.")
        return self.sin(deg) / c


def print_menu():
    print("\n=== Pure Python Advanced Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square Root (√x)")
    print("7. Logarithm")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. View History")
    print("12. Exit")

def main():
    calc = CustomAdvancedCalculator()
    
    while True:
        print_menu()
        choice = input("\nSelect an operation (1-12): ").strip()

        if choice == '12':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice == '11':
            print("\n--- Recent History ---")
            if not calc.history:
                print("No calculations recorded yet.")
            for record in calc.history:
                print(record)
            continue

        try:
            # Functions taking single numeric values
            if choice in ['6', '8', '9', '10']:
                val = float(input("Enter number: "))
                if choice == '6':
                    res = calc.square_root(val)
                    calc.add_to_history(f"√{val}", res)
                elif choice == '8':
                    res = calc.sin(val)
                    calc.add_to_history(f"sin({val}°)", res)
                elif choice == '9':
                    res = calc.cos(val)
                    calc.add_to_history(f"cos({val}°)", res)
                elif choice == '10':
                    res = calc.tan(val)
                    calc.add_to_history(f"tan({val}°)", res)
                
            # Functions taking dual numeric values
            elif choice in ['1', '2', '3', '4', '5', '7']:
                num1 = float(input("Enter first number: "))
                
                if choice == '7':
                    base_input = input("Enter base (Leave blank for natural log 'e'): ").strip()
                    base = None if base_input == "" else float(base_input)
                    res = calc.log(num1, base)
                    display_base = "e" if base is None else base
                    calc.add_to_history(f"log_{display_base}({num1})", res)
                else:
                    num2 = float(input("Enter second number: "))
                    if choice == '1':
                        res = calc.add(num1, num2)
                        calc.add_to_history(f"{num1} + {num2}", res)
                    elif choice == '2':
                        res = calc.subtract(num1, num2)
                        calc.add_to_history(f"{num1} - {num2}", res)
                    elif choice == '3':
                        res = calc.multiply(num1, num2)
                        calc.add_to_history(f"{num1} * {num2}", res)
                    elif choice == '4':
                        res = calc.divide(num1, num2)
                        calc.add_to_history(f"{num1} / {num2}", res)
                    elif choice == '5':
                        res = calc.power(num1, num2)
                        calc.add_to_history(f"{num1} ^ {num2}", res)
            else:
                print("Invalid choice! Please select an operation from 1 to 12.")
                continue

            print(f"\nResult: {res}")

        except ValueError as e:
            print(f"\nMath Error: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
	
