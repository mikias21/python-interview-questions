def sort(string: str) -> str:
    chars_ascii: int = []
    for char in string:
        chars_ascii.append(ord(char))
    
    chars = []
    for char in sorted(chars_ascii):
        chars.append(chr(char))
    
    string_s = ""
    return string_s.join(chars)

    
def is_permutation(string1: str, string2: str) -> bool:
    if len(string1) != len(string2): return False;
    return sort(string1) == sort(string2)



print(is_permutation("god", "doG"))