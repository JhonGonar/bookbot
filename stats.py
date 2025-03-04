def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def get_num_words(text):
    return len(text.split())

def count_chars(text):
    lower_text = text.lower()
    dict = {}
    for char in lower_text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
        
    return dict

def sort_by_count(dict):
    list =[]
    for i in dict:
        list.append({"character": i, "count": dict[i]})
    print(list)
    list.sort( key=lambda x: x["count"], reverse=True)
    return list
