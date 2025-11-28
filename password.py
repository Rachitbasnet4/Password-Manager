""" 
A utility class for generating secure, randomized passwords.

    This class generates passwords using a combination of uppercase and
    lowercase letters, numbers, and special characters. The number of each
    character type included in the password is randomized to increase entropy.

    Attributes:
        letters (list): A list of lowercase and uppercase alphabet characters.
        numbers (list): A list of numeric characters (0-9).
        symbols (list): A list of common special characters used in passwords.
"""
import random

class PasswordGenerator:
    """ 
    Generate and return a randomized password string.

        The password is constructed using:
            - 8 to 10 random letters
            - 2 to 5 random symbols
            - 2 to 5 random numbers

        Characters are selected randomly from predefined character pools and
        then shuffled to ensure the final password has no predictable pattern.

        Returns:
            str: A secure randomly generated password string.
    """
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def generate(self):
        """Generate a random password"""
        nr_letter = random.randint(8, 10)
        nr_symbols = random.randint(2, 5)
        nr_numbers = random.randint(2, 5)

        password_list = []

        for _ in range(nr_letter):
            password_list.append(random.choice(self.letters))
        for _ in range(nr_symbols):
            password_list.append(random.choice(self.symbols))
        for _ in range(nr_numbers):
            password_list.append(random.choice(self.numbers))


        random.shuffle(password_list)
        password_str = "".join(password_list)
        return password_str


# generator = PasswordGenerator()
# PASS = generator.generate()
# print(f"Your generated password is: {PASS}")
