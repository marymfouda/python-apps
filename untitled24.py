# task2 in sec 9

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
 
#task 1 in sec 9

word = input("What would you like to convert to plural?: ")

#Separate words in input into list
splitstring = word.split()
conversionlist = list(splitstring)
##list check
#print(conversionlist)


def plural(splitstring):
    #For every single word in string
    for split in conversionlist:
        #If vowel before y (endswith only takes 3 arguments)
        if split.endswith('fe') or split.endswith('f'):
            return split + 'ves'
        if split.endswith('us') :
            return split + 'i'
        if split.endswith('on') :
            return split + 'a'
        #If not a vowel before y
        if split.endswith('y') and not (split.endswith('ay','ey','iy') or split.endswith('oy','uy')):
            #Remove the y and append the appropriate ending
            return split[:-1] + 'ies'
        #o, ch, s, sh, x, or z endings
        if split.endswith('o') or split.endswith('ch') or split.endswith('s') or split.endswith('sh') or split.endswith('x') or split.endswith('z'):
            return split + 'es'
        #general case
        else:
            return split + 's'

plural(splitstring)

#Append all converted plurals into singular list and print output
totalplural = " ".join(plural(splitstring))
print(totalplural)