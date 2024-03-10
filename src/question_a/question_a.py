def reverse_string(string1):
    reverse_string = ' '
    index = len(string1) - 1

    while index >= 0:
        reverse_string += string1[index]
        index -= 1

    return reverse_string

#write functions here, don't add input('') statements here!
def test_config():
    return True

def test_reverse_string():
    tests = [
        ("Hello world", "dlrow olleH"),
        ("Hello", "olleH"),
    ]
    for input_str, expected_ouput in tests:
        result = reverse_string(input_str)
        assert result == expected_ouput, "Didn't work for input '{}'. Looking for '{}', got '{} instead.".format(input_str, expected_ouput, result)
        # The next part will look for the issue.
        if result != expected_ouput:
            print("That didn't work. Output was something unexpected.")
            print(f"I wanted '{expected_ouput}', but I got '{result}'")
        else:
            print("Looks fine.")

test_reverse_string()