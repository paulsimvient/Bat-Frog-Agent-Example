
import math 

#create enumeration
class TestState:
    NotTesting, Testing, DoneTesting = range(3)
    
#testing evaluationstate
class EvaluationState:
   def __init__(self):
       self.state = TestState.NotTesting 
        
#song class that describes frequences of song over time
#frequencies is a dictionary, and is tested (hence bool)
class Frequencies:
    def __init__(self):
        self.frequencyList = {}
        self.changeFrequencyList = {}
         
#song spectrum of frequences      
class Song(Frequencies):
    def __init__(self):
        Frequencies.__init__(self)
        self.isPlaying = False
        
#audible spectrum of frequencies
class AudibleSpectrum(Frequencies):
    def __init__(self):
        Frequencies.__init__(self)
        self.isListening = False
        
        
#simple vector class
'''
 x = ax/|a|
 y = ay/|a|
 z = az/|a|
'''
class Vector:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
    #normalize vector
    
    def Normalize(self):
        length = sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z)) 
        self.x  = self.x/length
        self.y  = self.y/length
        self.z  = self.z/length
 
 #agent class
class Agent:
#Init constructor
  def __init__(self):
    self.Position = Vector()
    self.Orientation = Vector()
    self.Name = ""
    self.Predator = False
    
  def Update(self, Agent):
    return
   
   #not finished yet, get dot product between me/him
  def WhereAmIComparedToHim(self, OtherAgent):
    v = Vector()
    v = self.Position - OtherAgent.Position
    v.Normalize()
 
#derived class agent   
class Frog(Agent):
    def __init__(self): 
        self.Spectrum = Song()
        self.InTact = 100.0
        self.LastChange=0
        
        
    #try to come up w/ a different frequency
    def ReviseFrequency(self):
        #check amount of change to self, if it's going down, moving in right direction
        #try some changes now and again 
       
        testing = False
        evalState = None
        
        #zero out change in frequencies
        for key in self.Spectrum.changeFrequencyList.iterkeys(): 
            self.Spectrum.changeFrequencyList[key]=0.0
            
        #find testing frequency
        for key in self.Spectrum.frequencyList.iterkeys(): 
            evalState = self.Spectrum.frequencyList[key]  
            #if there are no testing states set, set one
            if evalState == TestState.Testing:
                testing = True
                break
            
            #no frequency being tested
            if testing == False:
                for key in self.Spectrum.frequencyList.iterkeys(): 
                    evalState = EvaluationState()
                    evalState.state = TestState.Testing
                    self.Spectrum.frequencyList[key]=evalState
                    testing = True
                    break
                  
                   
        if testing == True:
            val = key
            #for now just up the pitch
            val += .03 
           
            #remove old key
            del(self.Spectrum.frequencyList[key])
            self.Spectrum.frequencyList[val]=TestState.Testing
            
            #set frequency diff for that key
            self.Spectrum.changeFrequencyList[val] = .03
            return
     
    #do sing
    def SingToMate(self):
        return
    
    #derrived class
    def Update(self, Agent):
      
      #if this number changing faster than last iteration?  
      #state = self.LastChange - self.InTact
      self.SingToMate()
      
      if self.InTact > 0:
          self.ReviseFrequency()
      
#derived class agent   
class BlueTailedBat(Agent):
    def __init__(self):
        self.Spectrum = AudibleSpectrum()
      
    #derrived class  
    def Update(self, Agent):
           return    
       
       
  

