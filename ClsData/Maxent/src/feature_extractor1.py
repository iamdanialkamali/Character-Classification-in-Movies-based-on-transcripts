train_file = open("./P2_Phase1/ClsData/train.txt")
train_features_file = open("./P2_Phase1/ClsData/Maxent/input.train.txt","w")

test_file = open("./P2_Phase1/ClsData/test.txt")
test_features_file = open("./P2_Phase1/ClsData/Maxent/input.test.txt","w")

def make_models(file):
    vocab = []
    label1_unigram_vocab = {("UNK",):0}
    label1_bigram_vocab = {("UNK","UNK"):0}
    label1_trigram_vocab = {("UNK","UNK","UNK"):0}
    label2_unigram_vocab = {("UNK",):0}
    label2_bigram_vocab = {("UNK","UNK"):0}
    label2_trigram_vocab = {("UNK","UNK","UNK"):0}

    for line in file:
        data = line.split()
        label = data[0]
        vocab_dict = {} 
        if(label=="label1"):
            vocab_dict = label1_unigram_vocab
        else:
            vocab_dict = label2_unigram_vocab
        data = data[1:]
        for index in range(len(data)):
            w1 = data[index] 
            if(":" in w1):
                continue
            word = (w1,) 
            vocab_dict[word] = vocab_dict.get(word,0) + 1
            vocab.append(word)

        if(label=="label1"):
            vocab_dict = label1_bigram_vocab
        else:
            vocab_dict = label2_bigram_vocab
        for index in range(len(data)-1):
            w1,w2 = data[index] ,data[index+1] 
            if(":" in w1 ):
                continue
            word = (w1,w2) 
            vocab_dict[word] = vocab_dict.get(word,0) + 1

        vocab_dict = {} 
        if(label=="label1"):
            vocab_dict = label1_trigram_vocab
        else:
            vocab_dict = label2_trigram_vocab
        for index in range(len(data)-2):
            w1,w2,w3 = data[index] ,data[index+1] , data[index+2]
            if(":" in w1 or ":" in w2 or ":" in w3 ):
                continue
            word = (w1,w2,w3) 
            vocab_dict[word] = vocab_dict.get(word,0) + 1
        vocab = set(vocab)

        label1_bigram_prob_vocab = {}
        
        for (word1,word2) in label1_bigram_vocab.keys():
            # print(unigram_vocab)
            bigram_prob_vocab[(word1,word2)] = ( label1_bigram_vocab[(word1,word2)]+1 ) / (unigram_vocab[word1] +  len(vocab) )
            data = "|".join([word1,word2]) + "|" + str(bigram_prob_vocab[(word1,word2)]) 
    
    print("WTF")

make_models(train_file)