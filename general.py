import os

#each website crawled is a seperate folder

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating directory "+directory)
        os.makedirs(directory)

#create_user_file function will create all files requested
# 'queue.txt will store the lsit of files currently in the waiting-list
# 'crawled.txt' will store the list of files scrawled
def create_user_file(project_name,base_url):
    queue = project_name +'/queue.txt'
    crawled = project_name +'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)

    if not os.path.isfile(crawled):
        write_file(crawled,'')


def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()


# add data onto an existing file
def append_to_file(path,data):
    with open(path ,'a') as f:
        f.write(data+'\n')

# remove data onto an existing file
def delete_file_contents(path):
    with open(path,'w') as f:
        pass

#function to read each line and convert each line staement to a set
def file_to_set(file_name):
    results= set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def set_to_file(links,file_name):
    delete_file_contents(file_name)
    with open(file_name,'w') as f:
        for link in sorted(links):
            append_to_file(file_name,link)
