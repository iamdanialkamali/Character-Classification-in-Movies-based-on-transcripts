

def get_reports(true_answers,model_answers,file_extra_name,labels):
        report_file = open("./P2_Phase1/ClsData/NaiveBayes/"+file_extra_name+".report.txt","w")

        labels_reports = []
        for label in labels:    
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
            report_file.write(labels[index]  + "\n")
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
        
        
dataSet_output_file = open("./P2_Phase1/ClsData/NaiveBayes/Test.output.txt")
dataSet_test_file = open("./P2_Phase1/ClsData/test.txt")

dataSet_test_true_answers = []
for line in dataSet_test_file:
    dataSet_test_true_answers.append(line.split()[0])
dataSet_model_answers = []
for line in dataSet_output_file:
    data = line.split()
    if( float(data[1]) < float(data[3])   ):
        dataSet_model_answers.append(data[2])
    else:
        dataSet_model_answers.append(data[0])



get_reports(dataSet_test_true_answers,dataSet_model_answers,"TEST",list(set(dataSet_test_true_answers)))



testCase_output_file = open("./P2_Phase1/ClsData/NaiveBayes/TestCase.output.txt")
testCase_test_file = open("./P2_Phase1/ClsData/TestCase/test.txt")


testCase_test_true_answers = []
for line in testCase_test_file:
    testCase_test_true_answers.append(line.split()[0])
testCase_model_answers = []
for line in testCase_output_file:
    data = line.split()
    if(float(data[1]) < float(data[3])   ):
        testCase_model_answers.append(data[2])
    else:
        testCase_model_answers.append(data[0])


get_reports(testCase_test_true_answers,testCase_model_answers,"TestCase",list(set(testCase_test_true_answers)))

