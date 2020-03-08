import nltk
import csv


label1 = []
label1_dict = {}
label1_cnt = 0
label2 = []
label2_dict = {}
label2_cnt = 0
with open("../../ProcessedData/postive_comments.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if(row[0] not in label1_dict.keys()):
            label1_dict[row[0]] = 1
        else:
            label1_dict[row[0]] = int(label1_dict[row[0]]) + 1
        label1.append(row[0])
        label1_cnt+=1

with open("../../ProcessedData/negative_comments.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        if(row[0] not in label2_dict.keys()):
            label2_dict[row[0]] = 1
        else:
            label2_dict[row[0]] = int(label2_dict[row[0]]) + 1
        label2.append(row[0])
        label2_cnt+=1

for i in label1_dict.keys():
    label1_dict[i] = label1_dict[i]/label1_cnt


for i in label2_dict.keys():
    label2_dict[i] = label2_dict[i]/label2_cnt


from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

stopwords = {"when's","the","but", 'doing', 'there', 'have', 'like', 'only', "you've",
'an', 'ourselves', 'we', 'any', 'very', 'is', 'nor', 'as',
'then', 'all', 'again', "i've", 'i', "they'd", "you'd",
'would', 'both', 'those', 'this', 'can', "weren't", 'who',
'am', 'where', 'my', 'against', "we've", 'itself', "let's",
"he'd", 'once', 'your', 'up', 'www', 'how', 'being', 'ever',
'get', 'other', "aren't", 'do', 'it', 'to', 'out', "that's",
"isn't", 'r', "she'd", 'while', 'that', "he'll", 'does', "why's",
"you'll", 'cannot', "we'll", 'some', 'such', "what's",
'below', 'down', "he's", 'which', 'until', "can't", 'because',
'of', "they'll", 'him', 'having', 'could', 'through', 'his', "wasn't",
'before', "we'd", 'too', 'com', "i'm", 'should', 'had', 'here', 'if',
'in', 'has', 'their', "where's", 'or', "here's", 'over', 'about',
'she', 'the', 'yourself', 'when', 'hers', 'k', 'myself', 'ought',
'more', 'and', 'just', 'whom', "hasn't", 'shall', 'otherwise',
'be', 'a', 'its', 'yourselves', 'were', 'what', 'with', "how's",
"she's", 'our', "there's", "you're", 'into', 'me', 'above', 'them',
'was', 'by', 'yours', 'on', 'own', "she'll", "won't", 'between',
'ours', 'under', 'herself', "they've", 'been', "we're", "i'd",
"don't", 'they', 'not', 'few', "haven't", 'most', 
'theirs', 'http', 'why', "they're", 'you', "hadn't",
"it's", 'but', 'no', "doesn't", 'at', 'since', 'for', 'are', "mustn't", 'themselves', 
"i'll", 'after', "couldn't", 'from', 'he', "didn't",
'further', "wouldn't", 'however', 'than', 'so', 'did', 'during', "shouldn't", "shan't",
'off', 'each', 'same', 'her', 'himself', 'these', 'else', "who's", 'also' , 'the'}


def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='black',
        max_words=100,
        max_font_size=50,
        stopwords=stopwords, 
        scale=3,
        random_state=1 
    ).generate_from_frequencies(data)

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud,interpolation="bilinear")
    plt.show()


def show_label1(stopword):
    wordcloud = WordCloud(
        background_color='black',
        max_words=100,
        max_font_size=50,
        scale=3,
        random_state=1 
    ).generate_from_frequencies(label1_dict)
    
    wordcloud.to_file('../out/'+str(4*stopword+1 ) + '.jpg')


def show_label2(stopword):
    wordcloud = WordCloud(
        background_color='black',
        max_words=100,
        max_font_size=50,
        scale=3,
        random_state=1 
    ).generate_from_frequencies(label2_dict)

    wordcloud.to_file('../out/'+str(4*stopword+2 ) + '.jpg')

def show_label1_diffrencial(stopword):
    label1_diffrencial = {}
    for i in label1_dict.keys():
        if(i in label2_dict.keys()):
            label2_count = float(label2_dict[i])
            label1_count = float(label1_dict[i])
            if((label1_count - label2_count)>0):
                label1_diffrencial[i]= label1_count - label2_count  
        else:
        
            label1_diffrencial[i] = float(label1_dict[i])
    # print(label1_diffrencial)
    wordcloud = WordCloud(
            background_color='black',
            max_words=100,
            max_font_size=50,
            scale=3,
            random_state=1 
        ).generate_from_frequencies(label1_diffrencial)

    wordcloud.to_file('../out/'+str(4*stopword+3 ) + '.jpg')

def show_label2_diffrencial(stopword):
    label2_diffrencial = {}

    for i in label2_dict.keys():
        if(i in label1_dict.keys()):
            label2_count = float(label2_dict[i])
            label1_count = float(label1_dict[i])
            if((label2_count - label1_count)>0):
                label2_diffrencial[i]= label2_count - label1_count  
        else:
        
            label2_diffrencial[i] = float(label2_dict[i])
  
    
    wordcloud = WordCloud(
            background_color='black',
            max_words=100,
            max_font_size=50,
            scale=3,
            random_state=1 
        ).generate_from_frequencies(label2_diffrencial)

    wordcloud.to_file('../out/'+str(4*stopword+4 ) + '.jpg')

# show_label1_diffrencial()
# show_label2_diffrencial()
# show_wordcloud(label1_dict)
# show_wordcloud(label2_dict)
# stopworded_label1


# for i in label1:
#     if (i in stopwords):
#         del i
       
# show_label2_diffrencial()

show_label1(0)
show_label2(0)
show_label1_diffrencial(0)
show_label2_diffrencial(0)

a = label1_dict.keys()
b = label2_dict.keys()
for i in stopwords:
    if(i in a):
        del label1_dict[i]
    if(i in b):
        del label2_dict[i]


show_label1(1)
show_label2(1)
show_label1_diffrencial(1)
show_label2_diffrencial(1)

