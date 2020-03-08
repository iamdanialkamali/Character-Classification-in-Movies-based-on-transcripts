from bs4 import BeautifulSoup
import requests
import codecs
import csv
import random
import math

label1_train_file =  open('./P2_Phase1/SplitedData/train/label1.txt', mode='r')
label2_train_file =  open('./P2_Phase1/SplitedData/train/label2.txt', mode='r')

label1_test_file =  open('./P2_Phase1/SplitedData/test/label1.txt', mode='r')
label2_test_file =  open('./P2_Phase1/SplitedData/test/label2.txt', mode='r')




def compute_leonard_1gram_perplexity(file):
    result_file = open("./P2_Phase1/Perplexity/"+str(file.name.split('/')[-2])+"/label2.perplexity.1gram.csv","w")
    result_file_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    language_model_file = open("./P2_Phase1/Model/label2.1gram.lm")
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    
    mean_perplexity = 0
    input_counter = 0
    for data in file:
        # print(data)s
        data = ["<s>"] + data.split() + ["</s>"]
        probablity = 1
        a = 1
        input_counter+=1
        if(len(data)>0):
            cnt = 0
            # print(data)
            if("" in data):
                data.remove("")
            for word in data:
                cnt+=1
                key = tuple([word])
                if(key not in language_model.keys() ):

                    probablity *=  ((language_model[tuple(["UNK"])]))
                else:    
                    probablity *= (float(language_model[key]))
                
        
            perplexity = probablity**(-1/cnt)
            mean_perplexity += perplexity
            result_file_writer.writerow(data+[perplexity])

    result_file_writer.writerow([mean_perplexity])
    print(mean_perplexity/input_counter)

def compute_leonard_2gram_perplexity(file):
    result_file = open("./P2_Phase1/Perplexity/"+str(file.name.split('/')[-2])+"/label2.perplexity.2gram.csv","w")
    result_file_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    language_model_file = open("./P2_Phase1/Model/label2.2gram.lm")
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    # print(language_model)
    mean_perplexity = 0
    input_counter = 0
    for data in file:
       # print(data)
        data = ["<s>"] + data.split() + ["</s>"]
        probablity = 1
        input_counter+=1
        if(len(data)>0):
            # print(data)
            cnt = 0
            # print(data)
            if("" in data):
                data.remove("")
            for word_index in range( len(data) -1):
                a = tuple([data[word_index + i] for i in range(2)])
                
                if(a not in language_model.keys() ):
                    probablity *=   ((language_model[tuple(["UNK","UNK"])]))
                else:    
                    probablity *= ((language_model[a]))
                cnt+=1
            # print(probablity)
            perplexity = probablity**(-1/cnt)
            mean_perplexity += perplexity
            result_file_writer.writerow(data+[perplexity])

    result_file_writer.writerow([mean_perplexity])
    print(mean_perplexity/input_counter)

def compute_leonard_3gram_perplexity(file):
    result_file = open("./P2_Phase1/Perplexity/"+str(file.name.split('/')[-2])+"/label2.perplexity.3gram.csv","w")
    result_file_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    language_model_file = open("./P2_Phase1/Model/label2.3gram.lm")
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    
    mean_perplexity = 0
    input_counter = 0
    for data in file:
        data = ["<s>"] + data.split() + ["</s>"]
        probablity = 1
        input_counter+=1
        if(len(data)>3):
            cnt = 0
            # print(data)
            if("" in data):
                data.remove("")
            for word_index in range( len(data) -2):
                a = tuple([data[word_index + i] for i in range(3)])
                
                if(a not in language_model.keys() ):
                    probablity *=  (( language_model[tuple(["UNK","UNK","UNK"])]))
                else:    
                    probablity *=  ((language_model[a]))
                    
                
                cnt+=1
            # print(probablity)

            perplexity = probablity**(-1/cnt)
            mean_perplexity += perplexity
            result_file_writer.writerow(data+[perplexity])

    result_file_writer.writerow([mean_perplexity])

    print(mean_perplexity/input_counter)

def compute_sheldon_1gram_perplexity(file):

    result_file = open("./P2_Phase1/Perplexity/"+str(file.name.split('/')[-2])+"/label2.perplexity.3gram.csv","w")
    result_file_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    language_model_file = open("./P2_Phase1/Model/label1.1gram.lm")
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
        # print(tuple(data[:-1]))
    mean_perplexity = 0
    input_counter = 0
    for data in file:
        data = ["<s>"] + data.split() + ["</s>"]
        probablity = 1
        input_counter+=1
        if(len(data)>0):
            cnt = 0
            # print(data)
            if("" in data):
                data.remove("")
            for word in data:
                cnt+=1
                key = tuple([word])
                if(key not in language_model.keys() ):
                    probablity *= ((language_model[tuple(["UNK"])]))
                else:    
                    probablity *=  ((language_model[key]))
            # print(probablity)
            perplexity = probablity**(-1/cnt)
            mean_perplexity += perplexity
            result_file_writer.writerow(data+[perplexity])

    result_file_writer.writerow([mean_perplexity])

    print(mean_perplexity/input_counter)
