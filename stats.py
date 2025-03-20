def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_on(dict):
    return dict["count"]


def get_sort_chars(chars):
    chars_list = []
    for char, in chars:
        count = chars[char]
        chars_list.append({"char":char, "count": count})
    for i in chars_list:
        chars_list.sort(reverse=True, key=sort_on)
    return chars_list
