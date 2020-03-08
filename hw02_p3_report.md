# Naive Bayes
##MACRO AVG
RECALL: 0.6799273364557818
Precison: 0.6799273364557818
F1: 0.6799273364557818
##MICRO AVG
Precision: 0.6773542034839687
Recall: 0.6773542034839687
F1: 0.6433962264150943

# MaxEnt

## bigram


-------------------- Trial 0  --------------------

Trial 0 Training MaxEntTrainer,gaussianPriorVariance=1.0 with 15848 instances
Trial 0 Training MaxEntTrainer,gaussianPriorVariance=1.0 finished
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 Test Data Confusion Matrix
Confusion Matrix, row=true, column=predicted  __accuracy=0.6647311285029033__ most-frequent-tag baseline=0.5352183791971724
     label   0   1  |total
  0 label1 1562 558  |2120
  1 label2 770 1071  |1841

Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data precision(label1) = 0.6698113207547169
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data precision(label2) = 0.6574585635359116
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data recall(label1) = 0.7367924528301887
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data recall(label2) = 0.5817490494296578
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data F1(label1) = 0.701707097933513
Trial 0 Trainer MaxEntTrainer,gaussianPriorVariance=1.0 test data F1(label2) = 0.6172910662824207

MaxEntTrainer,gaussianPriorVariance=1.0
Summary. test precision(label1) mean = 0.6698113207547169 stddev = 0.0 stderr = 0.0
Summary. test precision(label2) mean = 0.6574585635359116 stddev = 0.0 stderr = 0.0
Summary. test recall(label1) mean = 0.7367924528301887 stddev = 0.0 stderr = 0.0
Summary. test recall(label2) mean = 0.5817490494296578 stddev = 0.0 stderr = 0.0
Summary. test f1(label1) mean = 0.701707097933513 stddev = 0.0 stderr = 0.0
Summary. test f1(label2) mean = 0.6172910662824207 stddev = 0.0 stderr = 0.0

## Result

ba tavajoh be natayeje bala mibinim ke __MaxEent__ natijeh behtari az __NaiveBayes__ dashte yeki az dalayele asli oon feature feature overlap hast ke dar  __MaxEent__ be khoobi handel shode 

hamoon tor ke mibinid deghate nazdik be yek digar be dast oomade 

# BEST EFFORT
chon hes kardam natayej zaif hastand be onvane ye binnade serial khdoam saie kardam classify koanm ke az 20 morede testi random 16 ta dorost bood age max ro male man dar nazar begirim natijeye classifier ha bad be nazar nemirese  