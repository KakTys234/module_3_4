from itertools import count


def single_root_words(root_word, *other_words):
    same_words = []
    for w in other_words:
        if (root_word.lower() in w.lower()) or (w.lower() in root_word.lower()):
            same_words.append(w)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
