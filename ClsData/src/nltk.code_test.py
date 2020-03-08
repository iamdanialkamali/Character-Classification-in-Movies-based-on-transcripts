import nltk


import math
from nltk.tokenize import word_tokenize # or use some other tokenizer

class NaiveBayse():

    
    
    def train_from_file(self,training_file):
        trainning_data = []
        for line in training_file:
            data  = line.strip().split()
            data = (" ".join(data[1:]),data[0])
            trainning_data.append(data)
        self.train(trainning_data)
    
    
    def train(self,training_data):
        all_words = set(word.lower() for passage in training_data for word in word_tokenize(passage[0]))
        t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in training_data]
        self.classifier = nltk.NaiveBayesClassifier.train(t)
        

    def test(self,test_data):
        all_words = set(word.lower() for passage in test_data for word in word_tokenize(passage[0]))
        t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in test_data]
        print("Classifier accuracy percent:",(nltk.classify.accuracy(self.classifier, t))*100)
        print("wtf")
    
    def test_from_file(self,test_file):
        test_data = []
        for line in test_file:
            data  = line.strip().split()
            data = [" ".join(data[1:]),data[0]]
            test_data.append(data)
        self.test(test_data)


    # def get_reports(self,true_answers,model_answers):
    #     report_file = open("./P2_Phase1/ClsData/NaiveBayes/"+self.file_extra_name+".report.txt","w")

    #     labels_reports = []
    #     for label in self.labels:    
    #         report = {"tp":0,"tn":0,"fp":0,"fn":0,"recall":0,"precision":0,"F1":0}
    #         for index in range(len(true_answers)):
    #             if(model_answers[index] == label ):
    #                 if(model_answers[index] == true_answers[index]):
    #                     report['tp'] +=1
    #                 if(model_answers[index] != true_answers[index]):
    #                     report['fp'] +=1
    #             if(model_answers[index] != label ):
    #                 if(model_answers[index] == true_answers[index]):
    #                     report['tn'] +=1
    #                 if(model_answers[index] != true_answers[index]):
    #                     report['fn'] +=1
    #         precision = report['tp']/(report['tp']+report['fp'])
    #         recall = report['tp']/(report['tp']+report['fn'])
    #         F1 = 2*precision*recall/(precision+recall)
    #         report['recall'] = recall
    #         report['precision'] = precision
    #         report['F1'] = F1
    #         labels_reports.append(report)

    #     index = 0
    #     total_report = {"tp":0,"tn":0,"fp":0,"fn":0,"recall":0,"precision":0,"F1":0}
    #     for report in labels_reports:
    #         report_file.write(self.labels[ index]  + "\n")
    #         report_file.write("RECALL: " + str(report['recall'] )+"\n" ) 
    #         report_file.write("Precison: " + str(report['precision'] )+"\n")
    #         report_file.write("F1: " + str(report['F1'])+"\n")
    #         for key in report:
    #             total_report[key] += report[key]
    #         index += 1
        
    #     report_file.write("##MACRO AVG\n")
    #     report_file.write("RECALL: " + str(total_report['recall']/len(labels_reports) )+"\n" ) 
    #     report_file.write("Precison: " + str(total_report['precision']/len(labels_reports) )+"\n")
    #     report_file.write("F1: " + str(total_report['F1']/len(labels_reports))+"\n")
    #     report_file.write("##MICRO AVG\n")
    #     report_file.write("Precision: " +str( total_report['tp']/(total_report['tp']+total_report['fp']))+"\n")
    #     report_file.write("Recall: " +str( total_report['tp']/(total_report['tp']+total_report['fn']))+"\n")
    #     report_file.write("F1: " + str( 2*precision*recall/(precision+recall))+"\n")
    #     report_file.close()    
        
        

        


def run_testCase():
    test_naive_bayse =  NaiveBayse()
    testSet_training_file = open("./P2_Phase1/ClsData/TestCase/train.txt")
    testSet_test_file = open("./P2_Phase1/ClsData/TestCase/test.txt")
    test_naive_bayse.train_from_file(testSet_training_file)
    test_naive_bayse.test(testSet_test_file)

def run_main_dataset():
    main_naive_bayse =  NaiveBayse()
    training_file = open("./P2_Phase1/ClsData/train.txt")
    test_file = open("./P2_Phase1/ClsData/test.txt")
    main_naive_bayse.train_from_file(training_file)
    main_naive_bayse.test(test_file)


run_testCase()
# run_main_dataset()


