from sys import argv

script, filename = argv


def count_words(filename):
    open_file = open(filename)
    rm_punctuation = []

    word_count = {}

    for line in open_file:
        words = line.rstrip().split(" ")
        # print words
        

        for word in words:
            alpha_wrd = ""
            # print word.upper()
            for ltr in word:
                # print ltr.upper()
                if ltr.isalpha() or ltr is "'":
                    alpha_wrd = alpha_wrd + ltr
            rm_punctuation.append(alpha_wrd.lower())
           

    for word in rm_punctuation:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1

    return print_words(word_count)        

def print_words(full_dic):
    for key, value in full_dic.iteritems():
        print "%s: %d" %(key, value)


print(count_words(filename))



