def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered not in chars:
            chars[lowered] = 0
        chars[lowered] += 1
    return chars 

def get_sorted_dicts(char_dict):
    dicts = []
    for key in char_dict:
        dicts.append({
            "char": key,
            "num": char_dict[key]
        })
    dicts.sort(reverse=True, key=sort_on)
    return dicts 

def sort_on(char_dict):
    return char_dict["num"]