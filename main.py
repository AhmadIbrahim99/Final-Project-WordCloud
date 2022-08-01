from codecs import unicode_escape_decode
import wordcloud
from matplotlib import pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
import json
import codecs




with open("Quran-Simple.txt", "r", encoding='utf-8') as f:
    global file_contents
    file_contents = arabic_reshaper.reshape(f.read())

def printTXT(fre):
    with codecs.open("Quran.txt", "w", encoding='utf-8') as f:
        f.write(json.dumps(fre,ensure_ascii=False))

def printletters(letters):
    with codecs.open("QuranLetters.txt", "w", encoding='utf-8') as f:
        f.write(json.dumps(letters,ensure_ascii=False))

        

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do","those", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    # LEARNER CODE START HERE
    freqs = {}
    letters = {}
    words = file_contents.split()
    for word in words:
        letter = word.strip(punctuations)
        letter = letter.lower()
        if letter.isalpha() and letter not in uninteresting_words and letter not in freqs:
            freqs[letter] = 1
            for le in letter:
                if le not in letters:
                    letters[le] = 1
        elif letter in freqs:
            
             freqs[letter] +=1
             for le in letter:
                if le in letters:
                    letters[le] += 1
             

        
    #wordcloud
    printletters(letters)
    printTXT(freqs)
    cloud = wordcloud.WordCloud(font_path='arial',background_color='white', mode='RGB',width=2000,height=1000)
    cloud.generate_from_frequencies(letters)
    cloud.to_file("quranletters.jpg")
    return cloud.to_array()


# print(file_contents)
myimage = calculate_frequencies(file_contents)
plt.title("By Ahmad Ibrahim")
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
