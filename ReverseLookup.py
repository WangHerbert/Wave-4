def reverselookup (dic, value):
    keys = []
    for i in dic:
        if dic[i] == value:
            keys.append(i)
    
    return keys


periods = {'French': 'P1', 'Music': 'P2', 'Lunch': 'P3', 'ComSci': 'P3', 'English': 'P4'}

print ('Two answers example:')
print ('The subjects during P3 are ', reverselookup(periods, 'P3'))
print ()
print ('One answer example:')
print ('The subject during P4 is ', reverselookup(periods, 'P4'))
print ()
print ('No answer example:')
print ('The subject during P5 is ', reverselookup(periods, 'P5'))