words = ["asadbek", "bek", "sumary", "hello", "makhmudjonov"]
def get_longest_word(new_words):
    temp = new_words[0]
    for i in range(1, len(new_words) - 1):
        if len(new_words[i]) > len(temp):
            temp = new_words[i]
    answer = (temp, len(temp))
    return answer

print(get_longest_word(words))
