from textblob import TextBlob
import nltk
nltk.download('punkt')

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.tags)