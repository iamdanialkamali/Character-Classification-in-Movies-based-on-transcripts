import math

input_data = open("../input.txt","r").read().split()
input_data = ['s'] + input_data + ['/s']
language_model_file = open("../language_model.lm","r")
language_model = {}
lenght = 0
probablity = 1
cnt = 0
for line in language_model_file:
    data = line.split("|")
    lenght = len(data)-1
    language_model[tuple(data[:-1])] = float(data[-1][:-1])

# lenght = len(language_model.keys()[0])
for word_index in range( len(input_data) - lenght + 1):
    a = tuple([input_data[word_index + i] for i in range(lenght)])
    
    if(a not in language_model.keys() ):
        probablity +=  math.log2(language_model[tuple(lenght*["UNK"])])
    else:    
        probablity +=  math.log2(language_model[a])

    
    cnt+=1

perplexity = 2**(-probablity/cnt)
print(perplexity)      
# print(language_model)
