import sys
import pathlib

#runtime complexity explanation
def is_alphanumeric(char):
    '''Check if a character is alphanumeric'''
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9')

def tokenize(TextFilePath):
    '''Write a method/function that reads in a text file and returns a list of the tokens in that file. For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, apple, aPpLe are the same token). You are NOT allowed to use regular expressions (DO NOT USE THE re library), you are not allowed to import a tokenizer (e.g. from NLTK), since you are being asked to write a tokenizer.'''
    # Check if the file exists
    if not pathlib.Path(TextFilePath).is_file():
        print("File does not exist")
        sys.exit(1)
    # Read the file
    with open(TextFilePath, 'r') as file:
        # Read the file
        text = file.read()
        # Tokenize the text
        tokens = []
        token = ""
        for char in text:
            if is_alphanumeric(char):
                token += char
            else:
                if token:
                    tokens.append(token.lower())
                    token = ""
        if token:
            tokens.append(token.lower())
    return tokens

#runtime complexity explanation
def computeWordFrequencies(tokenList):
    """Counts the number of occurences of each token."""
    frequencies = {}
    for token in tokenList:
        if token in frequencies:
            frequencies[token] += 1
        else:
            frequencies[token] = 1
    return frequencies


#runtime complexity explanation
def printFrequencies(wordCount):
    """Prints word frequency count in descending order. Tie breaker is alphabetical."""
    for token, count in sorted(wordCount.items(), key = lambda item: (-item[1], item[0])):
        print(f"{token} -> {count}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tokenizer.py <TextFilePath>")
        sys.exit(1)
    # Get the path of the file
    TextFilePath = sys.argv[1]
    # Tokenize the file
    tokenList = tokenize(TextFilePath)
    # Compute the word frequencies
    wordCount = computeWordFrequencies(tokenList)
    # Print the word frequencies
    printFrequencies(wordCount)