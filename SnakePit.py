Previous="False"
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
                    pickOne=input("What's the number of the sublevel would you like to see? Input nothing to go to the previous Selections.")
                    if pickOne=="":
                        if Previous=="False":
                            self.print_children()
                        else:
                            Previous.print_children()
                    elif pickOne==int:
                        self.children[pickOne].print_children()
testlvl2=level("testlvl2",[],"This is test level 2")
testlvl1=level("testlvl1",["testlvl2"],"")
testlvl1.print_children() #TODO: figure out if this works
