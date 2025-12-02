import sys

def main():

    x = float(input("Enter number: "))

    print(f"The square of the number is {x**2}")
    print(f"The cube of the number is {x**3}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
