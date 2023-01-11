from IPython.display import clear_output
import os
from replit import clear

# Import the languages module
import languages

# Set the TERM environment variable to "xterm"
os.environ["TERM"] = "xterm"

# Use a dictionary to map language names to languages lists
language = {
    "english": languages.english_alphabet,
    "bits": languages.english_alphabet_bits,
    "morse": languages.international_alphabet_morse
}


def translator(source_language, target_language, text_input):
    """Translate the text from one language to another"""
    # Initialize an empty list to store the translated text
    translated_text = []
    # Iterate through each character in the text to be translated
    for char in text_input:
        # Find the index of the character in the source language
        index = language[source_language].index(char)
        # Append the character in the target language at the same index to the translated text list
        translated_text.append(language[target_language][index])

    # Print the translated text
    print(f"Here is your translation:\n{' '.join(translated_text)}")


# Initialize a variable to control the loop
run_again = True

# Run the loop as long as run_again is True
while run_again:
    # Clear the screen
    clear_output()
    os.system("clear")
    clear()
    # Get the language to translate from and to
    # If the user inputs an invalid direction, continue to prompt them until they provide a valid input
    translate_from = input("Choice from what language to translate and type: 'English', 'Morse' or 'Bits'\n").lower()
    while translate_from not in language:
        translate_from = input("Invalid direction. Please type 'English', 'Morse' or 'Bits':\n")

    # Get the language to translate from and to
    # If the user inputs an invalid direction, continue to prompt them until they provide a valid input
    translate_to = input("Choice to what language to translate and type: 'English', 'Morse' or 'Bits'\n").lower()
    while translate_to not in language:
        translate_to = input("Invalid direction. Please type 'English', 'Morse' or 'Bits':\n")

    # Get the text to translate and convert it to lowercase
    text_to_translate = input('Write a text to translate\n').lower()

    # Call the translator function to translate the text
    translator(source_language=translate_from, target_language=translate_to, text_input=text_to_translate)

    # Prompt the user to choose whether to run the program again
    run_again = input("Would you like to translate something? Type 'Yes' or 'No'\n").lower()

    # If the user inputs an invalid response, continue to prompt them until they provide a valid input
    while run_again != 'yes' and run_again != 'no':
        run_again = input("Invalid input. Please type 'yes' or 'no':\n")

    # If the user chooses not to run the program again, set run_again to 'False' to exit the loop
    if run_again == "no":
        run_again = False
        print("Goodbye")
