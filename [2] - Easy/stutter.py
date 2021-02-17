

def stutter(word):
    string = (word[0],word[1],"... ",word[0],word[1],"... ",word,"?")
    result = "".join(string)
    return result

print(stutter('siema'))