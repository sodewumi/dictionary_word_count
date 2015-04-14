from sys import argv
from collections import Counter

script, filename = argv


def count_words(filename):
    open_file = open(filename)
    rm_punctuation = []

    word_count = {}

    for line in open_file:
        words = line.rstrip().split(" ")
      
        for word in words:
            alpha_wrd = ""
            for ltr in word:
                if ltr.isalpha() or ltr is "'":
                    alpha_wrd = alpha_wrd + ltr
            rm_punctuation.append(alpha_wrd.lower())
    
    word_count = Counter(rm_punctuation)       

    return print_words(word_count)        

def print_words(full_dic):
    for key, value in full_dic.iteritems():
        print "%s: %d" %(key, value)


print(count_words(filename))



