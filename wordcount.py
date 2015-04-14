# put your code here.

def count_words(filename):
    open_file = open(filename)
    rm_punctuation = []

    word_count = {}

    for line in open_file:
        words = line.rstrip().split(" ")
        # print words
        alpha_wrd = ""

        for word in words:
            # print word.upper()
            for ltr in word:
                # print ltr.upper()
                if ltr.isalpha() or ltr is "'":
                    alpha_wrd = alpha_wrd + ltr
            rm_punctuation.append(alpha_wrd.lower())
            alpha_wrd = ""

    for word in rm_punctuation:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1

    return word_count        

    print rm_punctuation
print(count_words("test.txt"))



