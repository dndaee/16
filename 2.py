import nltk
import string
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

     nltk.download('stopwords')
nltk.download('wordnet')

text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do. 
Once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 
"and what is the use of a book," thought Alice "without pictures or conversation?"
"""

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

processed_tokens = []
for token in tokens:
    token = token.lower()
    if token in string.punctuation:
        continue
    if token in stopwords.words("english"):
        continue
    lemma = lemmatizer.lemmatize(token)
    stem = stemmer.stem(lemma)
    processed_tokens.append(stem)

filename = "processed_text.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(" ".join(processed_tokens))

print("\n Оброблений текст з файлу:")
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())
