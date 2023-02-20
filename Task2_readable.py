import docx
import codecs
import time
import wikipedia

special_symbhols = ['.', ',', ':', '\n', '-', ')', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '0',
                    ';', '(', '-', '«', '»', '—',
                    '  ', '–', '|', '<ref>', 'en', 'i', "'''" ]  # Определяем символы для удаления для адекватной проверки слов в тексте


def get_text(file_name: str, wiki=False) -> str:
    if wiki:
        wikipedia.set_lang('ru')
        return delete_special_symbols(wikipedia.page(file_name).content)
    if '.docx' in file_name:
        file = docx.Document(file_name)
        text = []
        for i in file.paragraphs:
            text.append(i.text)
        return delete_special_symbols(' '.join(text).lower())
    else:
        with codecs.open(file_name, 'r', 'utf_8_sig') as f:
            text = ''
            for i in f:
                text += i
        return delete_special_symbols(text.lower())


def delete_special_symbols(text: str) -> str: # можно оптимизировать проверяя ord(i) в радиусе, чтоб не вызывать for :)
    for i in special_symbhols:
        if i == '  ':
            text = text.replace(i, ' ')  # Если встретился двойной пробел
        elif i == '\n':
            text = text.replace(i, ' ')
        else:
            text = text.replace(i, '')

    return text


def triplets_from_words(text: str, return_dict=True) -> dict | list:
    words = text.split(' ')  # Получаем слова из текста
    return {' '.join(words[i:i + 3]): 0 for i in range(len(words) - 3)} if return_dict == True else [
        ' '.join(words[i:i + 3]) for i in range(len(words) - 3)]  # Возвращаем триплеты слов


def find_plagiat(check_text: str, text: str) -> float:
    check_text_triplets = triplets_from_words(check_text)
    text_triplets = triplets_from_words(text, return_dict=False)
    for i in text_triplets:
        # Проходимся по возможным триплетам слов, которые получились в проверяемом и исходном
        if i in check_text_triplets:
            check_text_triplets[i] += 1

    # print(check_text_triplets)
    return (sum(
        i.__len__() for i in check_text_triplets if
        check_text_triplets.get(i) != 0) / sum(list(map(lambda d: d.__len__(), check_text_triplets)))) * 100


def main():
    '''
    Данная реализация использует метод хэширования, так как из-за использовании словарей
    мы косвенно используем хэш-значение когда обращаемся к ключу элемента.
    :return:
    '''
    start = time.time()
    print(find_plagiat(get_text('Научный метод.docx'), get_text('Научный метод', wiki=True)), "%")
    print(delete_special_symbols(get_text('Научный метод', wiki=True)))
    print(f'Затрачено времени: {time.time()-start}')


if __name__ == '__main__':
    main()
