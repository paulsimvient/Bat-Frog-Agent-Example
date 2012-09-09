
# get sys for os current directory
import sys
import os
import copy

#get os directory
cwd = os.getcwd()
 
#import classes
from AgentLoader import * 
from ListUtility import *
from Agent import *

#Loads the agent data
class Main:
    def __init__(self): 
        self.FrogList = {}
        self.BatList = {}
  
    def Start(self):
        #spawn agents
        self.agentLoader = AgentLoader()
        self.agentLoader.LoadAgentData()         
        
        for ch in self.agentLoader.returnAgentList:
            if isinstance(ch, Frog):
                for i in range(100):
                    copyItem = copy.copy(ch)
                    self.FrogList[i] = copyItem
                  #make me two bats
            elif isinstance(ch, BlueTailedBat):
                for i in range(2):
                    copyItem = copy.copy(ch)
                    self.BatList[i] = copyItem        
                    
    #global update for the main class                 
    def Update(self):
         
        #doing generic update function
        for frogKey in self.FrogList.iterkeys():
           frog =  self.FrogList[frogKey]         
           for batKey in self.BatList.iterkeys():
               bat =  self.BatList[batKey]
               frog.Update(bat)
                     
 
MainClass = Main()
MainClass.Start()
while True:
    MainClass.Update()
