from utils import add, divide

def main():
    print("Program started...")  # змінений текст
    print("Starting program...")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("Sum:", add(a, b))
    print("Divide:" , divide(a, b))
    print("Calculation done")
    print("end program")
if __name__ == "__main__":
    main()