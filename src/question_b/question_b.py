import random

def get_random_number():
    return random.randint(1,5)

def user_input():
    return int(input("Give me a number between 1 and 5: "))

def main():
    while True:
        random_number = get_random_number()
        lucky_draw = user_input()
        if lucky_draw == random_number:
            print("You got it!")
        else:
            print("NO!!! You lose.")
        
        try_again = input("Try again? (y/n): ").lower()
        if try_again != "y":
            print("You better guess correctly this time.")
            break

if __name__ == "__main__":
    main()

def test_get_random_number():
    for _ in range(5):
        random_number = get_random_number()
        assert 1 <= random_number <= 5, f"Your number is not in the range of 1 to 5."

test_get_random_number()
print("Looks good and fine.")