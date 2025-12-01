import sys

def main():

    x = 10
    x+=2
    print(f"Sum : {x}")
    x-=4
    print(f"Difference : {x}")
    x**=3
    print(f"Power : {x}")

if __name__ == "__main__":
    sys.exit(main())