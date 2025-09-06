from core.calculator import Calculator

def main():
    calc = Calculator()
    while True:
        expr = input("Enter expression (or 'quit'): ")
        if expr.lower() == "quit":
            break
        try:
            result = calc.calculate(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
