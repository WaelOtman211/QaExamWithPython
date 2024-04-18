def get_words_longer_than(input_string, min_length):
    """
    Retrieves words from a string with length greater than a given value.

    Args:
        input_string (str): The input string containing words.
        min_length (int): The minimum length of words to be included in the result.

    Returns:
        list: A list of words from the input string that have a length greater than 'min_length'.
    """
    words = input_string.split()  # Split the input string into a list of words
    result = []  # Initialize an empty list to store words with length greater than 'min_length'
    for word in words:
        if len(word) > min_length:  # Check if the length of the word is greater than 'min_length'
            result.append(word)  # If yes, add the word to the result list
    return result


def is_palindrome(input_string):
    """
    Checks if a string is a palindrome.

    Args:
        input_string (str): The input string to check.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    for i in range(int(len(input_string) / 2)):
        if input_string[i] != input_string[len(input_string) - i - 1]:
            return False
    return True


def find_palindromes_in_list(str_list):
    """
    Finds palindromes in a list of strings.

    Args:
        str_list (list): A list of strings.

    Returns:
        list: A list of palindromes found in the input list.
    """
    result = []
    for string in str_list:
        if is_palindrome(string):
            result.append(string)
    return result


def main():
    # Example 1:
    min_length = 3
    input_string = "The quick brown fox jumps over the lazy dog"
    print("Words with length longer than:", min_length)
    print(get_words_longer_than(input_string, min_length))
    print("---------------------------")

    # Example 2:
    check_list = {"sheep", "xenex", "cow"}
    print("List of palindrome words:")
    print(find_palindromes_in_list(check_list))
    print("---------------------------")

    word = "cow"
    print("Is '" + word + "' a palindrome?")
    print(is_palindrome(word))


if __name__ == "__main__":
    main()
     