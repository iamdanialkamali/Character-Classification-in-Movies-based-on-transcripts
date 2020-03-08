import random
print("enter number")
count  = int(input())
print("enter seed")
seed  = int(input())

random.seed(seed)


def unigram_text_generator(language_model_file,name): 
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    keys = language_model.keys()
    sum_prob = 0
    for key in keys :
        sum_prob += language_model[key]
        language_model[key] = sum_prob
    
    # print(sum_prob)
    next_word = ("",)
    sentence = []
    # while("</s>" != next_word[0]):
    while( "</s>" not in  next_word):
        rand_number = random.uniform(0, sum_prob)
        # print(next_word)
        for key in keys:
            if(language_model[key]> rand_number):
                next_word =   key
                sentence.append(key[0])
                break
            
    
    sentence  =   " ".join(sentence)

    file = open("../"+name+"1.gram.gen",'a')
    file.write(sentence + '\n')
    file.close()


def bigram_text_generator2(language_model_file,name): 
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    keys = language_model.keys()
    language_model_prob = language_model.copy()
    sum_prob = 0
    sen_start_prob = 0
    sen_start = {}
    for key in keys :
        if(key[0]=="<s>"):
            sen_start[key[1]] = language_model_prob[key]  
        sum_prob += language_model_prob[key]
        language_model_prob[key] = sum_prob
    
    for key in sen_start.keys() :
    
        sen_start_prob += sen_start[key]
        sen_start[key] = sen_start_prob
    sen_start_random_num = random.uniform(0, sen_start_prob)
    start_word = ""
    for key in sen_start.keys():
            if(sen_start[key]> sen_start_random_num):
                start_word = key
                break
        
    # print(sum_prob)
    next_word = ""
    sentence = ["<s>",start_word]
    # print(start_word)

    while("</s>" != sentence[-1]):
        max_prob = 0  
        for key in language_model.keys():
            if(key[0] == sentence[-1]):
                if(language_model[key] > max_prob ):
                    # print(key,language_model[key])
                    max_prob = language_model[key]
                    next_word = key[-1]
                    
        # print(next_word)
        sentence.append(next_word)

        
            
                
    sentence  =   " ".join(sentence)

    file = open("../"+name+"2.gram.gen",'a')
    file.write(sentence + '\n')
    file.close()



def bigram_text_generator(language_model_file,name): 
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    keys = language_model.keys()
    sentence = ["<s>"]
  
    
    while(sentence[-1] != "</s>"):
        # print(sentence)
        total = 0
        for key in keys :
            if(key[0] == sentence[-1] ):
                    total +=language_model[key]
        sum_prob = 0
        sen_next = {}
        sen_next_word_random_num = random.uniform(0,total)
        for key in keys :
            if(key[0]==sentence[-1]):
                sum_prob +=language_model[key]
                sen_next[key] = sum_prob
        for key in sen_next.keys():
                if(sen_next[key]> sen_next_word_random_num):
                    sentence.append(key[1])
                    break
            
                
    sentence  =   " ".join(sentence)

    file = open("../"+name+"2.gram.gen",'a')
    file.write(sentence + '\n')
    file.close()



def trigram_text_generator(language_model_file,name):

    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    keys = language_model.keys()
    language_model_prob = language_model.copy()
    
    sentence = ["<s>"]

    sum_prob = 0
    sen_start_prob = 0
    sen_start = {}
    for key in keys :
        if(key[0]==sentence[-1]):
            sen_start[key] = language_model_prob[key]  
        sum_prob += language_model_prob[key]
        language_model_prob[key] = sum_prob
    
    for key in sen_start.keys() :
        sen_start_prob += sen_start[key]
        sen_start[key] = sen_start_prob

    sen_start_random_num = random.uniform(0, sen_start_prob)
    start_words = ""
    for key in sen_start.keys():
            if(sen_start[key]> sen_start_random_num):
                start_words = key
                break
    
    sentence = list(start_words)
    while(sentence[-1] != "</s>"):
        # print(sentence)
        total = 0
        for key in keys :
            if(key[0] == sentence[-2] and key[1] == sentence[-1] ):
                    total +=language_model[key]
        sum_prob = 0
        sen_next = {}
        sen_next_word_random_num = random.uniform(0,total)
        for key in keys :
            if(key[0] == sentence[-2] and key[1] == sentence[-1] ):
                sum_prob +=language_model[key]
                sen_next[key] = sum_prob
        for key in sen_next.keys():
                if(sen_next[key]> sen_next_word_random_num):
                    sentence  =  sentence +  [key[-1]]
                    break

        
            
    sentence  =   " ".join(sentence)

    file = open("../"+name+"3.gram.gen",'a')
    file.write(sentence + '\n')
    file.close()








def trigram_text_generator2(language_model_file,name): 
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    keys = language_model.keys()
    language_model_prob = language_model.copy()
    
    sentence = ["<s>"]

    sum_prob = 0
    sen_start_prob = 0
    sen_start = {}
    for key in keys :
        if(key[0]==sentence[-1]):
            sen_start[key] = language_model_prob[key]  
        sum_prob += language_model_prob[key]
        language_model_prob[key] = sum_prob
    
    for key in sen_start.keys() :
        sen_start_prob += sen_start[key]
        sen_start[key] = sen_start_prob

    sen_start_random_num = random.uniform(0, sen_start_prob)
    start_words = ""
    for key in sen_start.keys():
            if(sen_start[key]> sen_start_random_num):
                start_words = key
                break
    
    # print(start_words)
    # print(sum_prob)
    next_word = ""
    # print(start_word)
    sentence = list(start_words)
    while("</s>" != sentence[-1]):
        sen_next_word_random_num = random.uniform(0,1)
        sum_prob = 0  
        for key in language_model.keys():
            if(key[0] == sentence[-2] and key[1] == sentence[-1] ):
                if(sum_prob > sen_next_word_random_num ):
                    # print(key,language_model[key])
                    sum_prob += language_model[key]
                else:
                    sentence = sentence + next_word
                    # print(key,language_model[key])
                    
        

        
            
    sentence  =   " ".join(sentence)

    file = open("../"+name+"3.gram.gen",'a')
    file.write(sentence + '\n')
    file.close()


for i in range(count):
    with open("../../Model/leonard.1gram.lm") as file:
        unigram_text_generator(file,"leonard")
    with open("../../Model/leonard.2gram.lm") as file:
        bigram_text_generator(file,"leonard")    
    with open("../../Model/leonard.3gram.lm") as file:
        trigram_text_generator(file,"leonard")
    with open("../../Model/sheldon.1gram.lm") as file:
        unigram_text_generator(file,"sheldon")
    with open("../../Model/sheldon.2gram.lm") as file:
        bigram_text_generator(file,"sheldon")
    with open("../../Model/sheldon.3gram.lm") as file:
        trigram_text_generator(file,"sheldon")


# with open("./P2_Phase1/Model/leonard.2gram.lm") as file:
#         bigram_text_generator(file,"leonard") 

# with open("../../Model/sheldon.3gram.lm") as file:
#     trigram_text_generator(file,"sheldon")