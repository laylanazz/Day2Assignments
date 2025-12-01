import sys

def main():

    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))

    print(f"The quotient is {a/b}")
    print(f"The integer quotient is {a//b}")
    print(f"The remainder is {a % b}")

if __name__ == "__main__":
    sys.exit(main())