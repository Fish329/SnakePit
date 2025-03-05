class level:
    def __init__(self,name,children,details):
        self.name=name
        self.children=children
        self.details=details
    def print_children(self):
        print(self.name)
        if len(self.children)==0:
            print(self.details)
        else:
            itr=0
            for i in self.children:
                itr+1
                print(itr,":",i)
                while True:
                    pickOne=input("Which number sublevel would you like to see?")
                    if pickOne==int: #TODO: finish this
Animalia = level("Animalia",["Chordata"])
