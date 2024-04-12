# Assignment1

## Overview
This project consists of two parts designed to perform text processing on input files. The goal is to tokenize input texts, count word frequencoes, and compare text files to find the number of common tokens between them.

## Components
The project contains:
- **PartA.py**: Tokenizes input text files (tokenize(TextFilePath)), calculates (computeWordFrequencies(Token)) and prints (printFrequencies(wordCount)) the frequency of each token within an input file.
- **PartB.py**: Compares two input text files and calculates the number of tokens they have in common (countCommonTokens(file1, file2)).

## Usage
### Running PartA.py
To tokenize a file and print the frequencies of each token, navigate to your assignment1 directory and run in terminal:
    python3 PartA.py <TextFilePath>
    '<TextFilePath>' should be replaced with the path to the text file you want to process.

### Running PartB.py
To find the common tokens between two text files, run in terminal:
    python3 PartB.py <file1> <file2>
    Replace '<file1>' and '<file2>' with the paths to the two text files you want to compare.

## Time complexity
**PartA.py**:
- is_alphanumeric: O(1) - performs a constant time check for alphanumemric chars.
- tokenize: O(n):  Linear time complexity based on the num of tokens.
- printFrequencies: O(nlogn) - Sorts tokens based on frequency (and alphabetically for ties) in linear * log time.

**PartB.py**:
- countCommonTokens: O(n+m) - processes each file sequentially, making the time complexity linear to the size of both inputs

