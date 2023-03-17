# 1) Write a function that takes as input (sentence: String, n: Number) 
# and returns a list of size `n` where each element contains a word and and the frequency of that word in `sentence`
# This list should be sorted by decreasing frequency and alphabetical order in case of tie.

def str_to_sorted_list(sentence, n):
    if len(sentence) == 0 or n <= 0: return None
    sentence_dict = {}
    # Register word frequency
    for word in sentence.split(' '):
        if word not in sentence_dict:
            sentence_dict[word] = 0
        sentence_dict[word] += 1

    # register in tuple
    tuple_lst = [(k, v) for k, v in sentence_dict.items()]

    # return 'n' word frequency sorted
    return sorted(sorted(tuple_lst, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)[:n]
    
