import sys
import pathlib

#O(1)- This check if a char is alphanumeric is constant time because the "in" test on a string takes O(1) time. 
def is_alphanumeric(char):
    '''Check if a character is alphanumeric'''
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or (char >= '0' and char <= '9')

#O(n)- linear time relative to the size of the input file. Reading lines, iterating characters, scale linearly
#with the size of the input text, where n is num of chars in file.
def tokenize(TextFilePath):
    '''Tokenize the text in the file.'''
    # Check if file exists
    if not pathlib.Path(TextFilePath).is_file(): 
        print("File does not exist")
        sys.exit(1)
    # Read the file
    with open(TextFilePath, 'r') as file:
        text = file.read()
        # Tokenize the text
        tokens = [] #O(1)
        token = "" #O(1)
        for char in text: #O(n)
            if is_alphanumeric(char): #O(1)
                token += char #O(1)
            else: 
                if token: #O(1)
                    tokens.append(token.lower()) #O(1)
                    token = "" #O(1)
        if token: #O(1)
            tokens.append(token.lower()) #O(1)
    return tokens

#O(n) - linear time, whre n is num of tokens. 
#The function iterates through the list of tokens and counts the frequency of each token.
def computeWordFrequencies(tokenList):
    """Counts the number of occurences of each token."""
    frequencies = {} #O(1)
    for token in tokenList: #O(n)
        if token in frequencies: #O(1)
            frequencies[token] += 1
        else: 
            frequencies[token] = 1 #O(1)
    return frequencies 


#O(nlogn) - python's sorted function uses timsort which is O(nlogn) time complexity.
#The lambda function slightly adds to the computation, but it doesn't change the overall time complexity.
def printFrequencies(wordCount):
    """Prints word frequency count in descending order. Tie breaker is alphabetical."""
    for token, count in sorted(wordCount.items(), key = lambda item: (-item[1], item[0])): #O(nlogn)
        print(f"{token} -> {count}") #O(1)


if __name__ == "__main__":
    #perform argument checks
    if len(sys.argv) != 2:
        print("Usage: python3 tokenizer.py <TextFilePath>")
        sys.exit(1)
    #get the path of the file
    TextFilePath = sys.argv[1]
    #tokenize the file
    tokenList = tokenize(TextFilePath)
    #compute the word frequencies
    wordCount = computeWordFrequencies(tokenList)
    #print the word frequencies
    printFrequencies(wordCount)