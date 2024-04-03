import random
def get_random_number():
    return random.randint(1,5)
def user_input():
    return int(input("Give me a number between 1 and 5: "))
def main():
    while True:
        print("I want to play a game.")
        while True:
            random_number = get_random_number()
            lucky_draw = user_input()
            if lucky_draw == random_number:
                print("You got it right!")
                break
            else:
                print("BUZZ! WRONG!")
        try_again = input("Would you like to play a game? (y/n) ")
        if try_again != "y":
            print("Disappointing.")
            break
if __name__ == "__main__":
    main()