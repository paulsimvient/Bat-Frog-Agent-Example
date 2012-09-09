
#song class that describes frequences of song over time
class Frequencies:
    def __init__(self):
        self.frequencyList = []
         
#song spectrum of frequences      
class Song(Frequencies):
    def __init__(self):
        self.isPlaying = False
        
#audible spectrum of frequencies
class AudibleSpectrum(Frequencies):
    def __init__(self):
        self.isListening = False
        
        
#simple vector class
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
   
  def WhereAmIComparedToHim(self, OtherAgent):
    v = Vector()
    v = self.Position - OtherAgent.Position
    v.Normalize()
 
#derived class agent   
class Frog(Agent):
    def __init__(self):
        self.Spectrum = Song()
        
    #derrived class
    def Update(self, Agent):
           return    
      
#derived class agent   
class BlueTailedBat(Agent):
    def __init__(self):
        self.Spectrum = AudibleSpectrum()
      
    #derrived class  
    def Update(self, Agent):
           return    
       
       
  

