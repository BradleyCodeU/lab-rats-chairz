

class Weapon():
    #Constructor
    def init (self, name, color, size, elementfire, retractbutton):
        self.name = "Blade"
        self.color = "Silver"
        self.size = "Long"
        self.elementfire = False
        self.retractbutton = False
        self.descripion = "It's a very long, strong, silver blade that is retractable.  A switch on the sword can turn it into a fire sword."
    #Accessor
    def getColor(self):
        return self.color
    def getSize(self):
        return self.size
    #Mutator
    def setElementfire(self):
        if self.elementfire = False:
            self.elementfire = True
            print (self.size + self.color + self.name + "has now been enchanted with fire!")
        if self.elementfire = True:
            self.elementfire = False
            print (self.size + self.color + self.name + "has now been enchanted with lightning!")
        
    def setRetractbutton(self):
        if self.retractbutton = False:
            self.retractbutton = True
            print (self.name + self.color + self.name + "has now been put away.")
        if self.retractbutton = True:
            self.retractbutton = False
            print (self.name + self.color + self.name + "is now out and ready for combat.")
            
            
            
        
