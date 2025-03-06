print("""
 ######  ##    ##    ###    ##    ## ########    ########  #### ########
##    ## ###   ##   ## ##   ##   ##  ##          ##     ##  ##     ##   
##       ####  ##  ##   ##  ##  ##   ##          ##     ##  ##     ##   
 ######  ## ## ## ##     ## #####    ######      ########   ##     ##   
      ## ##  #### ######### ##  ##   ##          ##         ##     ##   
##    ## ##   ### ##     ## ##   ##  ##          ##         ##     ##   
 ######  ##    ## ##     ## ##    ## ########    ##        ####    ##   
Welcome to the Snake Pit!
all snake images sourced from Wikipedia. Thank you to the Wikipedia editors for keeping the information accurate!
All snakes in this list are nonvenomous.""")
class kingdom:
    def __init__(self,name,details): #define all the kinds of levels
        self.name=name
        self.details=details
class phylum(kingdom):
    def __init__(self,name,details):
        super().__init__(name,details)
class classlevel(phylum): #won't let me just call it class
    def __init__(self,name,details):
        super().__init__(name,details)
class order(classlevel):
    def __init__(self,name,details):
        super().__init__(name,details)
class suborder(order):
    def __init__(self,name,details):
        super().__init__(name,details)
class family(suborder):
    def __init__(self,name,details):
        super().__init__(name,details)
class genus(family):
    def __init__(self,name,details):
        super().__init__(name,details)
class snake:
    def __init__(self,name,comname,details,k,p,c,o,so,f,g):
        self.name=name
        self.comname=comname
        self.details=details
        self.k=k
        self.p=p
        self.c=c
        self.o=o
        self.so=so
        self.f=f
        self.g=g
#Declare levels:
animalia=kingdom("Animalia","Organisms in the Animalia kingdom are called animals. Usually, animals consume organic material, breathe oxygen, can move, reproduce sexually, etc.")
chordata=phylum("Chordata","All chordates have 5 properties that separate them from other taxa. these are a notochord, hollow dorsal nerve cord, an endostyle or thyroid, pharyngeal slits, and a post-anal tail.")
reptilia=classlevel("Reptilia","Reptiles are a group of cold-blooded tetrapods with amniotic development.")
squamata=order("Squamata","Squamata is the largest order of reptiles, comprized of lizards and snakes. Squamata are characterized by their scales, and molting, which is the shedding of a dead layer of skin.")
serpentes=suborder("Serpentes","This is a suborder of Squamata, an order containing lizards and snakes. Serpentes contains only snakes. Snakes are cold-blooded amniote vertebrates. They are covered in scales, and most of them have a peculiar skull shape that allows them to swallow large eggs.")
colubridae=family("Colubridae","The snakes of this family are extremely diverse, no one common trait describing them all, except that they are all snakes.")
carphophis=genus("Carphophis","Commonly called Worm Snakes, this genus contains only two species of snakes. They are small snakes, usually with brown coloring and a pink or orange underside.")
cemophora=genus("Cemophora","These snakes are commonly known as scarlet snakes. Both species are only found in the US.")
pantherophis=genus("Pantherophis","The 10 snakes in this genus are very terrestial constricter snakes. Common names for some of the snakes are ratsnakes, foxsnakes, and cornsnakes.")
coluber=genus("Coluber","This genus contains only one species of snake, the Coluber Constricter.")
lampropeltis=genus("lampropeltis","commonly called Kingsnakes, the snakes of this genus eat other snakes!! Some kingsnakes are muted brown in color, but others are more colorful with red, yellow, gray, and lavender coloring.")
heterodon=genus("Heterodon","The upturned snouts of these snakes have earned them the name Hognose snakes. Those poor guys. They have distinct threatening tactics.")
regina=genus("Regina","The snakes in this genus are semiaquatic. They get their common name, crayfish snakes, from their primary diet.")
opheodrys=genus("Opheodrys","A genus containing two green snakes, of opposite scale-smoothness.")
nerodia=genus("Nerodia","A genus of heavy snakes that vary in size. They have flat heads, with varying patterns per species. usually brown or olive-green colored.")
CAA=snake("Carphophis amoneus amoneus","Eastern Worm Snake","A brown snake that can be found in moist places under rocks, rotting wood, piles of leaves, and others. They can't bite you, but they probably might produce foul-smelling excretions.",animalia,chordata,reptilia,squamata,serpentes,colubridae,carphophis)
#TODO: finish writing all the snakes.
