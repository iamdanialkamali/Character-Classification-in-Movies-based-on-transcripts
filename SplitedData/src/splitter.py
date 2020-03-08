import codecs
import csv
import random

sheldon_main_file =  open('../../ProcessedData/token_sheldon_comments.csv', mode='r')
leonard_main_file =  open('../../ProcessedData/token_leonard_comments.csv', mode='r')

sheldon_text_file =  open('../../ProcessedData/token_label1.txt', mode='r')
leonard_text_file =  open('../../ProcessedData/token_label2.txt', mode='r')


def split_data(input_file):
    main_data = []
    sentence = "" 
    for line in input_file:
        line  = line[:-1]
        sentence  = sentence + " " + line
        if(line == '</s>' ):
            main_data.append(sentence[:])
            sentence = ""
        
    data_count = len(main_data)
    test_data_count = int(data_count//5 )
    test_data =[]

    for i in range(test_data_count):
        data_index = random.randint(0,data_count-1)
        test_data.append(main_data[data_index])
        data_count -= 1
        del main_data[data_index]
    
    return main_data,test_data


def write_text_files(name,train_data,test_data):
    
    train_file =  open('../train/'+str(name)+'.txt', mode='w')
    

    test_file =  open('../test/'+str(name)+'.txt', mode='w')


    for data in train_data:

        data = " ".join(data.split()[1:-1])
        train_file.write(data+'\n')
    
    for data in test_data:
        data = " ".join(data.split()[1:-1])
        test_file.write(data+'\n')


    test_file.close()
    train_file.close()
    return 1



def write_files(name,train_data,test_data):
    
    train_file =  open('../train/'+str(name)+'.csv', mode='w')
    
    train_writer = csv.writer(train_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    test_file =  open('../test/'+str(name)+'.csv', mode='w')

    test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for data in train_data:
        data = data.split()
        train_writer.writerow(data)
    
    for data in test_data:
        data = data.split()
        test_writer.writerow(data)

    test_file.close()
    train_file.close()
    return 1


sheldon_train_data ,sheldon_test_data = split_data(sheldon_text_file)
leonard_train_data ,leonard_test_data = split_data(leonard_text_file)

    
write_files('Sheldon',sheldon_train_data,sheldon_test_data)
write_files('Leonard',leonard_train_data,leonard_test_data)

write_text_files('label1',sheldon_train_data,sheldon_test_data)
write_text_files('label2',leonard_train_data,leonard_test_data)
