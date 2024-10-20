import pickle
import os

def getFilePath(file: str, file2: str = "", file3: str = "", orv: bool = False):
    if not orv:
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, file3)
        filename = os.path.join(filename, file2)
        filename = os.path.join(filename, file)
    else:
        filename = os.path.join(file3, file2)
        filename = os.path.join(filename, file)
    return filename

def getFileData(FileName: str, OriginalData, ParentFolder: str = "", ParentFolder2: str = "", orv: bool= False):
    filepath = getFilePath(FileName, ParentFolder, ParentFolder2, orv)
    if ( not os.path.exists(filepath) ):
        return OriginalData
    with open(filepath, "rb") as file:
        return pickle.load(file)

def writeFileData(FileName: str, data, ParentFolder: str = "", ParentFolder2: str = "", write: bool = True, orv: bool = False):
    filepath = getFilePath(FileName, ParentFolder, ParentFolder2, orv)
    if ( not os.path.exists(filepath) ):
        CreateFile(filepath)
        with open(filepath, "wb") as file:
            pickle.dump(data, file)
    elif write:        
        with open(filepath, "wb") as file:
            pickle.dump(data, file)

def checkFile(FileName: str, data, ParentFolder: str = "", ParentFolder2: str = "", write: bool = True):
    filepath = getFilePath(FileName, ParentFolder, ParentFolder2)
    return os.path.exists(filepath)

def CreateFile(file):
    with open(file, "x") as Openedfile:
        Openedfile.close

def makeFolder(folderName: str, Parentfolder: str = ""):
    folderpath = getFilePath(folderName, Parentfolder)
    if ( not os.path.exists(folderpath) ):
        os.mkdir(folderpath)


