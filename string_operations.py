def reverse_string(string):
    return string[::-1]


def capitalize(string):
    return string.capitalize()


def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)
