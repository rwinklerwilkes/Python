def unique(string):
    letters = {}
    for i in string:
        if i in letters:
            return False
        else:
            letters[i] = 1
    return True
