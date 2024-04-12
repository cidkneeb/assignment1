import sys
import pathlib

#O(1)- This check if a char is alphanumeric is constant time because the "in" membership test on a string is O(1) time. 
def is_alphanumeric(char):
    '''Check if a character is alphanumeric'''
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9')

#O(n)- Linear time relative to the size of the input file. Reading lines, iterating characters, scale linearly
#with the size of the input text, where n is num of chars in file.
def tokenize(TextFilePath):
    '''Tokenize the text in the file.'''

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

#O(n) - Linear time, whre n is num of tokens. 
#The function iterates through the list of tokens and counts the frequency of each token.
def computeWordFrequencies(tokenList):
    """Counts the number of occurences of each token."""
    frequencies = {}
    for token in tokenList:
        if token in frequencies:
            frequencies[token] += 1
        else:
            frequencies[token] = 1
    return frequencies


#O(nlogn) - python's sorted function uses timsort which is O(nlogn) time complexity.
#The lambda function slightly adds to the computation, but it doesn't change the overall time complexity.
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