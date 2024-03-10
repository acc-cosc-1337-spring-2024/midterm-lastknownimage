def reversed_string(string1):
    reversed_string = ''
    index = len(string1) - 1
    while index >= 0:
        reversed_string += string1[index]
        index -= 1
    return reversed_string
    
def main():
    while True:
        user_input = input("Enter 'Hello world' or type 'exit' to leave.")
        if user_input.lower() == 'exit':
            print("Exiting.")
            break
        reversed_input = reversed_string(user_input)
        print("Reversed:", reversed_input)

if __name__ == "__main__":
    main()
        