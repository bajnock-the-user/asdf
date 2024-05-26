import re

def is_palindrome_and_unique_count(s):
    # Remove non-alphanumeric characters and convert to lower case
    filtered_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if it's a palindrome
    is_palindrome = filtered_str == filtered_str[::-1]
    # Get the number of unique alphanumeric characters
    unique_chars = set(filtered_str)
    unique_count = len(unique_chars)
    
    # Prepare the result
    if is_palindrome:
        return f"YES, {unique_count}"
    else:
        return "NO, -1" 

def main():
    # Read input from input.txt
    with open('./input.txt', 'r') as file:
        lines = file.read().splitlines()
    
    # Process each line
    results = [is_palindrome_and_unique_count(line) for line in lines]
    
    # Print results to console
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
