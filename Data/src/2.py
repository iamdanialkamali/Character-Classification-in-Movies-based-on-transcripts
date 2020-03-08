from bs4 import BeautifulSoup
import requests
import codecs
import csv
sheldon_file =  open('../sheldon.csv', mode='w')
leonard_file =  open('../leonard.csv', mode='w')
sheldon_commnets_writer = csv.writer(sheldon_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
leonard_commnets_writer = csv.writer(leonard_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
label1 = open('../label1.txt', mode='w')
label2 = open('../label2.txt', mode='w')




l = 0
s = 0
def get_data(url):
    global l
    global s
    local_s = 0
    local_l = 0
    transcript_page  = requests.get(url)
    transcript_page_html = BeautifulSoup(transcript_page.content)
    # try:
    for p in transcript_page_html.select("span"):
        if(len(p.contents) > 0 and "Sheldon:" in p.contents[0]):
            sheldon_commnets_writer.writerow([p.contents[0][8:].replace('�',"'")])
            label1.write(p.contents[0][8:].replace('�',"'")+'\n')
            s+=1
            local_s +=1
            print("local_s:",local_s)
            print("s:",s)
            # print(p.contents[0][8:])
        if(len(p.contents) > 0 and "Leonard:" in p.contents[0]):
            leonard_commnets_writer.writerow([p.contents[0][8:].replace('�',"'")])
            label2.write(p.contents[0][8:].replace('�',"'")+'\n')
            l+=1
            local_l +=1
            print("local_l:",l)
            print("l:",l)
    
    # except Exception:
    for p in transcript_page_html.select("p"):
        if(len(p.contents) > 0 and "Sheldon:" in p.contents[0]):
            print(p)
            sheldon_commnets_writer.writerow([p.contents[0][8:].replace('�',"'")])
            label1.write(p.contents[0][8:].replace('�',"'")+'\n')
            s+=1
            local_s +=1
            print("local_s:",local_s)
            print("s:",s)
            # print(p.contents[0][8:])
        if(len(p.contents) > 0 and "Leonard:" in p.contents[0]):
            leonard_commnets_writer.writerow([p.contents[0][8:].replace('�',"'")])
            label2.write(p.contents[0][8:].replace('�',"'")+'\n')
            local_l +=1
            print("local_l:",l)
            l+=1
            print("l:",l)
            
start = False
html  = requests.get("https://bigbangtrans.wordpress.com/series-1-episode-1-pilot-episode/")

html = BeautifulSoup(html.content)
for li in html.select('li'):
    ep = "page_item"
    if('class' in li.attrs and ep in  li['class'] ):
        if(start):
            try:
                print(li.contents)
                a = li.select('a')[0]
                get_data(a['href'])
            except Exception:
                print("ERR")
        start = True


label1.close()
label2.close()
sheldon_file.close()
leonard_file.close()