def compute_sheldon_2gram_perplexity(file):
    result_file = open("./P2_Phase1/Perplexity/"+str(file.name.split('/')[-2])+"/label1.perplexity.2gram.csv","w")
    result_file_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    language_model_file = open("./P2_Phase1/Model/label1.2gram.lm")
    language_model = {}

    for line in language_model_file:
        data = line.split("|")
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    
    mean_perplexity = 0
    input_counter = 0
    for data in file:
        data = ["<s>"] + data.split() + ["</s>"]
        probablity = 1
        input_counter+=1
        if(len(data)>0):
            cnt = 0
            # print(data)
            if("" in data):
                data.remove("")
            for word_index in range( len(data) -1):
                a = tuple([data[word_index + i] for i in range(2)])
                if(a not in language_model.keys() ):
                    probablity *=  ((language_model[tuple(["UNK","UNK"])]))
                else:    
                    probablity *=  ((language_model[a]))
                cnt+=1
            # print(probablity)
            perplexity = probablity**(-1/cnt)
            mean_perplexity += perplexity
            result_file_writer.writerow(data+[perplexity])

    result_file_writer.writerow([mean_perplexity])

    print(mean_perplexity/input_counter)
def compute_sheldon_3gram_perplexity(file):
    result_file = open("./P2_Phase1/Perplexity/"+str(file.name.split('/')[-2])+"/label1.perplexity.3gram.csv","w")
    result_file_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    language_model_file = open("./P2_Phase1/Model/label1.3gram.lm")
    language_model = {}

    for line in language_model_file:

        data = line.split("|")
        # print(data)
        language_model[tuple(data[:-1])] = float(data[-1][:-1])
    
    mean_perplexity = 0
    input_counter = 0
    for data in file:
        data = ["<s>"] + data.split() + ["</s>"]
        # print("\n///////",data)
        probablity = 1
        input_counter+=1
        if(len(data)>3):
            cnt = 0
            # print(data)
            for word_index in range( len(data) -2):
                a = tuple([data[word_index + i] for i in range(3)])
                if(a not in language_model.keys() ):
                    probablity *=  (language_model[tuple(["UNK","UNK","UNK"])])
                else:    
                    probablity *=  (language_model[a])
                
                cnt+=1
            # print(probablity)
            perplexity = probablity**(-1/cnt)
            mean_perplexity += perplexity
            result_file_writer.writerow(data+[perplexity])

    result_file_writer.writerow([mean_perplexity])

    print(mean_perplexity/input_counter)


    
print("leonard_train_1gram",end= ':')
compute_leonard_1gram_perplexity(open('./P2_Phase1/SplitedData/train/label2.txt', mode='r'))
print("leonard_train_2gram",end= ':')
compute_leonard_2gram_perplexity(open('./P2_Phase1/SplitedData/train/label2.txt', mode='r'))
print("leonard_train_3gram",end= ':')
compute_leonard_3gram_perplexity(open('./P2_Phase1/SplitedData/train/label2.txt', mode='r'))

print("leonard_test_1gram",end= ':')
compute_leonard_1gram_perplexity(open('./P2_Phase1/SplitedData/test/label2.txt', mode='r'))
print("leonard_test_2gram",end= ':')
compute_leonard_2gram_perplexity(open('./P2_Phase1/SplitedData/test/label2.txt', mode='r'))
print("leonard_test_3gram",end= ':')
compute_leonard_3gram_perplexity(open('./P2_Phase1/SplitedData/test/label2.txt', mode='r'))



print("sheldon_train_1gram",end= ':')
compute_sheldon_1gram_perplexity(open('./P2_Phase1/SplitedData/train/label1.txt', mode='r'))
print("sheldon_train_2gram",end= ':')
compute_sheldon_2gram_perplexity(open('./P2_Phase1/SplitedData/train/label1.txt', mode='r'))
print("sheldon_train_3gram",end= ':')
compute_sheldon_3gram_perplexity(open('./P2_Phase1/SplitedData/train/label1.txt', mode='r'))

print("sheldon_test_1gram",end= ':')
compute_sheldon_1gram_perplexity(open('./P2_Phase1/SplitedData/test/label1.txt', mode='r'))
print("sheldon_test_2gram",end= ':')
compute_sheldon_2gram_perplexity(open('./P2_Phase1/SplitedData/test/label1.txt', mode='r'))
print("sheldon_test_3gram",end= ':')
compute_sheldon_3gram_perplexity(open('./P2_Phase1/SplitedData/test/label1.txt', mode='r'))

