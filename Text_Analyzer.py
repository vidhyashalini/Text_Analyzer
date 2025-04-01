def text_analyzer(text):
    print("\nText Analysis Results:")
    print("---------------------")
    print(f"Total Characters: {len(text)}")
    print(f"Total Words: {len(text.split())}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title Case: {text.title()}")
    print(f"Reversed Text: {text[::-1]}")
    
    # Checking if the text is a palindrome
    cleaned_text = text.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    if cleaned_text == cleaned_text[::-1]:
        print("Palindrome Check: Yes, it's a palindrome!")
    else:
        print("Palindrome Check: No, it's not a palindrome.")

if __name__ == "__main__":
    user_text = input("Enter a text for analysis: ")
    text_analyzer(user_text)
