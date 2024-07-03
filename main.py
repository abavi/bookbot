def main():
    path_location = "books/frankenstein.txt"
    file_contents = open_file(path_location)
    
    # Count the number of words using len        
    words = file_contents.split()
    print(f"{len(words)} words found in the document!")
    print(f"The character count is: {count_characters(file_contents)}")

def open_file(path_to_location):
    with open(path_to_location) as f:
        return f.read()
    
def count_characters(file_contents):
    character_count = {} # Empty dict to count characters CHAR:COUNT

    words = file_contents.lower().split() # Create list of words

    # Loop through the words and then letters and add them to the dict
    for word in words:
        for letter in word:
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
    
    return character_count

main()