from nltk.tokenize import TweetTokenizer
import csv
import nltk
tknzr = TweetTokenizer()

label1 =  open("../../Data/label1.txt")
label2 =  open("../../Data/label2.txt")

label1_text = ""

label2_text = ""


for lin in label1:
        line1 = " <s> "+ lin +" </s> " 
        label1_text += line1
for lin in label2:
        line2 = " <s> "+ lin +" </s>  " 
        label2_text += line2
label1_tokens = tknzr.tokenize(label1_text)
label2_tokens = tknzr.tokenize(label2_text)

# label1_tokens = label1_text.split()
# label2_tokens = label2_text.split()

stemmer = nltk.PorterStemmer()

# token_sheldon_file =  open('../token_sheldon_comments.csv', mode='w')
# token_leonard_file =  open('../token_leonard_comments.csv', mode='w')
# token_sheldon_commnets_writer = csv.writer(token_sheldon_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
# token_leonard_commnets_writer = csv.writer(token_leonard_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
token_label1 = open('../token_label1.txt', mode='w')
token_label2 = open('../token_label2.txt', mode='w')

for stem in label1_tokens:
        # token_sheldon_commnets_writer.writerow([stem])
        token_label1.write(stem+"\n")
for stem in label2_tokens:
        # token_leonard_commnets_writer.writerow([stem])
        token_label2.write(stem+"\n")
token_label1.close()
token_label2.close()
# token_sheldon_file.close()
# token_leonard_file.close()




label1_stemmed_words = list(map(stemmer.stem, label1_tokens))
label2_stemmed_words = list(map(stemmer.stem, label2_tokens))


sheldon_file =  open('../sheldon_comments.csv', mode='w')
leonard_file =  open('../leonard_comments.csv', mode='w')
sheldon_commnets_writer = csv.writer(sheldon_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
leonard_commnets_writer = csv.writer(leonard_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
label1 = open('../label1.txt', mode='w')
label2 = open('../label2.txt', mode='w')

for stem in label1_stemmed_words:
        sheldon_commnets_writer.writerow([stem])
        label1.write(stem+"\n")
for stem in label2_stemmed_words:
        leonard_commnets_writer.writerow([stem])
        label2.write(stem+"\n")
label1.close()
label2.close()
sheldon_file.close()
leonard_file.close()


