from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm


def ask_user(text, warning_text, func, type=float):
    while True:
        try:
            n = input(text)
            if not func(n):
                raise ValueError
            break
        except ValueError:
            print(warning_text)
    return type(n)


print("Functions:")
print(" - fact - factorial of number")
print(" - exp2 - square of number")
print(" - exp3 - cube of number")
print(" - root2 - square root of number")
print(" - root3 - cube root of number")
print(" - log - logarithm of number to base")
print(" - ln - natural logarithm of number")
print(" - lg - decimal logarithm of number")
while True:
    choice = input("Enter a function to use: ")
    try:
        if choice == 'fact':
            n = ask_user("Enter a number: ", "You have to enter an integer.", lambda x: int(x) >= 0, int)
            print(f"Factorial of {n} is {factorial.fact(n)}")
        elif choice == 'exp2':
            n = ask_user("Enter a number: ", "You have to enter a number.", lambda x: float(x))
            print(f"Square of {n} is {exponentiation.exp2(n)}")
        elif choice == 'exp3':
            n = ask_user("Enter a number: ", "You have to enter a number.", lambda x: float(x))
            print(f"Cube of {n} is {exponentiation.exp3(n)}")
        elif choice == 'root2':
            n = ask_user("Enter a number: ", "You have to enter a number >= 0.", lambda x: float(x) >= 0)
            print(f"Square root of {n} is {root.root2(n)}")
        elif choice == 'root3':
            n = ask_user("Enter a number: ", "You have to enter a number.", lambda x: float(x))
            print(f"Cube root of {n} is {root.root3(n)}")
        elif choice == 'log':
            a = ask_user("Enter a logarithm base: ", "You have to enter a positive number different from 1.",
                         lambda x: float(x) > 0 and float(x) != 1)
            b = ask_user("Enter a number: ", "You have to enter a positive number.", lambda x: float(x) > 0)
            print(f"Logarithm of {b} to {a} is {logarithm.log(a, b)}")
        elif choice == 'ln':
            b = ask_user("Enter a number: ", "You have to enter a positive number.", lambda x: float(x) > 0)
            print(f"Natural logarithm of {b} is {logarithm.ln(b)}")
        elif choice == 'lg':
            b = ask_user("Enter a number: ", "You have to enter a positive number.", lambda x: float(x) > 0)
            print(f"Decimal logarithm of {b} is {logarithm.lg(b)}")
        else:
            raise ValueError
        print("Happy New Year. Please level up my grades :)")
        break
    except ValueError:
        print("You have to enter one of offered function.")


if __name__ == '__init__':
    main()
