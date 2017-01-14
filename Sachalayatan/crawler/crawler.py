
import requests;
from astropy.extern.bundled.six import print_
from bs4 import BeautifulSoup;
from builtins import print
import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path);
        return 1;
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            return 0;
        else:
            return 1;

file_names = dict();

def goo_for_it(max_page):
    make_sure_path_exists("Data")
    page = 2421;
    cnt = 17214;
    page_error = 0;
    while page <= max_page :
        url = "http://www.sachalayatan.com/?page="+str(page);
        print(url)

        try:
            source_code = requests.get(url);
        except Exception as e:
            page_error+=1;
            if page_error > 10:
                page+=1;
                page_error = 0;
            continue;
        plain_text = source_code.text;
        #print(plain_text);
        soup = BeautifulSoup(plain_text,'lxml');

        for link in soup.findAll('h2') :
            #title = link.string;
            #href = link.findall('a');
            #print(title);
            #print(href[0].get('href'));
            tolink = BeautifulSoup(str(link), 'lxml');

            ll = tolink.findAll('a');
            if len(ll) <=0 :
                continue;
            print(tolink.find('a').string);
            post_link = ll[0].get('href');
            print(post_link);
            contests = str(post_link).split("/");
            nodeId = contests[len(contests)-1];
            get_single_item_data(post_link,tolink.find('a').string,cnt,nodeId)
            cnt+=1;


            #get_single_item_data(href);
        page+=1;
        print("Page : "+str(page)+" complete. "+" Total files : "+str(cnt));


def get_single_item_data(item_url,title,cnt,nodeId):

    mystring = "";
    try :
        source_code = requests.get(item_url);
    except Exception as e:
        return ;
    plain_text = source_code.text;
    soup = BeautifulSoup(plain_text, 'lxml');

    for link in soup.findAll('div', {'class': 'content','id':"node-"+nodeId+"-content"}):
        text = BeautifulSoup(str(link), 'lxml').get_text();
        lines = text.split("\n");
        #print(text);

        leng = len(lines);
        if leng <= 0 :
            return ;
        now = 0;
        while now < leng :
            mystring+=lines[now];
            mystring+="\n"
            now+=1;

    folder = "";
    for link in soup.find_all('em',{'id':'node-shortcuts','class':'info'}):
        tolink = BeautifulSoup(str(link), 'lxml')
        try:
            folder = tolink.find('a').string;
        except Exception as e:
            continue;
    root_path = "Data" + "\\" + folder
    if make_sure_path_exists(root_path)==0:
        return ;
    #try:
        #file_names[folder] = file_names[folder] + 1;
    #except KeyError:
        #file_names[folder] = 1;
    number = len(os.listdir("./"+root_path)) + 1;
    file_name = folder+"_"+str(number) + ".doc";
    print("File name" + file_name);
    path = root_path+"\\" + file_name;
    fw = open(path, 'w', encoding='utf8');
    try:
        fw.write(title);
        fw.write("\n");
        fw.write("\n");
        fw.write("\n");
        fw.write(mystring);
    except :
        fw.close();
    fw.close();





goo_for_it(2421);
