def is_unique(string: str) -> bool:
    if len(string) > 128: return False 
    char_set = []
    for char in string:
        val: int = ord(char)
        if val in char_set: return False 
        char_set.append(val)
    return True 


print(is_unique("abcde"))

"""
    Key points 
    -> Questions to asks 
        + is the string ASCII string or Unicode string 
    -> Time complexity O(n) where n is the length of the string
        + We can argue it can be O(1) since we will not iterate more than 128 characters 
    -> Space complexity O(1)
    -> Other assumptions 
        + We can assume all characters are small letters and use bit vector which will
            reduce the our space complexity by factor of 8.
        + Use sort algorithm and compare each character with the neighboring one sorting take
            O(n log(n)) with additional space
        + Compare each Character in the string with one another which takes O(n^2) time complexity
"""