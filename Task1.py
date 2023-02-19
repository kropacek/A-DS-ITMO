nums = []


def naive(nums: str, prelocate_dict=False) -> dict:  # Самый крутой додуманный алгоритм близкий к наивному
    '''Асимпототика данного алгоритма равна как O(len(nums)*(len(nums)-len(pattern)). В нашем случае можно принять как O(n^2) и как бы не крута'''
    '''Вообще даный алгорим является Рабина-Карпа, тк в словарях используется метод хэширования'''
    len_of_pattern = 2  # Ищем двузначные числа
    if prelocate_dict == False:
        res = {}
    else:
        res = {}
        for i in range(10, 100):
            res[f'{i}'] = 0
    for i in range(len(nums) - len_of_pattern):
        elem = nums[i:i + len_of_pattern]
        if int(elem) < 10: continue  # проверка подходит ли строка под двузначное число
        if elem in res:
            res[elem] += 1
        else:
            res[elem] = 1
    return res


def naive_dedicatedfunc(nums: str) -> dict:
    def search(string: str, pattern: str):
        search.n = 0
        for i in range(len(string) - len(pattern)):
            elem = string[i:i + len(pattern)]
            if elem == pattern:
                search.n += 1
        return search.n

    res = {}
    for i in range(10, 100): res[f'{i}'] = search(nums, f'{i}')
    return res


def rabin_karp_dedicatedfunc(nums: str, text=False) -> dict:
    '''Сложность данного алгоритма является O(n+m) что дает почти линейную сложность....'''

    def search(sting: str, pattern: str):
        hash_pattern = hash(pattern)
        search.num = 0
        for i in range(len(sting) - len(pattern)):
            hash_sub = hash(sting[i:i + len(pattern)])
            if hash_sub == hash_pattern:
                search.num += 1
        return search.num

    res = {}
    for i in range(10, 100): res[f'{i}'] = search(nums, f'{i}')
    return res


def rabin_karp(nums: str) -> dict:
    res = {str(i).__hash__(): 0 for i in range(10, 100)}
    # Чтобы просто удовлетворить условию того, что необходимы именно хэши...
    for i in range(len(nums) - 2):
        sub_str = nums[i:i + 2]
        if int(sub_str) < 10: continue
        res[hash(sub_str)] += 1
    return {str(i): res[str(i).__hash__()] for i in range(10, 100)}


'''
def boyer_mur(nums: str) -> dict:

    def search(string: str, pattern: str) -> int:
        shift = {'*': len(pattern)}
        for i in reversed(range(len(pattern) - 1)):
            if pattern[i] in shift:
                pass
            else:
                shift[pattern[i]] = len(pattern) - i -1
            shift[pattern[-1]] = len(pattern)
        i = 0
        k = 0
        while i < len(string) - len(pattern):
            sub_str = string[i:i+len(pattern)]
            if sub_str == pattern:
                k += 1
                i += 1
                continue

            for j in reversed(range(len(pattern))):
                if pattern[j] != sub_str[j] and j != len(sub_str)-1:
                    i += shift['*']
                    break
                elif pattern[j] != sub_str[j]:
                    i += shift[pattern[j]]
                    break
        return k
'''


def boyer_moore(nums: str) -> dict:
    def search(pattern: str, string: str) -> int:
        number_of_characters = len(pattern)
        unique_symbols = set()
        dict_of_offsets = {}
        for i in range(number_of_characters - 2, -1, -1):
            if pattern[i] not in unique_symbols:
                dict_of_offsets[pattern[i]] = number_of_characters - i - 1
                unique_symbols.add(pattern[i])
        if pattern[number_of_characters - 1] not in unique_symbols:
            dict_of_offsets[pattern[number_of_characters - 1]] = number_of_characters
        dict_of_offsets['*'] = number_of_characters
        len_string = len(string)
        count = 0

        if len_string >= number_of_characters:
            i = number_of_characters - 1
            while i < len_string:
                k = 0
                for j in range(number_of_characters - 1, -1, -1):
                    if string[i - k] != pattern[j]:
                        if j == number_of_characters - 1:
                            off = dict_of_offsets[string[i]] if dict_of_offsets.get(string[i], False) \
                                else dict_of_offsets['*']
                        else:
                            off = dict_of_offsets[pattern[j]]
                        i += off
                        break
                    k += 1

                    if j == 0:
                        count += 1
                        i += 1
        return count

    res = {str(i): search(str(i), nums) for i in range(10, 100)}
    return res


def knut_moris(nums: str) -> dict:
    def search(string: str, pattern: str) -> list[int]:
        def prefix(string: str) -> int:
            pi = [0] * len(string)
            i, j = 1, 0
            while i < len(string):
                if string[i] == string[j]:
                    pi[i] = j + 1
                    i += 1;
                    j += 1
                elif j == 0:
                    pi[i] = 0
                    i += 1
                else:
                    j = pi[j - 1]
            return pi

        prefix_string = prefix(pattern)
        i, j = 0, 0
        k = 0
        while i < len(string):
            if string[i] == pattern[j]:
                i += 1
                j += 1
                if j == len(pattern):
                    k += 1
                    if prefix_string == [0, 1]:
                        j = 1
                    else:
                        j = 0

            else:
                if j > 0:
                    j = prefix_string[j - 1]
                else:
                    i += 1
        return k

    res = {str(i): search(nums, str(i)) for i in range(10, 100)}
    return res


def prost(i: int) -> bool:
    for j in range(2, int(i ** 0.5) + 2):
        if i % j == 0:
            return False
    return True


'''
for i in range(2, 500): #Просто генератор простых числе
    nums.append(str(int(nums[i - 1]) + int(nums[i - 2])))
'''
i = 1
while len(nums) < 500:
    if prost(i):
        nums.append(str(i))
    i += 1

nums = ''.join(nums)
'''
print(naive_dedicatedfunc(nums))
print(nums)
print("naive")
print(naive(nums, prelocate_dict=True))
print('rabin')
print(rabin_karp(nums))
print('boyer_moore')
print(boyer_moore(nums))
print('knut_moris')
print(knut_moris(nums))
'''
import time

for i in [naive, rabin_karp, boyer_moore, knut_moris]:
    start = time.time()
    res = i(nums)

    print(time.time() - start, i.__name__, f'Больше всего двузначного числа: {max(res, key=int)}. Всего встречено: {res[max(res,key=int)]}')
