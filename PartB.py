import sys
import PartA as part_a

#O(n+m) - n is num of tokens in file 1, m is num in file 2.
#the func reads and processes each file sequentially, making time complexity
#linear to the size of the inputs.
def countCommonTokens(file1_path, file2_path):
    """Count the number of common tokens between two files."""
    #tokenize firsy file and store in set for o(1) lookup
    file1_tokens = set(part_a.tokenize(file1_path)) #O(n)

    #init common token counter
    num_common = 0 #O(1)

    #tokenize second file and check for common
    for token in part_a.tokenize(file2_path): #O(m)
        if token in file1_tokens: #O(1)
            num_common += 1
            #remove token from file1_tokens so no double counting
            file1_tokens.remove(token) #O(1)
    return num_common #O(1)

if __name__ == "__main__":
    #perform argument checks 
    if len(sys.argv) != 3:
        print("Usage: python PartB.py <file1> <file2>")
        sys.exit(1)
    # read in files
    file1_path, file2_path = sys.argv[1], sys.argv[2]
    common_tokens_count = countCommonTokens(file1_path, file2_path)
    print("Number of common tokens:", common_tokens_count)

