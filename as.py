def length_of_last_word(s: str) -> int:
    s = s.rstrip()
    last_space_index = s.rfind(' ')
    return len(s) - last_space_index - 1

if __name__ == "__main__":
    input_string = input("Please enter a string: ")
    result = length_of_last_word(input_string)
    print(f"The length of the last word is: {result}")

