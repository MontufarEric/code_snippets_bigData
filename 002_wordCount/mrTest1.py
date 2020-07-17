# first we import a library to work with regular expressions
import re



# this functions prepocess the text file to retutn a list of lowercase words without punctuation
def prep(text):
    return re.split(' |\n|:|"|;|\.|\'|!|\?|,' ,text.lower())


# this function gets a list of words and returns a dictionary word: freq sorted by freq
def reduceByKey(list_of_words):
    dc ={}
    for w in list_of_words:
        if w in dc.keys():
            dc[w]+=1
        else:
            dc[w]=1
    return sorted(dc.items(), key=lambda k: k[1], reverse=True)


# we take a dictionary of word frequencies and create a text file with 2 columns word, frequency
def write_file(word_freq):
    with open ('freq_list.txt', 'w') as f:
        f.write('word, frequency\n')
        for i in word_freq[1:]:
            f.write(f'{i[0]}, {i[1]}\n')



# then we read the text we are goin to process

if __name__ == __main__():
	with open('./Shakespeare.txt') as f:
	    content = f.read()

	    list_of_words = prep(content)
	    print(list_of_words)
	    write_file(reduceByKey((list_of_words)))

