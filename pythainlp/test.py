# Import Counter
from collections import Counter
from pythainlp.tokenize import word_tokenize,Tokenizer
#Read TXT file
f = open("lexitron.txt", "r")
article = f.read()
tokens =word_tokenize(article)
print(tokens)
