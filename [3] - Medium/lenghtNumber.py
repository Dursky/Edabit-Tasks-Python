
def number_length(number):
    string = str(number)
    count = 0
    for num in string:
        count = count + 1
    return count
    
print(number_length(20))