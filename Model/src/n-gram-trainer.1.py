import csv
import operator
import collections

import math
unigram_vocab = {"UNK":0}
unigram_words_counter = 1

bigram_vocab = {("UNK","UNK"):0}
bigram_words_counter = 0

trigram_vocab = {("UNK","UNK","UNK"):0}
trigram_words_counter = 0

vocab = []
full_data = []


def fill_vocab():
    input_vocab = open("../vocab.txt",'r')
    for line in input_vocab:
        vocab.append(line[:-1])    
    input_vocab.close()


def learn_unigram(text_list):
    global vocab
    global unigram_words_counter
    for word in text_list:
        if(word in vocab):
            if(word in unigram_vocab.keys()):
                unigram_vocab[word] = unigram_vocab[word] + 1 
            else:
                unigram_vocab[word] = 1
            unigram_words_counter += 1
        else:
            unigram_vocab['UNK'] +=1

def learn_bigram(text_list):
    global vocab
    global bigram_words_counter

    sentece_lenght = len(text_list)
    for index  in range(sentece_lenght-1):
        word1 = text_list[index]
        word2 = text_list[index+1]
        if(word1 not in vocab or word2 not in vocab):
            print(word1,word2)
            word1 = "UNK"
            word2 = "UNK"
        if((word1,word2) in bigram_vocab.keys()):
            bigram_vocab[(word1,word2)] = bigram_vocab[(word1,word2)] + 1 
        else:
            bigram_vocab[(word1,word2)] = 1

def learn_trigram(text_list):
    global vocab
    global trigram_words_counter


    sentece_lenght = len(text_list)
    for index  in range(sentece_lenght-2):
        # print(text_list)
        word1 = text_list[index]
        word2 = text_list[index+1]
        word3 = text_list[index+2]
        # print(word3)
        if(word1 not in vocab or word2 not in vocab  or word3 not in vocab ):
            word1 = "UNK"
            word2 = "UNK"
            word3 = "UNK"
        if((word1,word2,word3) in bigram_vocab.keys()):
            trigram_vocab[(word1,word2,word3)] = trigram_vocab[(word1,word2,word3)] + 1 
        else:
            trigram_vocab[(word1,word2,word3)] = 1
        trigram_words_counter += 1

        
def set_unigram_probablity(name):  
    global unigram_vocab
    global unigram_words_counter
    unigram_prob_vocab = {}
    file = open("../"+name+".1gram.lm","w")
    total_count = sum(unigram_vocab.values())   
    for word in unigram_vocab.keys():
        unigram_prob_vocab[word] = (unigram_vocab[word]+1)/(total_count + len(unigram_vocab.keys()))  
        data = str(word) + "|" + str(math.log10(unigram_prob_vocab[word]))
        file.write(data+"\n")
        # print(data)
    file.close()
    

def set_bigram_probablity(name):  
    global bigram_vocab
    global bigram_words_counter
    global unigram_vocab
    bigram_prob_vocab = {}
    file = open("../"+name+".2gram.lm","w")
    for (word1,word2) in bigram_vocab.keys():
        # print(unigram_vocab)
        bigram_prob_vocab[(word1,word2)] = ( bigram_vocab[(word1,word2)]+1 ) / (unigram_vocab[word1] + len(bigram_vocab.keys()) )
        data = "|".join([word1,word2]) + "|" + str(bigram_prob_vocab[(word1,word2)]) 
        file.write(data+"\n")
        # print(data)
    file.close()
    


def set_trigram_probablity(name):  
    global trigram_vocab
    global bigram_vocab
    global trigram_words_counter
    
    trigram_prob_vocab  = {}
    file = open("../"+name+".3gram.lm","w")
    for (word1,word2,word3) in trigram_vocab.keys():
        trigram_prob_vocab[(word1,word2,word3)] = ( trigram_vocab[(word1,word2,word3)] + 1)/(bigram_vocab[(word1,word2)] + len(trigram_vocab.keys()))
        data = "|".join([word1,word2,word3]) + "|" + str(trigram_prob_vocab[(word1,word2,word3)])
        # print(data)
        file.write(data+"\n")

    file.close()
   
def flush():
    global unigram_vocab
    global bigram_vocab
    global trigram_vocab
 
    unigram_vocab = {"UNK":0}

    bigram_vocab = {("UNK","UNK"):0}

    trigram_vocab = {("UNK","UNK","UNK"):0}

    

def start_leonard_learning():
    global unigram_vocab
    global unigram_words_counter
    with open("../../SplitedData/train/Leonard.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if("" in row):
                row.remove("")
            if(len(row)>0):
                # print(row)
                learn_unigram(row)
                learn_bigram(row)
                learn_trigram(row)
    set_unigram_probablity("leonard")
    set_bigram_probablity("leonard")
    set_trigram_probablity("leonard")
    flush()


def start_sheldon_learning():
    
    global unigram_vocab
    global unigram_words_counter
    
    with open("../../SplitedData/train/Sheldon.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if("" in row):
                row.remove("")
            if(len(row)>0):
                learn_unigram(row)
                learn_bigram(row)
                learn_trigram(row)
    set_unigram_probablity("sheldon")
    set_bigram_probablity("sheldon")
    set_trigram_probablity("sheldon")


def generate_vocab():
    words_list =[]
    vocab_file = open("../vocab.txt",'w')
    with open("../../SplitedData/train/Leonard.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if(len(row)>0):
                learn_unigram(row)
                for i in row:
                    words_list.append(i)
    with open("../../SplitedData/train/Sheldon.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if(len(row)>0):
                learn_unigram(row)
                for i in row:
                    words_list.append(i)
        
    temp_vocab = set(words_list)
    for word in temp_vocab:
        vocab_file.write( word + "\n")
    vocab_file.close()

def start_test():
    # file_1gram_input = open("../test/in.1gram")
    # unigram_prob_vocab ={}
    # for line in file_1gram_input:
    #     learn_unigram(line.split())
    # total_count = sum(unigram_vocab.values())   
    # for word in unigram_vocab.keys():
    #     unigram_prob_vocab[word] = (unigram_vocab[word]+1)/(total_count + len(unigram_vocab.keys()))  
    #     data = str(word) + "|" + str(unigram_prob_vocab[word])
    #     print(data)
    # print(unigram_vocab)
    global unigram_vocab
    global bigram_vocab
    unigram_vocab ={}
    bigram_vocab ={}
    file_2gram_input = open("../test/in.2gram")
    for line in file_2gram_input:
        data = ['<s>']+line.split()+['</s>']
        learn_unigram(data)
        learn_bigram(data)
        print(data)
    bigram_prob_vocab = {}
    for (word1,word2) in bigram_vocab.keys():
        # print(unigram_vocab)
        bigram_prob_vocab[(word1,word2)] = ( bigram_vocab[(word1,word2)] + 1 ) / (unigram_vocab[word1] + len(unigram_vocab) -1  )
        data = "|".join([word1,word2]) + "|" + str(bigram_prob_vocab[(word1,word2)]) 
        print(data)
    print(unigram_vocab)
    print(bigram_vocab)
    print(bigram_prob_vocab)    
    # file_3gram_input = open("../test/in.3gram") 
# generate_vocab()
fill_vocab()

# start_leonard_learning()
# start_sheldon_learning()

start_test()
