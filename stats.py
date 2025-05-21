def get_num_words(text):
    return len(text.split())
def get_num_characters(text):
    num_characters = {}
    for c in text.lower():
        if c in num_characters:
            num_characters[c] += 1
        else:
            num_characters[c] = 1
    return num_characters

def sort_dict(num_chars):
    char_list = [{"char": ch, "num": n} for ch, n in num_chars.items()]
    char_list.sort(key=lambda d: d["num"], reverse=True)
    return char_list
