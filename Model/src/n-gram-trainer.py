import csv
import operator
import collections

import math

unigram_vocab = {"UNK":0}
bigram_vocab = {("UNK","UNK"):0}
trigram_vocab = {("UNK","UNK","UNK"):0}


vocab = []
full_data = []


def fill_vocab():
    input_vocab = open("../vocab.txt",'r')
    for line in input_vocab:
        vocab.append(line[:-1])    
    input_vocab.close()

def fill_vocab2(file):
    global vocab
    vocab = list(vocab)
    for row in file:
        row = row.split()
        row = ["<s>"]  + row + ["</s>"]

        vocab = vocab + row

    vocab = set(vocab)

def learn_unigram(text_list):
    global vocab
    text_list = ["<s>"]  + text_list + ["</s>"]

    for word in text_list:
        if(word not in vocab):
            word = "UNK"
        if(word in unigram_vocab.keys()):
            unigram_vocab[word] = unigram_vocab[word] + 1 
        else:
            unigram_vocab[word] = 1
    
def learn_bigram(text_list):
    global vocab

    text_list = ["<s>"]  + text_list + ["</s>"]
    sentece_lenght = len(text_list)
    
    for index  in range(sentece_lenght-1):
        word1 = text_list[index]
        word2 = text_list[index+1]
        if(word1 not in vocab or word2 not in vocab):
            # print(word1,word2)
            word1 = "UNK"
            word2 = "UNK"
        if((word1,word2) in bigram_vocab.keys()):
            bigram_vocab[(word1,word2)] = bigram_vocab[(word1,word2)] + 1 
        else:
            bigram_vocab[(word1,word2)] = 1

def learn_trigram(text_list):
    global vocab

    text_list = ["<s>"]  + text_list + ["</s>"]
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
        if((word1,word2,word3) in trigram_vocab.keys()):
            trigram_vocab[(word1,word2,word3)] = trigram_vocab[(word1,word2,word3)] + 1 
        else:
            trigram_vocab[(word1,word2,word3)] = 1

        
def set_unigram_probablity(name):  
    global unigram_vocab
    unigram_prob_vocab = {}
    file = open("../"+name+".1gram.lm","w")
    total_count = sum(unigram_vocab.values())   
    for word in unigram_vocab.keys():
        unigram_prob_vocab[word] = (unigram_vocab[word]+1)/(total_count + len(vocab))  
        data = str(word) + "|" + str(unigram_prob_vocab[word])
        file.write(data+"\n")
        # print(data)
    file.close()
    

def set_bigram_probablity(name):  
    global bigram_vocab
    global unigram_vocab
    bigram_prob_vocab = {}
    file = open("../"+name+".2gram.lm","w")
    for (word1,word2) in bigram_vocab.keys():
        # print(unigram_vocab)
        bigram_prob_vocab[(word1,word2)] = ( bigram_vocab[(word1,word2)]+1 ) / (unigram_vocab[word1] +  len(vocab) )
        data = "|".join([word1,word2]) + "|" + str(bigram_prob_vocab[(word1,word2)]) 
        file.write(data+"\n")
        # print(data)
    file.close()
    

def set_trigram_probablity(name):  
    global trigram_vocab
    global bigram_vocab
    
    trigram_prob_vocab  = {}
    file = open("../"+name+".3gram.lm","w")
    for (word1,word2,word3) in trigram_vocab.keys():
        if( "Keys" in (word1,word2,word3) ):
            print("www")
        trigram_prob_vocab[tuple([word1,word2,word3])] = ( trigram_vocab[tuple([word1,word2,word3])] + 1)/(bigram_vocab[tuple([word1,word2])] + len(vocab) )
        data = "|".join([word1,word2,word3]) + "|" + str(trigram_prob_vocab[(word1,word2,word3)])
        # print(data)
        file.write(data+"\n")

    file.close()
   
   
def flush():
    global unigram_vocab
    global bigram_vocab
    global trigram_vocab

    print(len(unigram_vocab))
    print(len(bigram_vocab))
    print(len(trigram_vocab)) 
 
    unigram_vocab = {"UNK":0}

    bigram_vocab = {("UNK","UNK"):0}

    trigram_vocab = {("UNK","UNK","UNK"):0}

    
def start_leonard_learning():
    global unigram_vocab
    with open("../../SplitedData/train/label2.txt") as file:
        # fill_vocab2(file)
        for row in file:
            row = row.split()
            if("" in row):
                row.remove("")
            if(len(row)>0):
                # print(row)
                learn_unigram(row)
                learn_bigram(row)
                learn_trigram(row)
    set_unigram_probablity("label2")
    set_bigram_probablity("label2")
    set_trigram_probablity("label2")
    flush()


def start_sheldon_learning():
    
    global unigram_vocab

    global unigram_vocab
    global bigram_vocab
    global trigram_vocab
   
    
    with open("../../SplitedData/train/label1.txt") as file:

        for row in file:
            row= row.split()
            if("" in row):
                row.remove("")
            if(len(row)>0):
                learn_unigram(row)
                learn_bigram(row)
                learn_trigram(row)
    set_unigram_probablity("label1")
    set_bigram_probablity("label1")
    set_trigram_probablity("label1")
    flush() 


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
    global unigram_vocab
    global bigram_vocab
    global trigram_vocab
    global vocab
    unigram_vocab = {}

    bigram_vocab = {}

    trigram_vocab = {}

    file_1gram_input = open("../test/in.1gram")
    with open("../test/in.1gram" ) as file :
        fill_vocab2(file)

    for line in file_1gram_input:
        learn_unigram(line.split())
    set_unigram_probablity("/test/out1")
        # print(data)
    # print(unigram_vocab)
    file_2gram_input = open("../test/in.2gram")
   
    unigram_vocab = {}

    bigram_vocab = {}

    trigram_vocab = {}


    for line in file_2gram_input:
        data = line.split()
        learn_unigram(data)
        learn_bigram(data)
        # print(data)
    set_bigram_probablity("/test/out2")

    unigram_vocab = {}

    bigram_vocab = {}

    trigram_vocab = {}

    file_3gram_input = open("../test/in.3gram") 
    
    for line in file_3gram_input:
        data = line.split()
        learn_unigram(data)
        learn_bigram(data)
        learn_trigram(data)
        # print(data)
    set_trigram_probablity("/test/out3")


################# ONLY UNCOMMENT ONE PART AT TIME ############################################


 
################# UNCOMMENT Area IF YOU WANT TO RUN N-Gram FOR LABEL1 AND LABEL2 ############# 

# fill_vocab()  #UNCOMMENT IF YOU WANT TO LOAD VOCABULARY FROM vocab.txt FILE AND 
# YOU SHOULD COMMNET WITH OPEN PARTS IN THE AREA




with open("../../SplitedData/train/label2.txt") as csv_file:
    fill_vocab2(csv_file)

start_leonard_learning() 

vocab = []
with open("../../SplitedData/train/label1.txt") as csv_file:
    fill_vocab2(csv_file)


start_sheldon_learning()

#############################################################################################

################ UNCOMMENT Area IF YOU WANT TO RUN N-Gram FOR TESTS##########################


# fill_vocab()  #UNCOMMENT IF YOU WANT TO LOAD VOCABULARY FROM vocab.txt FILE AND 
# YOU SHOULD COMMNET WITH OPEN PARTS IN THE AREA


# with open("../test/in.1gram" ) as file :
#     fill_vocab2(file)


# with open("../test/in.2gram" ) as file :
#     fill_vocab2(file)

# with open("../test/in.3gram" ) as file :
#     fill_vocab2(file)


# start_test()

#############################################################################################