
#list utilities
class getlist:   
    #Init constructor, adds item to list
    def __init__(self,*number):
        self.lst=[]
        self.lst += number #I changed this to add all args to the list
    #prints list
    def printlist(self):
        return self.lst
    
    #reads a file into a dictionary
    def readFile(self, fileHandle): 
        line = fileHandle.readline() 
        dictName = {} 
        keycounter = 1 
   
        while line: 
            key = str(keycounter) 
            dictName[key] = line 
            keycounter = keycounter + 1 
            line = fileHandle.readline()
            
        return dictName