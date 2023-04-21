def duplicate_characters(string):
    # Create an empty dictionary
    chars = {}
    RandomList=list(string)
    print(RandomList)
    for char in string:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
 
    duplicates = []
 
    for char, count in chars.items():
        if count > 1:
            duplicates.append(char)
            
    RandomList.remove(())
    print(RandomList)       
    print(duplicates)
duplicate_characters("parameter")