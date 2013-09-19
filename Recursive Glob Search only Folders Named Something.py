import glob

'''Say you want to search for all text files under folders named 'December''''

path = 'C:\\' #your starting directory here
List = []
findThis = ['pass']#in order to start the while loop
search_params = '.txt' #file extension etc.
fldr_name = 'December'
while len(findThis) > 0: #While a downward search still produces results
    findThis = glob.glob(path)
    for item in findThis:
        if item.rsplit('\\',1)[0].endswith(fldr_name) == True:
            if item.endswith(search_params) == True: #Just eliminate the 'if' to return all paths
                List.append(item)
    path = path + '\\*'

for paths in List:
    print paths
