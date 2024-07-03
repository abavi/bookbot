def main():
    path_location = "books/frankenstein.txt"
    file_contents = open_file(path_location)
    
    # Count the number of words using len        
    words = file_contents.split()
    print(f"{len(words)} words found in the document!")

def open_file(path_to_location):
    with open(path_to_location) as f:
        return f.read()

main()