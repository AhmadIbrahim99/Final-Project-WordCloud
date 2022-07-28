import wordcloud
from matplotlib import pyplot as plt


with open("text.txt", 'r') as f:
    global file_contents
    file_contents = f.read()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    # LEARNER CODE START HERE
    freqs = {}
    words = file_contents.split()
    for word in words:
        letter = word.strip(punctuations)
        letter = letter.lower()
        if letter.isalpha() and letter not in uninteresting_words and letter not in freqs:
            freqs[letter] = 0
        else:
            continue
        freqs[letter] +=1

        
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(freqs)
    cloud.to_file(words[0]+"text.jpg")
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
