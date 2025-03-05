class animalia:
    def __init__(self,name,sciName,level,details):
        name=self.name
        sciname=self.sciName
        pattern=self.pattern
        habitat=self.habitat
        level="Kingdom"
        details="The animal kingdom"
class Chordata(animalia):
    def __init__(self,name,sciName,level,details):
        super().__init__(name,sciName)
        level = "Phylum"
        details = "Phylum: Chordata"
class Reptilia(Chordata):
    def __init__(self,name,sciName,level,details):
        super().__init__(name,sciName)
        level = "Class"
        details = "Reptiles class" #TODO: finish writing all detail blocks
class Squamata(Reptilia):
    def __init__(self,name,sciName,level):
        super().__init__(name,sciName)
        level = "Order"
class Serpentes(Squamata):
    def __init__(self,name,sciName,level):
        super().__init__(name,sciName)
        level = "Suborder"
class Colubridae(Serpentes):
    def __init__(self,name,sciName,level):
        super().__init__(name,sciName)
        level = "Family"
class Carphophis(Colubridae):
    def __init__(self,name,sciName,level):
        super().__init__(name,sciName)
        level = "Family"
CAA = Carphophis