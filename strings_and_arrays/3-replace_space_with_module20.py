def replace_spaces(string: list, true_length: int):
    space_count: int = 0
    for i in range(true_length):
        if string[i] == ' ':
            space_count += 1
    
    index: int = true_length + space_count * 2
    if(true_length < len(string)): string[true_length] = '\0'
    for i in range(true_length-1, 0):
        if(string[i] == ' '):
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index -= 3
        else:
            string[index] = string[i]
            index -= 1
