from nltk import word_tokenize
from nltk.tokenize import TweetTokenizer

tweet = '@Hari: This sounds good! :D'
print(word_tokenize(tweet))
print(TweetTokenizer().tokenize(tweet))

