import math
training_file = open("./P2_Phase1/ClsData/train.txt")
trainning_data = []
for line in training_file:
    trainning_data.append(line.strip())


stopwords = {"the", 
    'an', 'ourselves', 'we', 'any', 'very', 'is', 'nor', 'as',
    'then', 'all', 'again', "i've", 'i', 
    'would', 'both', 'those', 'this', 'can',
    'am',  'against', 'itself', "let's",
    "he'd", 'once',  'up', 'www', 'how', 'being', 'ever',
    'get', 'other', "aren't", 'do', 'it', 'to', 'out', "that's",
     'r', "she'd", 'that', "he'll", 'does',
     'some', 'such', 
    'below', 'down', "he's" 'until', "can't", 'because',
    'of', "they'll", 'him', 'having', 'could', 'through', 'his', "wasn't",
    'before', "we'd", 'too', 'com', "i'm", 'should', 'had', 'here', 'if',
    'in', 'has', 'their', 'or', "here's", 'over', 'about',
    'she', 'the', 'yourself', 'hers', 'k',  'ought',
    'more', 'and', 'just',  "hasn't",  'otherwise',
    'be', 'a', 'yourselves', 'were''with', "how's",
     'our', "you're", 'into',  'above', 'them',
    'was', 'by',  'on', 'own',  'between',
    'ours', 'under', 'herself', "they've", 'been', 
    "don't", 'they', 'few', "haven't", 'most', 
    'theirs', 'http',  "they're", 'you', "hadn't",
     'but', 'no', "doesn't", 'at', 'since', 'for', 'are', "mustn't", 'themselves', 
     'from', 'he', 'off', ":",",","." }

def extract_count_feature():
    lines_features = []

    for data in trainning_data:
        splitted_data = data.split()
        label = splitted_data[0]
        splitted_data = splitted_data[1:]
        features = {}
        for word in splitted_data:
            if word.lower() not in stopwords and ":" not in word.lower()  :
                features[word] = features.get(word,0) + 1
        ######################### triGRAM ###########################
        for index in range(len(splitted_data)-2):
            w1,w2,w3 = splitted_data[index] ,splitted_data[index+1],splitted_data[index+2]
            if(":" in w1 or ":" in w2 or ":" in w3):
                continue
            word = w1 + "|" + w2 + "|"+ w3
            features[word] = features.get(word,0) + 1

        # ######################### biGRAM ###########################
        # for index in range(len(splitted_data)-2):
        #     w1,w2 = splitted_data[index] ,splitted_data[index+1]
        #     if(":" in w1 or ":" in w2 ):
        #         continue
        #     word = w1 + "|" + w2 + "|"
        #     features[word] = features.get(word,0) + 1



        lines_features.append([label,features])
    return lines_features
features = extract_count_feature()
features_file = open("./P2_Phase1/ClsData/Maxent/input.train.txt","w")

for line_data in features:
    label = line_data[0]
    lines_features = line_data[1]
    lines_features["f_count"] = len(line_data[1].keys())
    for features in lines_features:
        label = label + " " +features + ":" + str(lines_features[features])
    features_file.write(label + "\n")

features_file.close()
print("WTF")



training_file = open("./P2_Phase1/ClsData/test.txt")
trainning_data = []
for line in training_file:
    trainning_data.append(line.strip())



def extract_count_feature():
    lines_features = []

    for data in trainning_data:
        splitted_data = data.split()
        label = splitted_data[0]
        splitted_data = splitted_data[1:]
        features = {}
        
        for word in splitted_data:
            if word.lower() not in stopwords and ":" not in word.lower()  :
                features[word] = features.get(word,0) + 1

        ######################## triGRAM ###########################
        for index in range(len(splitted_data)-2):
            w1,w2,w3 = splitted_data[index] ,splitted_data[index+1],splitted_data[index+2]
            if(":" in w1 or ":" in w2 or ":" in w3):
                continue
            word = w1 + "|" + w2 + "|"+ w3
            features[word] = features.get(word,0) + 1

        # ######################### biGRAM ###########################
        # for index in range(len(splitted_data)-2):
        #     w1,w2 = splitted_data[index] ,splitted_data[index+1]
        #     if(":" in w1 or ":" in w2 ):
        #         continue
        #     word = w1 + "|" + w2 
        #     features[word] = features.get(word,0) + 1
        lines_features.append([label,features])

    return lines_features
features = extract_count_feature()
features_file = open("./P2_Phase1/ClsData/Maxent/input.test.txt","w")

for line_data in features:
    label = line_data[0]
    lines_features = line_data[1]
    lines_features["f_count"]=len(line_data[1].keys())

   
    for features in lines_features:
        label = label + " " +features + ":" + str(lines_features[features])
    features_file.write(label + "\n")

features_file.close()
print("WTF")

