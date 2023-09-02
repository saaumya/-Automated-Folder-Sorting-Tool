import os, shutil

# taking all the fie names present in temp folder
allfilesnames = os.listdir(r'C:\Users\saumy\OneDrive\Documents\Python\Project\temp')
print(allfilesnames)

# create unique list of extensions
extn =[]
onlyfiles =[]
# print(onlyfiles)
for x in allfilesnames:
    if('.' in x):
        tempextn = x.split('.')[1]
        # print(tempextn)
        extn.append(tempextn)
        # print(extn)
        onlyfiles.append(x)
        # print(x)

# to price unique value we used set
extn = list(set(extn))
print(extn)

print(onlyfiles)

# creating folders for the extension
for x in extn:
    foldername = r'C:/Users/saumy/OneDrive/Documents/Python/Project/temp/'+x
    try:
        os.mkdir(foldername)
    except FileExistsError as err:
        print(x , "Folder already exists please ignore")


# Move the respective file in to the folders

for x in onlyfiles:
    sourcepath = r'C:/Users/saumy/OneDrive/Documents/Python/Project/temp/'+x
    tempfile = x.split('.')
    extnname = tempfile[1]
    destpath = r'C:/Users/saumy/OneDrive/Documents/Python/Project/temp/'+ extnname
    shutil.move(sourcepath,destpath)

print("completed")