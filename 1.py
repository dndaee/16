import matplotlib.pyplot as plt
from collections import Counter
import string
import requests
import os

filename = "bible-kjv.txt"
if not os.path.exists(filename):
print("Файл не знайдено. Завантаження з інтернету...")
url = "https://www.gutenberg.org/files/10/10-0.txt"
response = requests.get(url)
with open(filename, "w", encoding="utf-8") as f:
f.write(response.text)
print("Файл збережено як", filename)

with open(filename, "r", encoding="utf-8") as file:
text = file.read()

words = text.split()
print("Кількість слів у тексті:", len(words))

word_counts = Counter(words)
top_words = word_counts.most_common(10)

words_, counts = zip(*top_words)
plt.figure(figsize=(10, 5))
plt.bar(words_, counts, color='skyblue')
plt.title("10 найбільш вживаних слів (без фільтрації)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_raw_bible.png")
plt.show()

stop_words = {
"the", "and", "to", "of", "a", "i", "it", "in", "was", "that", "you", "is",
"he", "she", "for", "on", "with", "as", "his", "at", "had", "be", "but",
"not", "her", "they", "this", "my", "me", "or", "so", "what", "all", "them",
"their", "unto", "which", "shall", "him", "from", "by", "ye", "thou"

punctuation = set(string.punctuation)

filtered_words = [
word.lower().strip(string.punctuation)
for word in words
if word.lower() not in stop_words and word.isalpha()
]

filtered_counts = Counter(filtered_words)
top_filtered = filtered_counts.most_common(10)

words_, counts = zip(*top_filtered)
plt.figure(figsize=(10, 5))
plt.bar(words_, counts, color='orange')
plt.title("10 найбільш вживаних слів (після фільтрації)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_filtered_bible.png")
plt.show()

