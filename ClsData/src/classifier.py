import math

class NaiveBayse():

    
    stopwords = {"the", 'doing', 'there', 'have', 'like', 'only', "you've",
    'an', 'ourselves', 'we', 'any', 'very', 'is', 'nor', 'as',
    'then', 'all', 'again', "i've", 'i', "they'd", "you'd",
    'would', 'both', 'those', 'this', 'can', "weren't",
    'am', 'my', 'against', "we've", 'itself', "let's",
    "he'd", 'once', 'your', 'up', 'www', 'how', 'being', 'ever',
    'get', 'other', "aren't", 'do', 'it', 'to', 'out', "that's",
    "isn't", 'r', "she'd", 'that', "he'll", 'does',
    "you'll", 'cannot', "we'll", 'some', 'such', 
    'below', 'down', "he's" 'until', "can't", 'because',
    'of', "they'll", 'him', 'having', 'could', 'through', 'his', "wasn't",
    'before', "we'd", 'too', 'com', "i'm", 'should', 'had', 'here', 'if',
    'in', 'has', 'their', 'or', "here's", 'over', 'about',
    'she', 'the', 'yourself', 'hers', 'k', 'myself', 'ought',
    'more', 'and', 'just',  "hasn't", 'shall', 'otherwise',
    'be', 'a', 'yourselves', 'were''with', "how's",
    "she's", 'our', "there's", "you're", 'into', 'me', 'above', 'them',
    'was', 'by', 'yours', 'on', 'own', "she'll", "won't", 'between',
    'ours', 'under', 'herself', "they've", 'been', "we're", "i'd",
    "don't", 'they', 'not', 'few', "haven't", 'most', 
    'theirs', 'http',  "they're", 'you', "hadn't",
    "it's", 'but', 'no', "doesn't", 'at', 'since', 'for', 'are', "mustn't", 'themselves', 
    "i'll", 'after', "couldn't", 'from', 'he', "didn't",
    'further', "wouldn't", 'however', 'than', 'so', 'did', 'during', "shouldn't", "shan't",
    'off', 'each', 'same', 'her', 'himself', 'these', 'else',
    'also',"n't","'ve" ,"'re" ,"'ll" ,"but'","''" ,"'here",":", 'the'
    ,"%","'t","!","$","'","&" , "'s",",",",",".","?","'m",""}

    labels = []
    labels_count = []
    labels_probs = []
    labels_words_counter = []
    labels_total_words_counter = []
    labels_words_probs = []
    vocab = []
    vocab_lenghts = 0
    vocab_lenghts1 = 0
    sentence_probs = []
    file_extra_name = ""
    def __init__(self,stop_words = stopwords,file_extra_name = ""):
        self.file_extra_name = file_extra_name
        self.stop_words = stop_words
    def train_from_file(self,training_file):
        trainning_data = []
        for line in training_file:
            trainning_data.append(line.strip())
        self.train(trainning_data)
    
    def fill_dict(self,training_data):
        for sentece in training_data:
            tokenized = sentece.split()

            if(tokenized[0] not  in self.labels):
                self.labels.append(tokenized[0])
                self.labels_count.append(0)
                self.labels_words_counter.append({"UNK":0})
                self.labels_total_words_counter.append(0)
                self.labels_words_probs.append({})
                self.labels_probs.append(0)
            index = self.labels.index(tokenized[0])
            self.labels_count[index] +=1

            for word in tokenized[1:]:
                word = word.lower()
                if(word not in self.stop_words):
                    if(word not in self.vocab):
                        self.vocab.append(word)
                        self.vocab_lenghts +=1                    
                
                    count = self.labels_words_counter[index].get(word,0)

                    self.labels_words_counter[index][word] = count +1
                    self.labels_total_words_counter[index] +=1


    def set_probablities(self):
        for label_index in range(len(self.labels)):
            
            label_words_counter = self.labels_words_counter[label_index]
            label_vocab_lenght = self.labels_total_words_counter[label_index]
            self.labels_probs[label_index] = self.labels_count[label_index]/sum(self.labels_count)
            for key in label_words_counter:
                self.labels_words_probs[label_index][key] = (label_words_counter[key] +1) / (label_vocab_lenght + self.vocab_lenghts)

    def get_probablity(self,word,label_index):
        return self.labels_words_probs[label_index].get(word,self.labels_words_probs[label_index].get('UNK'))

    def train(self,training_data):
        self.fill_dict(training_data)
        self.set_probablities()  
    
    def test_from_file(self,test_file):
        test_data = []
        for line in test_file:
            test_data.append(line.strip())
        self.test(test_data)


    def get_reports(self,true_answers,model_answers):
        report_file = open("./P2_Phase1/ClsModel/NaiveBayes/"+self.file_extra_name+".report.txt","w")

        labels_reports = []
        for label in self.labels:    
            report = {"tp":0,"tn":0,"fp":0,"fn":0,"recall":0,"precision":0,"F1":0}
            for index in range(len(true_answers)):
                if(model_answers[index] == label ):
                    if(model_answers[index] == true_answers[index]):
                        report['tp'] +=1
                    if(model_answers[index] != true_answers[index]):
                        report['fp'] +=1
                if(model_answers[index] != label ):
                    if(model_answers[index] == true_answers[index]):
                        report['tn'] +=1
                    if(model_answers[index] != true_answers[index]):
                        report['fn'] +=1
            precision = report['tp']/(report['tp']+report['fp'])
            recall = report['tp']/(report['tp']+report['fn'])
            F1 = 2*precision*recall/(precision+recall)
            report['recall'] = recall
            report['precision'] = precision
            report['F1'] = F1
            labels_reports.append(report)

        index = 0
        total_report = {"tp":0,"tn":0,"fp":0,"fn":0,"recall":0,"precision":0,"F1":0}
        for report in labels_reports:
            report_file.write(self.labels[index]  + "\n")
            report_file.write("RECALL: " + str(report['recall'] )+"\n" ) 
            report_file.write("Precison: " + str(report['precision'] )+"\n")
            report_file.write("F1: " + str(report['F1'])+"\n")
            for key in report:
                total_report[key] += report[key]
            index += 1
        
        report_file.write("##MACRO AVG\n")
        report_file.write("RECALL: " + str(total_report['recall']/len(labels_reports) )+"\n" ) 
        report_file.write("Precison: " + str(total_report['precision']/len(labels_reports) )+"\n")
        report_file.write("F1: " + str(total_report['F1']/len(labels_reports))+"\n")
        report_file.write("##MICRO AVG\n")
        report_file.write("Precision: " +str( total_report['tp']/(total_report['tp']+total_report['fp']))+"\n")
        report_file.write("Recall: " +str( total_report['tp']/(total_report['tp']+total_report['fn']))+"\n")
        report_file.write("F1: " + str( 2*precision*recall/(precision+recall))+"\n")
        report_file.close()    
        
        

    def test(self,test_data):
        tests_labels_probablity = []
        true_answers = []
        model_answers = []
        for sentence in test_data:
            sentence_labels_prob = []
            words = sentence.split()[1:]
            true_answers.append(sentence.split()[0])
            for label_index in range(len(self.labels)):
                label_probablity = math.log10(self.labels_probs[label_index])
                probality = label_probablity
                # probality = 0 #####   "Test CAse ha ba in javab mide akhe chera ???????????????   ://// " 
                for word in words:
                    word = word.lower()
                    if(word not in self.stop_words):
                        probality += math.log10(self.get_probablity(word,label_index))   
                sentence_labels_prob.append(probality)
            tests_labels_probablity.append(sentence_labels_prob)

    
        model_file = open("./P2_Phase1/ClsModel/NaiveBayes/"+self.file_extra_name+".output.txt","w")

        for sentence_probs in tests_labels_probablity:
            for label_index in range(len(sentence_probs)):
                model_file.write(self.labels[label_index] + " " + str(sentence_probs[label_index])+ " " ) 

            model_file.write("\n" ) 
            
            model_answers.append(self.labels[sentence_probs.index(max(sentence_probs))])

        self.get_reports(true_answers,model_answers)


ss = {
        "the",
        "in",
        "at",
        "on",
        "off",
        "by",
        "beside",
        "under",
        "over",
        "blow",
        "above","up","down","across","through","from","of","about","four",
        "with"
}



def run_testCase():
    test_naive_bayse =  NaiveBayse(file_extra_name="TestCase")
    testSet_training_file = open("./P2_Phase1/ClsData/TestCase/train.txt")
    testSet_test_file = open("./P2_Phase1/ClsData/TestCase/test.txt")
    test_naive_bayse.train_from_file(testSet_training_file)
    test_naive_bayse.test(testSet_test_file)

def run_main_dataset():
    main_naive_bayse =  NaiveBayse(stop_words=ss,file_extra_name="Test")
    training_file = open("./P2_Phase1/ClsData/train.txt")
    test_file = open("./P2_Phase1/ClsData/test.txt")
    main_naive_bayse.train_from_file(training_file)
    main_naive_bayse.test(test_file)

########################################## FOR RUNNING NB ON  TEST_CASES UNCOMMENT THIS PART ##################
run_testCase()
########################################## FOR RUNNING NB ON MAIN DATA  UNCOMMENT THIS PART ##################
# run_main_dataset()
