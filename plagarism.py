import re

# Function to tokenize text into words
def tokenize(text):
    text = text.lower()
    words = re.findall(r'\w+', text)
    return set(words)

# Function to calculate Jaccard Similarity between two sets
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union

# Function to check for plagiarism
def check_plagiarism(text1, text2, threshold=0.5):
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    
    similarity = jaccard_similarity(tokens1, tokens2)
    
    if similarity >= threshold:
        return f"Plagiarism detected! Similarity: {similarity:.2f}"
    else:
        return "No plagiarism detected."

if __name__ == "__main__":
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")
    
    plagiarism_result = check_plagiarism(text1, text2)
    
    print(plagiarism_result)
