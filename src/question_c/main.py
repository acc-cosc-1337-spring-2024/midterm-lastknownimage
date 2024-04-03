def get_person_type(person_age):
    if person_age < 0:
        return "Invalid. You haven't even been born yet."
    if person_age > 125:
        return "Invalid. Gravestone."
    elif person_age <= 1:
        return "Infant."
    elif person_age < 13:
        return "Child."
    elif person_age < 20:
        return "Teenager."
    else:
        return "Adult."

def main():
    while True:
        try:
            number = int(input("Give a person's age. You can type 'DONE' to exit: "))
            if number <= 0:
                print("The person hasn't been born yet and I won't accept this answer.", "Try again.")
                continue
            elif number > 125:
                print("This person is too old to be alive and I won't accept this answer.", "Try again.")
                continue
            else:
                type = get_person_type(number)
                print(f"This person is a/an {type}")
        except ValueError:
            user_input = input("I won't accept this answer. Enter 'DONE' to leave. Otherwise, hit enter.")
            if user_input.lower() == 'DONE':
                break

if __name__ == "__main__":
    main()