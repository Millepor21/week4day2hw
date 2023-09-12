a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def times_word(astring):
    output = {}
    astring_list = astring.split()
    astring_list.sort()
    for word in astring_list:
        if word.lower() not in output.keys():
            output[word.lower()] = 1
        else:
            output[word.lower()] += 1
    return output
times_word(a_text)