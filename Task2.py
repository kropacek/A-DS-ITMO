import codecs
import docx
import time
special_symbhols = ['.', ',', ':', '\n', '-', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', '-', '«', '»', '—', '  ']

# len = triplet.__len__()
def get_text() -> str:
    file = docx.Document('Научный метод.docx')
    text = []
    for i in file.paragraphs:
        text.append(i.text)
    return ' '.join(text)

start = time.time()
text = get_text().lower()  # Получаем просто текст
# Подготавливаем текст, для того чтобы просто брать по три слова и сравнивать  с тем, что имеем
for i in special_symbhols:
    while i in text:
        if i == '  ':
            text = text.replace(i, ' ')
        else:
            text = text.replace(i, '')



words = text.split(' ') # Выделим слова которые имеются в тексте
triplets = { }
text_char = text.__len__()
for i in range(len(words) - 3):
    triplets[' '.join(words[i: i+3])] = 0

with codecs.open('text_1.txt', 'r', 'utf_8_sig') as f:
    text = ''
    for i in f:
        text += i
text.lower()
for i in special_symbhols:
    if i == ' ':
        text = text.replace(i, ' ')
    else:
        text = text.replace(i, '')
words = text.split(' ')
plagiat_triplets = []
for i in range(len(words) - 3):
    plagiat_triplets.append(' '.join(words[i:i+3]))

for i in plagiat_triplets:
    if i in triplets:
        triplets[i] += 1

print(sum(i.__len__() for i in triplets if triplets.get(i) != 0 ) / text_char * 100 )

print(triplets)







print(time.time() - start)


