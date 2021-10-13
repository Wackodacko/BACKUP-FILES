import time
import os 
import shutil

def main():
    deleteFolderCount=0
    deleteFileCount=0
    days=0
    path='/C:/Users/anaeo/Downloads/Story-Hub-3-main'
    
    seconds=time.time()-(days * 24 * 60 * 60)
    if os.path.exists(path):
        for rootFolder, folders,files in os.walk(path):
            if seconds >= getFileAge(rootFolder):
                removeFolder(rootFolder)
                deleteFolderCount +=1
                break
            else:
                for folder in folders:
                    folderPath=os.path.join(rootFolder, folder)
                    if seconds >= getFileAge(folderPath):
                        removeFolder(folderPath)
                        deleteFolderCount +=1

                for file in files:
                    filePath=os.path.join(rootFolder, file)
                    if seconds >= getFileAge(filePath):
                        removeFile(filePath)
                        deleteFileCount +=1 
        
        else:
            if seconds >= getFileAge(path):
                removeFile(path)
                deleteFileCount +=1
        
    else:
        print("Path Not Found")
        deleteFileCount +=1
    print("Total Folders Deleted: ")
    print(deleteFolderCount)
    print("Total Files Deleted: ")
    print(deleteFileCount)

def removeFolder(path):
    if not shutil.rmtree(path):
        print("Folder Is Removed Succsesfully")
    else:
        print("Unable To Delete Folder")

def removeFile(path):
    if not shutil.rmtree(path):
        print("File Is Removed Succsesfully")
    else:
        print("Unable To Delete File")

def getFileAge(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__=='__main__':
    main()
        
                 

    