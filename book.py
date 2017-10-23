class Book():
    # Constructor
    def __init__(self,name,material,color):
        self.name = "Diary of a Wimpy Kid"
        self.material = "Paperback"
        self.color = "Red"
            
    # Accessor
    def getBack(self):
        return self.material
    def getColor(self):
        return self.color

    #Mutator
    def changeName(self, newColor):
        self.color = newColor

    def changeBack(self, newMaterial):
        self.material = newMaterial
        

    
        
        

