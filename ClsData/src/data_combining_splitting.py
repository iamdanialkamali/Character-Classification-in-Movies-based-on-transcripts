
import codecs
import csv
import random


def combine_data(label1_input_file,label2_input_file):
    main_data = []
    sentence = "" 
    for line in label1_input_file:
        line  = line[:-1]
        sentence  = sentence + " " + line
        if(line == '</s>' ):
            data = "label1 " +  sentence[4:-4].strip()
            data = data.replace(",","")
            data = data.replace(".","")
            if(len(data)>13):
                main_data.append(data)
            sentence = ""
    sentence = "" 
    for line in label2_input_file:
        line  = line[:-1]
        sentence  = sentence + " " + line
        if(line == '</s>' ):
            data = "label2 " + sentence[4:-4].strip()
            data = data.replace(",","")
            data = data.replace(".","")
            if(len(data)>13):
                main_data.append(data)
            sentence = ""
    
    return main_data    



def split_data(main_data):
    data_count = len(main_data)
    test_data_count = int(data_count//5 )
    test_data =[]

    for i in range(test_data_count):
        data_index = random.randint(0,data_count-1)
        test_data.append(main_data[data_index])
        data_count -= 1
        del main_data[data_index]
    
    return main_data,test_data



def write_text_files(train_data,test_data):
    
    train_file =  open('../train.txt', mode='w')
    

    test_file =  open('../test.txt', mode='w')


    for data in train_data:

        train_file.write(data+'\n')
    
    for data in test_data:
        test_file.write(data+'\n')


    test_file.close()   
    train_file.close()
    return 1



label1_file = open("../../ProcessedData/token_label1.txt")
label2_file = open("../../ProcessedData/token_label2.txt")

combined_data = combine_data(label1_file,label2_file)

train_data,test_data  = split_data(combined_data)
write_text_files(train_data,test_data)
print("EXIT")
