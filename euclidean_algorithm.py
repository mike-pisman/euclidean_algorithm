def gcf(a, b):
    return b if a == 0 else gcf(b % a, a)

def gcf2(a, b):
    if a == 0:
        return b, 0, 1

    gcf, x1, y1 = gcf2(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcf, x, y

def get_number(s):
    while True:
        a = input(s)
        if a.isdigit():
            return int(a)

def main():
    while True:
        print("\nWhich program to run?\nc",
              "1) Euclidean Algorithm",
              "2) Diophantine Equation",
              "3) Exit", sep = "\n")
        choice = input("> ")

        if choice == "1" or choice.lower() == "simple gcd":
            a = get_number("\na = ")
            b = get_number("b = ")
            print("Greates common factor of {} and {} is {} \n".format(a, b, gcf(a, b)))
        elif choice == "2" or choice.lower() == "extended gcd":
            a = get_number("\na = ")
            b = get_number("b = ")
            print("Diophantine Equation of {0} and {1} is {0}*{3} + {1}*{4} = {2} \n".format(a, b, *gcf2(a, b)), end="\n")
        elif choice == "3" or choice.lower() == "exit":
            break
        else:
            print("\nWrong entry, please enter 1, 2, or 3")

if __name__ == "__main__":
    main()
