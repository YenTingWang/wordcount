text = open('Building_Global_Community.txt').read()

norm_text = text.lower()

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
import string

stopwords.update(string.punctuation)
from nltk import wordpunct_tokenize

words = wordpunct_tokenize(norm_text)

filtered_words = [word for word in words if word not in stopwords if word.isalpha()]

from collections import Counter
counter = Counter(filtered_words)

for word, count in counter.most_common(20):
        print("%s: %d" % (word, count))
