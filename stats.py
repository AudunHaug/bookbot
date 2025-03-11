def get_num_words(file_contents):
    divided_content = file_contents.split()
    return len(divided_content)


def count_characters(file_contents):
    file_contents = file_contents.lower()
    data = {}
    for char in file_contents:
        if(not data.get(char)):
            data[char] = 1
        else:
            data[char] += 1
    return data