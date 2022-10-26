def is_unique(string: str) -> bool:
    if len(string) > 128: return False 
    char_set = []
    for char in string:
        val: int = ord(char)
        if val in char_set: return False 
        char_set.append(val)
    return True 


print(is_unique("abcde"))