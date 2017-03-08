import os;

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size;

def get_names(path,freq):
    folders = os.listdir(path);

    for folder in folders:
        apath = path + "\\"+folder;
        #print(apath);
        if os.path.isdir(apath):
            if len(os.listdir(apath)) >= freq:
                print(folder);
                #print(folder);
                #if get_size(apath)/1024/1024 >= 3:
                    #print(folder);
                    #print(get_size(apath)/1024/1024);


get_names("./Data",150);