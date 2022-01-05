import nltk,re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


text =['''Helloing worlds better d#$aaa  Helloing  one8 '''] # Sample query

# 1. Lower casing and sets
lower_text = []
def to_lower_case(search_query):
    for words in search_query:
        lower_text.append(str.lower(words))
    return lower_text

print("Lowered:",to_lower_case(text))


# 2. Tokenize
word_token = []
def to_word_token(lowered_text):
    for words in lowered_text:
        word_token.append(word_tokenize(words))
    return word_token


print("Tokenized:",to_word_token(lower_text))

word_token = list(set(word_token[0]))
print("set:",word_token)


# 3. Special character

clean_text=[]
def to_normalize(word_tokenized):
    for words in word_tokenized:
            res = re.sub(r'[^\w\s]',"",words)
            if res!="":
                clean_text.append(res)
    return clean_text

print("Removed Special char:",to_normalize(word_token))

# 4. Stopwords
semantic_words = []

def to_remove_stopwords(cleaned_text):
    for words in cleaned_text:
            if not words in stopwords.words('english'):
                semantic_words.append(words)
    return semantic_words

print("Removed Stopwords:",to_remove_stopwords(clean_text))

# 5. Stemming

port = PorterStemmer()
stemmed = []
def to_do_stemming(semantic_words_list):
    for words in semantic_words_list:
        stemmed.append(port.stem(words))
    return stemmed

print("Stemmed:",to_do_stemming(semantic_words))

# 6. Lemmatization
wnet = WordNetLemmatizer()
lemmatized = []
def to_do_lemmatizing(stemmed_list):
    for words in stemmed_list:
        lemmatized.append(wnet.lemmatize(words))
    return lemmatized

print("Lemmatized:",to_do_lemmatizing(stemmed))

