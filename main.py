def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # Count the number of words using len        
        words = file_contents.split()
        print(f"{len(words)} words found in the document!")
                
main()