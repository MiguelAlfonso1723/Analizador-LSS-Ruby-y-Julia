import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

tokens = ['PRUEBA', 'NOMBRE']

t_PRUEBA = word_tokenize(str(tokens[1]))

print(t_PRUEBA)




