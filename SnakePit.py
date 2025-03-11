print("""
 ######  ##    ##    ###    ##    ## ########    ########  #### ########
##    ## ###   ##   ## ##   ##   ##  ##          ##     ##  ##     ##   
##       ####  ##  ##   ##  ##  ##   ##          ##     ##  ##     ##   
 ######  ## ## ## ##     ## #####    ######      ########   ##     ##   
      ## ##  #### ######### ##  ##   ##          ##         ##     ##   
##    ## ##   ### ##     ## ##   ##  ##          ##         ##     ##   
 ######  ##    ## ##     ## ##    ## ########    ##        ####    ##   
Welcome to the Snake Pit!
Most snake images, unless specified, were sourced from Wikipedia. Thank you to the Wikipedia editors for keeping the information accurate!
The information in the Snake Pit is sourced from the Department of New Jersey's "Snakes of New Jersey" pamphlet and Wikipedia.
All snakes in this list are nonvenomous.""")
CAA=("Carphophis amoneus amoneus") #placeholders for the 12 snakes
CCC=("Cemophora coccinea copei")
CCConstr=("Coluber constrictor constrictor")
PG=("Pantherophis guttatus")
PO=("Pantherophis alleghaniensis")
HP=("Heterodon platirhinos")
LGG=("Lampropeltis getula getula")
LT=("Lampropeltis triangulum")
NSS=("Nerodia sipedon sipedon")
OA=("Opheodrys aestivus")
OV=("Opheodrys vernalis")
RS=("Regina septemvittata")


allsnakes=[CAA,CCC,CCConstr,PG,PO,HP,LGG,LT,NSS,OA,OV,RS] #list of all the snakes for classes to interact with
class kingdom: #superclass
    def __init__(self,name,details,snakes): #define all the kinds of levels
        self.name=name
        self.details=details
        self.snakes=snakes
        self.level="Kingdom"
    def printLevel(self): #print the details of this level
        print("")
        print("=[",self.level," ",self.name,"]=",sep="") #print the level name
        print(self.details) #print level description
        print("")
        print("[Snakes in this list that are in this level:]")
        iter=0
        for x in self.snakes: #go through the list of snakes and print them
            iter+=1
            print(iter,": ",x,sep="")
        input("Input anything to return to the SnakeDex.") #I couldn't get viewing snake details to work. since the snakes are declared after the taxonomy classes, and the snake objects are dependent on the taxonomy classes, I don't think there's a way to rearrange it so you can view properties of an object that does not yet exist in the current line.
        snakeDex()
        return
class phylum(kingdom): #define all the subclasses
    def __init__(self,name,details,snakes):
        super().__init__(name,details,snakes)
        level="Phylum"
class classlevel(phylum): #won't let me just call it class
    def __init__(self,name,details,snakes):
        super().__init__(name,details,snakes)
        level="Class"
class order(classlevel):
    def __init__(self,name,details,snakes):
        super().__init__(name,details,snakes)
        level="Order"
class suborder(order):
    def __init__(self,name,details,snakes):
        super().__init__(name,details,snakes)
        level="Suborder"
class family(suborder):
    def __init__(self,name,details,snakes):
        super().__init__(name,details,snakes)
        level="Family"
class genus(family):
    def __init__(self,name,details,snakes):
        super().__init__(name,details,snakes)
        level="Genus"
class snake: #Snake has a scientific name, common name, ASCII art picture, a description, and taxonomy in that order.
    def __init__(self,name,comname,picture,details,k,p,c,o,so,f,g):
        self.name=name
        self.comname=comname
        self.picture=picture
        self.details=details
        self.k=k
        self.p=p
        self.c=c
        self.o=o
        self.so=so
        self.f=f
        self.g=g
    def snake(self): #print snake bio
        print("")
        print("=[",self.name, " (",self.comname,") ]=", sep="") #print snake name
        print(self.picture) #print snake picture
        print(self.details) #print snake description
        print("")
        print("[TAXONOMY:]") #print taxonomic levels
        print("1. Kingdom:",self.k.name)
        print("2. Phylum:",self.p.name)
        print("3. Class:",self.c.name)
        print("4. Order:",self.o.name)
        print("5. Suborder:",self.so.name)
        print("6. Family:",self.f.name)
        print("7. Genus:",self.g.name)
        while True: 
            choice=input("Input 0 to return to SnakeDex, or input the number of a Taxonomy level to see details about it. ")
            try:
                choice=int(choice) #try again if the user input is not an integer
            except:
                print("ERROR: please input a whole number.")
                continue
            choice=int(choice)
            if choice > 7 or choice < 0: #if the user integer is out of range, try again
                print("ERROR: there is no item at that index. please choose from the list given.")
                continue
            else: #if the user's integer is within range, print level accordingly
                if choice==0:
                    snakeDex()
                elif choice==1:
                    self.k.printLevel()
                elif choice==2:
                    self.p.printLevel()
                elif choice==3:
                    self.c.printLevel()
                elif choice==4:
                    self.o.printLevel()
                elif choice==5:
                    self.so.printLevel()
                elif choice==6:
                    self.f.printLevel()
                elif choice==7:
                    self.g.printLevel()
                return
                
        
#Declare levels:
animalia=kingdom("Animalia","Organisms in the Animalia kingdom are called animals. Usually, animals consume organic material, breathe oxygen, can move, reproduce sexually, etc.",allsnakes)
chordata=phylum("Chordata","All chordates have 5 properties that separate them from other taxa. these are a notochord, hollow dorsal nerve cord, an endostyle or thyroid, pharyngeal slits, and a post-anal tail.",allsnakes)
reptilia=classlevel("Reptilia","Reptiles are a group of cold-blooded tetrapods with amniotic development.",allsnakes)
squamata=order("Squamata","Squamata is the largest order of reptiles, comprized of lizards and snakes. Squamata are characterized by their scales, and molting, which is the shedding of a dead layer of skin.",allsnakes)
serpentes=suborder("Serpentes","This is a suborder of Squamata, an order containing lizards and snakes. Serpentes contains only snakes. Snakes are cold-blooded amniote vertebrates. They are covered in scales, and most of them have a peculiar skull shape that allows them to swallow large eggs.",allsnakes)
colubridae=family("Colubridae","The snakes of this family are extremely diverse, no one common trait describing them all, except that they are all snakes.",allsnakes)
carphophis=genus("Carphophis","Commonly called Worm Snakes, this genus contains only two species of snakes. They are small snakes, usually with brown coloring and a pink or orange underside.",[CAA])
cemophora=genus("Cemophora","These snakes are commonly known as scarlet snakes. Both species are only found in the US.",[CCC])
pantherophis=genus("Pantherophis","The 10 snakes in this genus are very terrestial constricter snakes. Common names for some of the snakes are ratsnakes, foxsnakes, and cornsnakes.",[PG])
coluber=genus("Coluber","This genus contains only one species of snake, the Coluber Constricter.",snakes=[CCConstr])
lampropeltis=genus("lampropeltis","commonly called Kingsnakes, the snakes of this genus eat other snakes!! Some kingsnakes are muted brown in color, but others are more colorful with red, yellow, gray, and lavender coloring.",[LGG,LT])
heterodon=genus("Heterodon","The upturned snouts of these snakes have earned them the name Hognose snakes. Those poor guys. They have distinct threatening tactics.",[HP])
regina=genus("Regina","The snakes in this genus are semiaquatic. They get their common name, crayfish snakes, from their primary diet.",[RS])
opheodrys=genus("Opheodrys","A genus containing two similar looking green snakes, of opposite scale-smoothness.",[OA,OV])
nerodia=genus("Nerodia","A genus of heavy snakes that vary in size. They have flat heads, with varying patterns per species. usually brown or olive-green colored.",[NSS])
#Declare snakes:
CAA=snake("Carphophis amoneus amoneus","Eastern Worm Snake","""xX$$$$$x+;+xxx+++++++xXXxxxxXXXXXXXXxxx+x++++;;;+++;;;;;;;+;;;++;.+;+xXXXXxX+;;;;;+xXx+xx:+XXx++x;.::
$x+x++++++x;+;;;;++++;+xxXX$$$XXXXX+;;;::::::::;;+;::::::;+;;;;+xX$+++xX$$x+++++XXx++x+xx;:+X++;;:.:;
;+xx++;;;x+Xx+;+;;++xxXXxxXXxx++++;;;::;:::::++;::::;::::::::::;++++:;+XXxx+;++x++;+++++xx+x+xXx;;++;
XXXx+;+xxxXXxx++xx++;;++xx++++;;;;;;;;;;:::.:;;;+::::::.:::::;++++++++xx++xxx+xXxXXx++xxxxxXXXx+xXXXx
$++;;++++xx+xXx+++;;;;;+Xx++++;;;::.:::::::::;:;+;.::..:...:;+x+;;;+x+;+xXxxXXx+;x+xxX$Xx+x++xxxxx+XX
;;;;;;;++xXxx;;:::;;;;;;++++++;;:::;x+;..;;+;:.......:::.::;+x+;+xxx+xxxxXXxxx+++;+:;xXX$x$xx;:::::xx
:+;;+x$$XXx;:::::;;;:;;;+;::::;+::::;;+xxx+;::::::;;:.::;;::;++xxxxxxxxxxxxxXxxX$X+:::::::xx::::;+++$
;+xx$Xx;;xx+++::::;;;;;;;;;:::::::;:::.:::+;;::;;:::::;::;:;++xxXXXXXXXXxxxxxxXxxx+xX$X+;;:;::;;;;;+X
.;::;+$X+XxxxXxx++x++;;Xxx+;++;++xxxxx+;;++xx;;;::::++:::;+++xxXXX$$$$$XxxxxxxxxX$XXXXXxX&::;+;;:;;x$
.::;$&&$x+++;++;;;++;+;;xXXxxxxxxxxxxxxxxxxx+;;;::;;::++;:++xxXXX$$$$$$$Xx+++xxxXx;++xXXXx;;;++++:+xX
+x$X+x$$$XX+;;$&$x;;:;;xxXxxxxxxxXxXxxxxxxxxxx+.::::::::;;+;+xxxX$$$$$$$Xx+;++xxXX;;;;xxx+xXx++++xx++
;::.::::;:::::xXXxxXXx:;;xXXXXXXXXXXXXxxxxxxx+xx+:;::::::;+;++xxxXXXXXX$Xx+++xxX$X++;;+xXXxXXXxxxxx++
:::::::;;::::$x+;+XxxXX$$$$X$$X$$$$XXXXxxxxxxxxxxx;::::::;+++xxxxxXxxxxXXx++xxXXXx+;;;;;;++xxxxx+++;;
::;;:;+;;;;:X+;+xxxxXXX$$$$$$$$$$$XXXXXXxx+++xxxxXx;;;:::;++;+xx+xXX++xx++xxX$$$Xxx+;;;;;;++++;;++++x
:;::;+;;+++xX+xx+xxXXXX$$$$$$$$$Xxxxxxxxxx++++xxxXXX+;;;:;;+++xxxxX$$X++xxXX$$XXxxx+;;;;;;;;;;;;x$$$$
:;;+++++;;;:xx++xxXXX$$$$$$$$Xxx++:;;;;;+xx++++xxXXXXx;;;;+xxxxxxXX$X++xxXXXXXXxx++;;;:::;::;;;+;+XXX
::+.:;;::;;:x+++xxXXX$$XX$Xx++++;+++;;;+++xxxx++xxXXXXXxXxxXXXxxXX$$++xxXXX$$Xx+++;;;::;;;:::;;++X$$X
:::::;;;;;x$++;+xxXXXXXXX++;;;:::::::;;;;;+xxXxXxxxXXXXXXXxXxXXX$$$$++xxXXXXXX++;++x++;;::;::;++;xXX$
;:;++++++xXX++++xxXXXXXxx++++;;::::;;;;;;;;++xxXXXXXXXXXXXXXXX$$$$$$x+xX$$Xx++++++++++;:::::X$xX$xXx$
;::::;+;;;X$++++xxxxxXXxx+x+;;;;::;::;++;;;;+++xXXX$$$$$$$$$$$$$$XXXXX$XXxxxxxxxxxxxxxxxx+;+xXxX$$$$X
;:;:::;;:::+Xxx+++xxxxXx++;;;;;;;+:;;;;;;;;;;;;;+xXXX$$$$$$$$XXXxXxxxxxxxxxXxxxXxXxxxxxxxxxX$$Xx$$$$$
;;;;:::::::;+XXx+++xxxxxxx;;;;;;;:;;;;;;;+++x++xx+++xxXxxXxxxxxx+++xxXXXXXXXXX$XXXXxxxxxxxxXXXXXX$$X$
;;+;::::;:;+X$$XXxxxxxxxxxxxx+xx++++++xxxxxxxxxXxXxxxxxxxxxxx++++xxXXXX$X$$$$$$$$$XXxxxxxxxxXX$$XXX$$
;;+;++:;;+Xx$&&$XxxxxxxxxxxxxxxxxxxxxxxxXXXXXXXXXXXXXxxxxxxxxxxXXXXX$$$$$$$$$$$$$$$XXx++xxxXXX$&$$$$$
XX$$$$Xx::X$$XXX$XXxXxxxxXxxxXxxXxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$XX$$$$$$$$$XXXXXXXXxx++xXxXXX$$$&$$X
$$$xxxX$X$$$$XxxXX$$XXXXXXXXXXXXXXXXX$$$$$XXX$$$$$$$$$$$$$$$$$$$$$$$$$$$XXXxx+xxXXxxXxxxXXXX$$$$$$$$&
xx+;;++xx+xXX$XXXXXX$$$XXXX$XXXXXXX$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&$XXXXxxxxxxXxxxxxxXXXXXX$$$$XX$XXx
xxxx+;;;+;;:;+X$$XXX$XX$$$$$$$$$$$$$$$$$$$&&&&XXX$$$$$$$$$$$$$$$&$&&&xxX+++xx++xxXXXXXXXX$$$$$$X$$X+:
x++;;;++;;::;+xX$$$$$XXXXXXX$$&$&&&&&$X$$$$$&$&$xxX$$$$$$$$$$$$$$$$$$$X+x+++xxXXXXXXX$$$$$$&&&$$X;+X$
XxxxxxxxX;::;++;+xxX$$$$XXXXXXxXxxxxxxXXXXX$$$$$xX$XXXX$XXXX$XXXXXXXXxxxxxxXXXXX$$$$$$$$&&$+XXXXXxX&+
;;;;;;;X$$x;;;;;;+++xxx$$$$$$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxXXX$$$$$$$$&&&&$$$x$xX$$$&x+
:::::::;XXX&&$+;::;;:::x$$$$$$$$$$$$$$$$$$$$$$$$$XXXXXXXXXXXXXXXXXXXXxXXX$$$$$$$$XX$&$$XX$$$$&&$$$+x:
;::..::..;XXXXXXxxX$$XXXX$XXXXX$$$$$&&$$$$$$$$$$$$$$$$$XXXX$XXXXXXXX$X$$$$$$$&$XxXXXxX+:+&&$$$$XXxx+.
::.:::..:;xXXXXXxxXXXXXXXXXXXXXXXXXX$$&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&$xxX+:;;;;;;XX$$XXx++::
..:.:...;++$$$$$$$XX$XxxxxxxXXxxXXXX$$$XX$$$$&&&&&&$$$$$$$$$$$$$$$&&&&X+X&$$$$$&Xxxx++;+:;;+xXXX++:::
.::....:;;:XX$$$X$$XXXXXXXxxxXxxxXX$$XX$$$$$$$$$$$$$&&&$$XXXX$&&$$$$x;:;X$$X$$$x+xX+++++++Xx+xx++:...""","A brown snake that can be found in moist places under rocks, rotting wood, piles of leaves, and others. They can't bite you, but they might produce foul-smelling excretions.",animalia,chordata,reptilia,squamata,serpentes,colubridae,carphophis)
CCC=snake("Cemophora coccinea copei","Northern Scarlet Snake","""$$$$$$&$XxX$$$$$$$$$$$$$$$$XXX$$$XXXXXXXXXxxxxxxxxxx+;;;;++xxX$$XXxxxxXXXX$XXXXxxx+++++++++;+++;+++++
$$$$$$$$XXX$$$$$$$$$$$$$$$XxxxX$$$XXXXXXXXXXXXxxXXx+;;;+xXxxXXX$$$XXXXXX$XXXXXXXXXXxxxxxxxxxxx+++++++
$$$$$$$XXxXX$$$$$XX$$$$$$XxxxxX$$$XXXXXXXXXXXXXXXXx++++xXXxxXXXXX$$$$$$$XXXXX$X$$XXXXXXXXXXXXxxx+++++
$$$$$$$$XxXX$$XXXXXXXXXXXXXXXXX$XXXXXXXXXXXXXXXXXXXxxxxxxxxXXXXXXXX$$$$$XXXXXX$$$$XXXXXX$XXXXXXxxx+++
$$$$$$$XXXXXX$XX$$$$$XXXXX$XXXXXXXXXXXXXXXXXXXXxxxxXXXXxxxX$XX$$$$$$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXxx++
$$$XXXX$$$$$$$$$XXXXXXXxxxxxxxxXXXXXXXXXXXXXXxx++xxxXXXXxxX$XX$$$$$$$$$$$$XXXXXXXXXXXXXXXXXXXX$XXx+++
$XXXX$$$$$$$XXXXxxxx+++++;;;;+++++++xxxxXXXXXxxxxXXXXXXXxxX$XX$$$$$$$$$$$$$XXXXXXXXXXXXXXXXXXXXXXx++;
X$$$$$$XXXXXxxx+++++++;;;;;;;;;;;;;;;;;++++xxxXXXXXXXXXXxxX$$$$$$$$$$$$$&&&$XXXXXXXXXXXXXXXXXXXXx+++;
$$$$XXXxx+++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;++xxxXXXXXX++xX$$$$$$$$$&&$XXX$$XXXXXXXXXXXXXXXXXXx++++;
$$XXx+++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+++xxXXx+++X$$$X$$$$Xx++;;;+XXXXXXXXXXXXXXXXXxx++;;;;
Xxxx++;;;;+xX$$$$$$$$$$++;;;;;;;;;;;;;;;;;;;;;;;;;;+xxxxx;+xXXX$$Xxx++++;;+++xXXXXXXXXXXXXxx+++;;;;;;
xx++;;;x$$$&$$$$$$$$$&&&$++;+X$Xx;;;;;;;;;;;;;+++++++++++xxxxX$XXx+X$$$$$$$$XxxXXXXxxxxxx++;;;;;;;;;;
x++++x$&&&&&&&&$$$$$$$&&&$x;+;X$&&$$X+;;;;;;;+xXXXXxxx+++xxx+xxxxX$$$$$$$&&&&$XXXxxxxxx++++;;;;;;;;;;
+;;;X$$X+;;;++X&$$$$$$$&&&&$++$&&&&&$$$$$X+;;;+xXX$$Xx++++xx+xxxX$$$$$$$$$$$$$Xxxx++++++;;;;;;;;;;;;;
;;;x&X+;;+xXxxX+X$$$$$$$&&&X+++X&&&$$$$$$$$$$$$XXxXXXx+++xx++xXX$$$$$$$$$$$$$$XXxx+++;;;;;;;;;;;;++++
+++$++++X$$&&&&$$$$$$$$$&&&&X+X&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$XXXXxx++;;;;;;;;;;;;+xx+
++Xx++X&$$$&$$$$$$$$$$$$$$&XxxX$&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&X++++xX$&&&&$$XXxxx+++;;;;;;;;;;;;;+
;;$+++X&$&$$$x$XXXXXX$$$$$XxxxX$&&$$$$$$$$$$$$$$$$$$$$$$$$XX$$$X;;++;+x$&&$x+++++$&&&$x;;;++;;;;;;;;;
;;xx++x$$$$X$XXXx+;++XxxX$$$$$XX&&$$$$$$$$$$$$$$$$$$$$$$$$$XxXX;:;;;;+;+++;;;;;+$&&&&&$$$X;;;;;;;;;;;
;;+x+X$$$$$X$$XXXXX;;:+xxX$$$$$$$$&&&$$x+++;+&&$$$$$$$$$$$$$Xx;::;;;;;;;+xxx+++XXX$&$$$$$$$$x;;;;;;;;
;;;xxxX$$$$$XXXXXXXXXX+xxXX$XX$$$$$&&&&&X++++x&&$$$$$$$$$$$X$x;;;+++;;;;+++;:+$xXXXXx+xX$$$$$$x;;;;;;
;;;;+xx$XXXXXXXXXXXXXX$X$$X$$$$$X$$$$&&&&Xx+++$&$$$$$$$$$$XX$+;;+;++++++++++X$$&X$&$$XXXXX$$$$$x+;;;;
;;;;;;+xXXXXXXXXXXX$XXXX$$$$$$$$$$$$$&&&&$Xxxxx$$$$$$$$$$$$$X+;+;++++++++++x$$$&&&&$$XX$$$X$$XxX$x;;;
;;;;;;;;xxXXXxXXXXXXXXX$$XX$$$$$$$$$$&&&&$XxXxX$$$$$$$$$$$$$Xx+++++++x+++xxX$$$$$$$$XXXXXXXXXXXX$x;;;
;;;;;;;++++xxxXXxxxXXXXXX$X$$$$$$$$$$$$$$$$XxXX$$$$$XXX$X$$$Xxxxxxxxxxxxxxxx$X$$$$$$$XxxxxXXXXXx+;;;;
;;;;;++++++x+xxxxXXXXXXXXXXX$$$$$$$$$$$$$XXXXxX$$$$$$$$$$$$$$XXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxx++;;;;;+
;;;;++++++xxxxXXXXXxXXXXXXX$$X$$$$$$$$XXXXXXXX$$XXXXXX$$$$$$$$$$$$$$XXXXXXXxxxxXxxXXXXXx+++;;;;+;;;;;
;;;;;;++++++xxxXXXXX$XXXXXXXXXXXXX$XXXXXXxxxxxxxxxXXX$$$$$$$$$$$$$$$$$$$$$$$XXXXX$$XX$XXxx++++++;;;;;
;;;;;;;++xxxxxxXXXXXXXXXXxXXxX$XXXXxx+xxxx+++xxXXXX$$&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$XXXXXxxx+++++++;
;;;;;;+++xx++xXXXXXXXXXXXXX$XXXXXxxxxxxxxx++xxxXXXXX$&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$XXXXXXXxxxx++
;;;;;++++++xxxXXXXXXXXXXXXXXXxxxx+++++++xxxxXxXXXXXXXXX$$XXXXXXXxXXXXXXXXX$$$$$$$$$$$$$$$$$&&$$$Xxxxx
+;;;;+x+++xxxxxXXXXXXXXXXXXXXXXxxx+x+xxxxxxXXXXXXXXXXXXxxXXxxxxx+x++XxxXXXXXXXxX$XXXX$$$$$$&$$$$$$$XX
;;;;+++++++++xxxXXXXXXXXXXXXXXXXxx$$$$$$XXXXXXXXXXXXXXXxxxxx+++++++;++++++++xxxxxxxXXXXXXXXXX$$$$$$$X
;+;;;;+++++++xxxxxXXXXXXXxXXXXXX$$$$X$$&&&&$$$$XXXXXxxxxxxx+++++;;;:;;;++;;++++++;;;;++;+++xxXXXXXX$$
+;;;;;;+++++++++xxxXXXXXX++XxX$$$$XxX&&&&&$$&&$$$XXxxxxX$XXX+;;;;;;;;;;;;;;;;;;;;;;;;;;;;++$X$$x++++;
;;;;;;;++++++++xxxxxxXXXXXxx+x$X$$X+X$$$&&$$&$$$$$$$XXxXX$Xx++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++;;;;;;
""","Cemophora cocciena is a small red-orange snake with black-outlined white or yellow splotches that don't fully wrap around the body. It can be found around damp woodlands and sandy soil, under logs, boards, or debris, but it rarely comes out during the day. Their diet consists of lizards, rodents, and various kinds of eggs.",animalia,chordata,reptilia,squamata,serpentes,colubridae,cemophora)
CCConstr=snake("Coluber constrictor constrictor","Northern black racer","""Xxxxxx+++++xxxxxxxxxxxxxxxx+++++++;;++;:.......  ..;+++++++;;;+xXx++++;;;;:... ...:;;;+++++;;..xXX$$x
Xxxxx+++++xxxxxx+;:;xxxxxxx+.......:..;:;+;;:;:..:;+++++x+xXXx++++++;;;;;::..  .xx..:;;;;;.;..+xX$X++
xxxx+++++++++xxx;:..;xxxxxx+:..  .....:xxxxxxxxxXxx+++xXxx++++;+xxxxx+xxxxxxx++xxx+...:;;:X;  ..:+++x
xxx+x+++++++xx+;::....:xx+xx:.    ...;+xxxxxx+;++xxxXXxxxx+++xxxxxxxxxxxxxx++++xxxx+:.;+;;x.  ...:;xx
++xxx+++++++xx+;:.......xx:..     ..;xxxxxxxx+++XXXXx+++;::.:;+++++x+++++;:++++xxxxx:+:;;+:..::...;+x
xxxxx++++++;;+x+;:....  .xx.   ....;+xxxXX++xXXXXXXXx++;......;Xx++xxxxxx+;+++xxxxxx..+;;$Xx+...+:++x
xxxx+++++;;;;;:;;:........XX......;++xx+xXXXxxXXXXXx+++;:.....:+xxxXx+++xx+;+++xxxx:..:XX;xxxx;;XxXX+
xxxxxx++;;;::......   ....:$x:::::;++X$$$$xxxXXXxx+;;;;;;:.....;xxxxxxxxxx++:...........+..xxxx+XXXXx
Xxxxxx++;;::....   ..::::::;$X+;+XXx+++xxxXXxxx+;::::;;;;;+;::.:+xxxxxxx+++:.........  .:. ;xx;;XXXXX
XXXXx++;;;;;;:......;;++xx+x$&xXx++;::::;;;;xx+;:::::::::;+++++;:;+++++++++..          :.....;+xXXXXX
XXXxxxx+;;;;;;;::....:+X$Xx++X$xxx+;:::::::;;+xx::......:;+++++;;;;;x+;;;+;..        ..x+xXx++++xXXXx
XxXXxxxxxxx+;;:..:;x$X;....:;x$$xxx+;:::..:::::;+;......::;;;;+XX$&&&&&XXx$XXX:.:+XXX$$XXx;xXXXXxX$$x
xxxxxxxxx+;:::;xX$X+::....::;;+&X+++++++;::;;;::::+:.......::XXX$&&&$$$&&$XXx$$xX$x;:.:;..:+++++X$xxx
xxxxxx+++;+XXXx+;+xXXXxxxxx+;;+x&x+++;++x+++++++;:::;:......x$&&&$XXxxx+++xxXxX$X;...:x;.  .:;+Xx+++x
xxxxxx++++;++;;;+xxx+++xx+++++++$$+;;;++xxx++xxx+;:..::.....$&&&&$$XxxxXXXxxxxxX$;....+:.  ..+..:++++
xxxxxxx+++++++++++x++;;;+++++++++$$+;+++x+++++++;;+;..;+xX$&&&&$&&&$x....:::;;::;xx;..+...++...  ....
+xxxxxxx++++++++++++;;;;;++x+++xxx$X+;+++++;+++++xXxx$&&$xx:.;$$&&&&$X;..    .......;xX;+:.          
x+xxxxxxxxxx++++++++;:::;+++++xxx++x+;;+++xX$$$&&$XXXx:.:.::;.:$$&&&&$X+:.. .........+x.+x..         
;;+++xx+xxx++;++++xxxXXXXXXx++;+++++x$Xx&&$XX+;;;:::::+x:.....:.X$&&&&$$x::......::x$Xx:...x+..     .
+xxxxxx++xx++++++xxxXXxx+;;;xxX$$&&$$xXx+++xXXx+;:::....+X;....:;$$&&&&$$x:.....:XX;;:...;;:.:x;.;+++
++xxxxxxxxXXxxx++xxx+++xX$$&&&$$XxXXxX$X$XXXXX$$X+:........+xx;..:$$&&&&$$+...;X;..:;+;:..:;xx+;;x:..
xxxxxxxxxxxxxxxxxX$$&&&&$XXxXXX$$$$&$&&$&XxxxxxxX&$X+.........:XX$$$$$$$$XX+X$xxxxxXX$$Xxxx+++;;;xxXx
xxxxxxxxxxX$$&&&&&&&&&&&&&&$&&$&&&&$$$$&$Xxxxxxxxx&X+;++xxxXX$$$$$&&&$$$XX$XXXXXx++++++;;xXXXxxxx;..:
xxxxx$&&&&&&&&&&&&&&&&&$$&&$&&$&&&&$$$$&$$&&&&$XXXXX$$&&&&X+;+x$&&&&&$X$$XxXx+++++++++;:...+:......;X
X$&&&&$XXX$&&&&&&$&&$$&&$&&$$$$&$&X+++$&&&$&$X$$$&&&&&&&&&&&&&&&&&$XX$$$x.:::;xXx:..........;:;xXx+;.
&&$xxxX$&&&$&&&&&$&&&$&$$$$$X++X&xxX$&$$$&&&$&&$$$$X+xX$$&&&&&&&$X$$$$$:...::::..:XXx:::++X$$x+++x+..
xX$&&&&&$&&&&&$&&&&$$$$Xx+xx$&&&&&&&$$$Xxxxxx+;;X$&$&&$$$$x+xXX$$$&$X+::..:::::;x$$$$$XX$Xxx+;:.....:
&&$&&&&&&&&&&&$&&$$x+xX$&&&&&&&&$$X$$$++++;;::......;X$$$&$X$$$$XX$$$$$$$$$$XX$x++xxxxxxxx++xX$$X+::.
&$&&&&&&&&&$&&&$&&&&&&&&$$Xx+++++++Xx$$+;;::......:::...;X$:..:::;;::::::..::.:+xxxxxxxxxxxxxxxxx+...
&&&&&&&&&&&&&&&&&&&&$Xxxx++++++++++$++XX;::.....::...+$X:...:;+++;;;;:;;::.....;xxxxxxxx;xxxXxxxxxxx.
&&&&&&&&&&&&&$$Xx++xxxxx+++++++xx+xx+++$X;:..:x;;:x$x......:;;+xx++++;;;;;;;::..;xxxxx:.:XXxXXXXxXXXX
$$$$&&&&$x++;;;;++++++;;:;;++++++x$+++++$+:;+;+$$x.......::;;;+xxxxxxx+++;;;;;::...... .:XXxXxXXxXXXX
&&$Xxx+;;+++;;;;;;;;;;:::;+++++;;$++++++x+x$&&x...... ....:;;+xxxxxXXXXx+;::;;;;:...    .xXXXXXXXXXXX
+xxxxxx+;++++++;;;;;;;:;;;+xxxxX&$$$$$$$&&$xxx+:..........+xXXXXXXXXX$$X;.....;x;:..... .;xXXXXXXXXXX
$$$$$$$&&$&&&&&&&&&$XXXXXXXX$&x++++++xxxx$Xx+++;:........;xXXXXXXXXX$$$+::....:+X+::......+XXXXXXXXXX
+++;++xx++++++;;;;;x$x+xxxxxxx+++++xxxxxxx$xxx+;++;;;x+;+xXXXXXXXXXXXXX;....:;+x+++;:......;xXXXXXXXx""","As the name suggests, the Northern Black Racer is a black snake. It also has a lighter colored underbelly. They are very fast, and active day and night. Baby ones are often confused for the venomous Timber Rattlesnake (not covered in the snakeDEX), so much so that even the mature ones often mimic rattlesnakes when they feel threatened. They frequent fields and woodlands, and may even show up in someone's garden.",animalia,chordata,reptilia,squamata,serpentes,colubridae,coluber)
PG=snake("Pantherophis guttatus","Corn Snake","""    . :       ....     ;:;;::.  :..   .:..::: .  .. . . .::..     ..   ;. :..:::....   : :;:... :::;+
  ..: ..      :.     ....::  .:. ..   .  ..:; ::.::::.  ...  :.  .  .     :;;::   :;..;.  ::;. ..  :.
     .         :        ..    . ..::::;:  .:::.::::.       . .......   :.. .:;;.  :;;: ..:.:.:;:;;:+;
           .:..  .     ..         ;. ;;;  ..  ..:..:+...  ...    . .     :.. .::: . : . .:;:..:.:.;;+
     :+;. :;++;::.      . ..       :;;..    .   . .. . :.   . .     . : .;: :...: .   .:  .....;;;;..
  .::::... ;:::;: ......         :;: .: .:..   .:.::.: . .         .         :.::.   :...::.. .::.:;:
:.  .:;::::.       ..          ..::::;. .  .. ...:.::..           .        ..     .  ........ .:.    
 ...  :;;;..                    .:...:. ..:.:.:. .;;:.;:.;:.::;x:         .:;. :      .. . ..  :.    
  ::..            ::.      .     . :::.:. :..::.   .++++++++xxX$.:;:&$+;: .  ...    ::.....:;    :.. 
    ..          ....:.   .  ..   :.. :  .:....;:;.;$x+++xX$$$$&$;;+&$XXXXx+::; :::       .:;.  :;::..
          . .:..::::.::..::   :::.:         .:;x  xX+xxXX$&xX$&$$&&&$$$XXxXXx;..;   :.::...;. ....:..
.              ......:   .:    ...  ...   . :;X$x :$xx$X&&$&&&&&&&x+X$;x$&$XXx;    ...:.  ..   :.::.:
;:. :  :   .    . ..  ;..:  .        :..  :::xxXX  :XXXXXx$Xx: ;. .: ;X    .+$x:  :;::. .    ....;+;:
    .  . ....     ..      .;    .   .     :;xx++x .+x:;+;xxX x&$:X:;x$&. .;   :+;.:;...;:.. : .:;:.:.
        .   ..::..  :     :          :  .:.+xx++xxxx:.;;.     : $&$&&&&&&&&&Xx.;       .;+: .::::::::
  .   .  ....::  . .:.   .      .        .xxxx+++X+;x+;+  ;   x&&&&&&&&&&&&&&&&xX:;;:  ;;:.:...:.:;::
 .        :  ;    .::.  ..  :   .:::;:  ;++Xxx+xxXx++xx+    $xx+xXXX&&&&&$$$$&&&xx . ..::.:. ..:.:::;
     .   :    :.;+;++ .     .;;;    :.   .x$&X$+$+xxx.Xx;;;+;+x+;+++xx$$XXXXX$&&X; . ..::     ...::. 
   . :.     :;++++::;+:.:   :..       .::;;. .++X$x;  . X&$XxxxxxX&$::.&&XxxX$$XX+  ::..;.; ::::  ;.:
    ..     :;::+;:; .: ::.       .:.  ::;xx;.;xXXXX$&x... :$Xxx+xxX$&.:+&XXX$X$$$     ;.  .:::. : ...
   :..    ::::;:+++;;:...   ;     .:: .+XXX$&&$XXXXXX$+;+++x$$$$$$$$X;+;x$XXX&&x+  ..      .:.  :;.; 
::.. ....:;+++x++x++;::     ;+;+.  xXxxxxX$$&$$X$$XXX;+&$X:+X&&xxxX&&&$X$$&&X;;++::..:.   ::;:.   .;:
 ;.::::+;+x$.::&$$XX$&+ :X+x+xX&+..+&$$$$&&&&&&&&$$x;+&xxx x&$$&$&&$$&&X&&Xxx:;:  ... .;..::.: .: .:.
    :;:;xXXX$X;xX$$$$$:x&$XXXX$$&;;++xxX&&&&X+:;:.:X;Xx:+xx    .::     ;x:+:;;;:::.::.:+$     . :..::
.:.::.:;XXXXx;X&&&$&&&XxX&$$$$$$$xX&$$&&&$&$$++&&&x;:&$&&$: .x.   .  ;.  . xx;;:    .:;+x::  .    ...
.  ..::xX$$xx:++++;;xxxX;X&$$XXx+;++++x;xxxX$&&$$XxX..X&$XX$&X;+:.xXX    ;.  ...+x+x:.:;.:   .  .. .;
 .;.;;+x$x;X++ .; . . ::. ;x;;:++::..;;:;++XX&&$XXxX; +:;$&&&&$$X$&$xXXxx+$XX$X&$     .  +; .:: .. ;:
::;:::;x$X;Xx :. .       .   .;:. ..:  :;xXxx&&$$X$XXxxx: XXX+xxxX:;;;+;&$$XX$$&&;: ;$+x++:   ..     
;;:..:;+$X+;Xx .    :.      .::.          ;;xX&&&$$$$$$$&+  .X$XXX$&&++&&&$$&&&&&X$x&&Xx++x+..:::    
;+++::;xXX$$+x+.  .;..:  .  .:.. :  .::   .;xX$&&&&&&&&x::.x&$$$$$&&+xx&&&&&&&&&&&$$&&&$Xx+xX+$. .   
::::..;X$$Xx$$: ;:::;;.:...    :.:;. .:.:.:::.;X$&&&&$$X++&&$$$$$&&&XXX&&&&&&&&&&&&&&&&&&$$$$&:X.:.. 
.  .;::X$X$$$+x .  :::  .    .:::  . .      .;.:::+x$$&&&&&&&&$$&&&$$&&&&&&&&&&&&&&&&&&&&&&&&x+:  .x.
+..:;;+$&X+$;+X:.   ..::.  :..   ::...       ;.  ::;;++XXX$XX$XX$&X$XX$&&&&&&&&&&&&&&&&&&&&$$X+:x;  :
  .::;:x$&$$$X..      .: .:..:.;;;. .;    .  ::::.. ..;:;;++++xxx+XxXXx$XXX++$X$&&&&&&&&&&&&&&. .:;; 
. ...: .x&$XX; ;  ::: .  .:;+++. . :..            .  .:.. .;+ . ..;::.+X++XX;xxxxX$XX&X$&Xx++;. :;;:.
++;   .:++X$X;  .....   ::: ..:.:.. ;:    .  ::.     .    :..;;..;.   :+;;.:::.x+xxxxxXX+X&+ :;.:    
... ..:;;..;+;. .       ::.;+;::+x:.;.    .;. ...          .::: :::...:;;;;+;:;; ;;:;+xX:+;;:.:+; :. 
       .;+::;;+;;..     .  .:+++;:....      . .  .         : :.:+;;;;.+::..: :. .;:;:::;x+;..:x;;;   
.    .. ..: ..:; :  :.  .  :.:+;+::.  :++.+      .: .     .       ;.:.. :.:.   :; :;:;++x++. :;+x .: 
""","An orange-bodied snake with black-outlined red blotches on their backs. They are one of the most popular kinds of snakes to keep as pets, second only to the Ball Python. In the wild, corn snakes typically live for 10-15 years, but in captivity, they can live for over 20 years! They can be found in places like overgrown fields, trees, and abandoned or rarely-used buildings or farms. They can, in fact, climb trees. Their diet may consist of rodents, other reptiles, amphibians, or unguarded eggs in the trees.",animalia,chordata,reptilia,squamata,serpentes,colubridae,pantherophis)
PO=snake("Pantherophis obsoletus","Black Rat Snake","""XXXXXXXXXXXXXXXxxxxxxxxxx++++++;;;;::::::.......   .::::........:;++;::.........       ...::;;:......
$$$$$$$$$$$$$$$$$XXXXXXXXXXXXXxxxxxx++++;;:::... ..::;;:::::......::::::::::.......    .....::.......
&&&&&&&&&$$$$$$$$$$$$$$$$XXXXXXXXXXXXxx+++;;::.      ..::.............:::..........    ..............
&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$XXXXXx;;;:..         ..........   ..  .....:::::..    ...............
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$XX;:..          ...:::::;:.......   . ..:...        ..  .........
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$xx+;.         .:::::;+x+::::::.......::.. ..:.........    .....
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$Xx+;:         ...:;+xXXXx+;:..  ......:::::;;:::....:..    .::.
&&&$XXX$$&&&&&&&&&&&&&&&&&&&&&&&&$$$XXxx+;.        .:;+xXXXXXXx;::.  ....::::;;:::::.................
Xx+++x+xXX$&&&&&&&&&&&&$$$&&&&&$$$$$XXx++;:.     .:;+xX$$$$$$Xx:::.   ....:......   ...:....:;;::::..
+xXXxXxxX$$$&&&&&&&&&&&&$&&&&&$$$XXX$Xx++;..:::::;+xXX$$$$$$$Xx+;:.........    ...  ..........:..::::
$XXXX$$$$$$$$$$$$$$$$$$$$$$&&$$$$$$$$$Xx+:.:;::;++xX$$$$$$$$$X+;:::::.....      ...::....     ......:
XXX$$$$$$$$$$$XXXXXXXXxxx+xxx+++xxxXX$XXx+;;;;;+xX$$$$$$$$$$$Xx+;;:::::.:.. .......::.......         
$&&&&&$$$$$$$$x;;;;:;::::::::...::::;;:;;x+;;;+xX$$$$$$$$$$$$$$$XXxxxxx+;;::::::......    .  ...... .
&&&$$$$&&$$$$$+:....:;;;;:.:::::::::;;;;++;;+xX$$$$$$$$$$$$&&$$$$$XXXXXXXXxx+;;::.....   ............
&&&&&$$&&$$$$$x:....::::::::;;:;;;;+++++++++;;:  .:;::+xx;:+x+X$$$$$$$XXXXXXXxxxx+++++;::....::..:...
&&&&&&&&&&&$$$X;::::::::::;;;;:::;;;;;:.....      .::;;..:::;;+++X$$$$$XXXX$$$$XXXXX$$x+;:;;.....::::
&&&&&&&$&&&&&$X;::::::::;;:;;;;;;;+;.       ;xx:..:xX+;;;:;;;+xxxX$X$&&&&&&&$$$XXXXX$$XxxXxx+;;;;;;;;
&&$$&&&$&&&&&$$+::::::::;;;++;;+;++  .   .+x$xx;$$$$x+xxx+xX;x$$$XXXx$$$$$$$$XXXXXXXXX++x$$$+:..::+xx
&&&&&&&&&&&$$XXXXXXXXXXxxxxxxxXxx; :: .+xxXX;;+;:;xx::..::  :+xx+;;;;$$$$$$$$$$$$XXXXXXXXXx+:  .:;+;.
&&&&&&&&&$XxX$$$$$$$$$$$$$$$$$$x;.::;++xx;:.     .           :;;;+;;X$XxX$$$$$$$$$$$XXXXXxx;...:;++;:
&&&&&&&$$x+X$XXX$$$$$&$$$$$$$+;+:   :;;.      .. ..  ..:::;;;;;+;;+$$$$$$$$X$$$$XXXX$XXxxxx+::;:::...
&&&&&$XxXx+xXXX$$$$$$$$$$Xx+:+x+:       .::::;;:;:::;:;;;+;+;;;+xX$$XX$$$XXXXXXXXXXXXxxxx+::.......  
&&&&&Xx++;;;+xX$$$$$$X+;..+xXXx:    .:::;:;;;;;;;;;;+++++++xX$$$$$$XXXXXXXXXXXXXXxxxx+;:......       
&&&&$x;;::.:.:...  .    ;X$XX;      ::;;;;++;;;++++xXX$$$$$$$$$$XXXXXXXXXXxxXXXXxxxx+:    ..         
&&&&$X+..  .        ;;xX$$+;.       :::;;;;+++xX$&&$$XXXXXXXXXXXXXXXxxxx;::..:::::...     ..         
&&&&$Xx+;;;;;;::+;xXXxxx+         . :;;;;++xX&&&&&&&&$XXXXXXXXxxXXXXxx+;. ....:::::;:     ..     .:;.
&&&&$xx+:;x+xxxxxxx+;;:          .:;;++++x$&&&&&&&&&&&$$XXXXxxxxx+;;:::.    .::::...      ..   ..:+x+
&&&&$+:..:;;;:;::.            :;;;+++++X$$$&&&&&&&&&&&&$Xxxxx++;..  .. .       ... . ..  ...    .... 
$&&&&+         ...         .:;;+++x++$$$$$$$$$&&&&&&&&&&$Xx+:....  .      .   ....     . ::..... .   
X$$$$$;                .:;;;++xxxXX$$$$$$$$$XX$&&&&&&&&&&Xxx+;::   ..   ..:....   .:::....:. ....::..
$$&&$$$X;        ..:;;;++++xxXx;;xxX$$$$$$$$$$$&&&&&&&&&&$xx+...   ...      .:..::++;. ....:......::.
XX$$$$$&&&&Xx+;;;++++xxxXX$&&$;::.    :+XX$$+.X$&&&&&&&&&$xxx+;.  . .. .   .:::;:::;. .:::+;.   .::::
XXXX$$$$&&&&&&&&$&&&&&&&&&&&&&&&$XXx;      .;+xX$$&&&&&&&XXxxxx++;;.  . .....:;::::..............:;:;
$$$$$$$&&&&&&$x. X&&&&&&&&&$$&&&$$&$$&$XxXxxxxXxxxxxxX$$X$&$xxXXXxXxx;:...:::;:.  ...   ..... ...;;::
&$$$$$&&&$Xx:.x x$&&&&&&$x++$&&&$&&&&$$$&&&$$XXxX$$x+  :.  .;++++xxxx+++:::.    . .....:....  .....::
&&&&&$X;:++xX$&&&&&&&&&&&&&&&&&&&&&&&&$$$&&&&&$$$$$$$Xxxxxx+;;x+:..:;++xx+;:.....:...  .::::..:::...:
&X+;::+x$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&$XXx+xxxxx+++x+x+;xxxxx++++;:..::.:;++;::;;:;xXX
   +x$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$&$$$$$$$XXX$$XXXXXXxx+xxxx++;.::.::::::;+;++;;;
""","Adult Black Rat Snakes are black in color with a white underbelly. When they're younger, they are brown and grey, but as they grow, the dark pattern grows in quickly. It has a varied diet, including (but not limited to) mice, rats, moles, eggs, frogs, lizards, and more.",animalia,chordata,reptilia,squamata,serpentes,colubridae,heterodon)
HP=snake("Heterodon platirhinos","Eastern Hognose Snake",""":;:::::::..::::::...:.::.:::::::.:...:::;:..::::::...:......:::.::...::.....:...:..:::.:::::::;;:::::
::::;::.::::::;:::.:::::::.::.:..:::::::.:;:......::.:::..........:::::::::::::::.......:....::::::::
:::;;:.:.:::::::........:.....::...:::...::.:.:::...:.......::...::::.::.:.:.::...::::....:::::::::::
::.:::::::::::::...........:::....:::::.......::::.:..:....:......:.....:;:...::::......:....::.:::::
:..::....:::........::::..:.....::::....::::::::::.::::...::::.......::.:...:..:;xx:....:..::.:::..::
:::::::..:::.........::........:::;:..::::::::::.:..::..:::.....:..:.::..::.::;+X$Xx;::::.....::...:.
:::::.::::........:...........::::.:::::...::...:.............:::::....:::::;;+XX$X$x;::::::::::.::..
::.:::.:............:..::;++++xxxxx+++;;;::::;::::............:.:...::::::::;xX$$$$$Xx;:::..........:
:::::::::......::.:::+xxXx+x$$$$$$$$XXxx++++;;::::...:::.........:.:::::::+x+xX$$$$$x++xx+:::::::...:
:::::::::....::.:+xXX$$Xx+X&&&$$&&Xx+xxX$$$XXXx+;:....::.:......:..::::.::;+x$$$$&$$$XXx+;;::::.:::::
..:::.:::..:::;xX$$$&&&X+X&$&$$$&Xxx$$$$$$$$$$XXXx;:...:::....::.::::::::+X$&$$$&&&$$$$$$X;:::..:..::
::::::::::.:xx+X$&&&&&&$+$&$$$$$XxxX$$$$$$$$$XXXxXXXx;::::::::...::::::::$$&&$$$$&$$$$&&&&X;:::::::;;
::::::..:;+X$x+x$&&&$$$$x$$$$$$X$&$X$X$$$$$x+x++xXXXXX;:::;::..:::::::;+:$&$&$$XXxx$X&&&&$X;;:;::::::
:::..:::+X$$$X+x$&$$$$$$$&$$$$$$&&XX$XX$$$x+X$$$$$$$Xxxx+:::..:::;::::;+$$&&&$$xXxx$x$&&&&$$;::::::::
..:::+xXX$$&&&$x+&$$$$$$Xx+$XXXxxxX$XXXXXxX$$$$$$$$$XXXXXx:::.::::..::;+$&$$&$$x++x+xx$$&&$$x;::::::.
::::;+x$$&&&&&&X$&&$X$$X$XXX$$$XxXXXx$X$$XxXXX$$$$$$$$XXXx+;:;;::::::::;$$&$$XxX$&&$$$xxxXXx+++::::::
::;+;xX$&&&&$$$$$XXx$$$$$XX++;;;;;+++x+XxxXXXX$$$$$$$$$XXXxx;::;::::::::;xx+xXX$$$$$$$$XXXxx+;;::::::
;+;;xx++X&&&$$$$&$$xxXXx++;;;::;::::;;xXXXXXXX$$X+++++++$$$$x;;:::::::;;++++xxX$$$$$$$XXXxxx++;;:::.:
;::+$$Xxxx$&&$$$$$$$XX+++;;;:::::::::::;xxxXX$X+++xX$$&$$xXX+;;:::::::;;+$$$$$$XX$$$$XXXX$$$$x;+;;:::
::;+X$$$xxxxX&&X+X$Xx+;;:::;;;:::::::;+;+xX$$++X$$$$&$$$X$XxXx;:::::::::;+xxxxxX$$&$$$$X$Xxxx++;::.::
:.;X$$$&&&&&$$$XXX$xx+;;:::::;:::::::;;:;;;x$Xx$$$$$&$$$XXX$Xxx;;:::::::;++xXXXx+$&&&&$$Xxxxxx+;;::::
::;x$$$&&&&$$$$$XXXxxx;;+x+;xxxXx+;+++;:;+++xxXXX$$$$&$$$$XXX$xx+;::::::+;$&$&&$xx+x+x$&XXX$$x;;;::+;
::;X$$&X+x$&&$$$&$$XXXXX$Xx$$$$$$$$$$X+++++xxXxXXX$$$&&&$xXXXx++;::::::;;+$&&&&&x+$X+XXxX$&&$$;+;::;;
::;xXXXx+X&&$Xx+X$$$$$$$$&+x+xX&&&&&&&$$Xx+xX$$XXX$$&x++xX&&&&Xx;;;:;;:::;++xxxxX&$$&$$X+x$&$$+++Xx;:
:::+X$$x$&&$x+X$&$$X$&&&&&$&$+xX$&&&&&&&&&$XXxxXX$$$xxX+$$X$$$X+;;;;:;:::;$xxxX$$$$$&&&&&Xxx$X+XXXx+;
;::;+X&$XX$$$&&&$xxx$&&&&&&&&&xX$&&&&&&$+X$&XXxXxXx++x$&$$$$XXXX++;;:::::+xX$$$XxX$$$&&$$$$XXxxxXX$x:
:.:;;;xxxx$$$&&&xx+X&$$$$$&&&&&XX$$$$&&xxX&&&x$$$X++X$$&$$$$$$$x+++;;:::::+XXXXXX$$&$$$$$XXXxxX++;;;:
+::;;:+xXxX$$XX$&&&&xX$$$X$$$&$$$$$$$&xxX&&&&x&&$XX&&$&&&$$$$$XXx++;;;:;:;++$&&&$$X+x+X$$X$$$Xx;;;;::
;::;::+xXXXxXx+X$&&$xXX$$XXX$XXxX&$XX$$&&&&&&X+Xxx$$$$$&&&$$$XXXx++;;;::;;+x$&&$Xx$$&&&&$$XXXXX+;;:::
::;::;+x+:;xXXXx+XxX$$XXXx$$X$&&&$$$$$&&&&&&&&xxXXXX$$$$&&&$xX&&&X+;;:::;;XXXXXXX$$$&&$$&$XXXx+;:::::
::;;;:::;;::::;+++xX&&&&&&X+XXxxxX$$$$&&&&&&&&$$XxXXX$$$&X+++X$$XXx;;;;;+;xX$$X$$$$$XxxxxX&$$x+;;::::
::::::::;::::::;;;;+$&&&&$x$$$$$$XxX$$&&&&&&&&XxxX$$$$$$&Xxx$&$$XX$X++++++XXXXX$$$$$$$&&XX&&&$+;;::::
::::::::;::::::;;;;+x$&&Xx+&&&$&&&Xxxxx&&&&$$XxXX$XxXX$&$x+x&&$$$$XXXxxxxxxx$$XX$$&&&&&&$XX$X+++;;:::
::;::::::::::::::;;;;x$$Xx+&&&&&&&&$$XXXXX&$Xxx+xXxxxX$Xx+x$&&&&$$$$X$$XX$$X$$Xx+x$&&&&$$$Xxx+::::;;;
::::::.:;::::::::;;:;+X$xx&&&&&&&&&&&&&XXXXx+;;;;xxxX&&XxX&&&&&&&&&$x+$$$$$$$$$&Xxxx&&$$$X$X+;:;;;++;
:;::::::::::::;::::;;+;;++$&$$$$&$XXX&x++++;;;:;;+xx$&&&$X$$$&&&&&&$x+X&&&$$$$&&$+Xx$&$$$XXx++;:;:;;;
:;;::::::::::::::::;:::;;;;;xxxX$Xxx+;+;+;;:;;;:;+++xX$$$XX$$$$&&&&$xx+$&&&&&&&&&XxX$XXX$Xx+;;:;++;::
;;;::::::.::::::;+:::;;:::::;;;:;;;::;;;;;::+x+;;+++x+xxxXXX$$$$$&&$xxX&&&&&&&&&&Xx$&$XXXXX+;::::::;:
::::::::::::;;;:::::;+;::;;;:;;;:;;;:;;;;::::;;+;+x+++xXXXX$$$XX$$X$Xx$&&$&$$$$&X$$&&$Xx++x;;:;:::;;;
;::;;::::::::::::::;+;;::+;;::;;:;;:::::;:::;;;++x+;+++++xX$$$XXX$&&&&&$$$$&&$XXX$&$Xxx+;;;;:;;:::::;
;::;;:::::::;:::::::::;+x+;;:::::::;;;:::::::;;;;;;;;+x;;+xxXXXXX$&&&&&$XX$$$$XXXxx+++++;;;:;;:::;:;;
;;;:::::::;;::::;;;:::;++;;:::::::;+;:;;;;::;;:;:;;;;x+;;;;;+xxxxxXXXXXXX$X$$Xxxx+++;+;;;;;:::;;;:;:;
:;:;;;:::::::::;;:::;;:::::+::;;::::::;;;;;;;::;;;;+XX+;:;;+;;;+;x+++xxxxx++++;;;;;;:;;;;;;::::;;;:::
:;xx;::;::::;::;:;::;;::::;+;:::::::;;;:::;:;:;;;:;;;+;;:;;;;;;;:;;;:;;;;+++;;:::;;::;;::::;::::::;;;
::::::;:::::::::;;;;::::::::::;+:::::::::::::::;::;;;;;;::;++;++::;;:;:;;;:;;;:::;;::;;::;:::::::;;;;
""","The name \"Platirhinos\" is derived from greek, meaning \"flat snout\". It uses this unique nose to burrow into the ground. The patterns on this species are extremely diverse, depending on locality. In New Jersey, the coloring is commonly a rusty gray with black or brown rectangular blotches. It can be found in places with sandy substrates. It often immitates venomous snakes by puffing up its body and flattening its head. It can also deter predators by emitting an awful smell.",animalia,chordata,reptilia,squamata,serpentes,colubridae,heterodon)
LGG=snake("Lampropeltis getula getula","Eastern Kingsnake","""................    .......................   .. .    ...............        . ............ . .......
..........:................. .......               ................             ............  ..    .
....................................   :.;X$$$$$$X:++;:...........              ....  ............ ..
.............................. .... :X$&&;X&&&&$$X;xXxXXx+:........              .     ..........  . 
....:...  .:x$Xx$&&$x;:...........:X&&&&&X;X&&&&$;;XXXX$$$X+:..  ..              ....................
..........:$$&&$X&&$XXXx;:........;x&&&&&X$$xxxxx$$xxX$X+;x$$+..........           ............ .....
 ..  .....+$XX$&&XX$XXx+$$$;....;$$$X+$$XX$X+:..:+XXx+xX;$$$$$+...........    .... ...... .......... 
..........:+;;;+$&$X++;x&$&$+..:x$$&&XxXx..:..... ...:xXx$$$&$$:.........      ......................
  ... .   .:;xx&&&&&$$$$&&&&&;.;$$$&$$X+..::...........:++;;;x$+..........    ................. .... 
..... .....:;xXXX&$XX$$x$++XxX+x$$&&$XX:.:.. ...........+$&&&X++.......................... ....:.....
....  ....xX$$$$XX&&&&&$&&&&&XxXxx;xXXx.:+xX$$Xxxx++;;;;x$&&&&Xx.::.....:.................   ........
...........+XXX$X$&&&&&&&&&&&&$$&&&$$X::x&&&&&$$X$X$X$$&$&&&&$X+...:..:....::............ ...........
 ...  .....:..::x+:;+X$&&&&&&$$&&&$$X&&&&x+$&&$$$$X;:x$&&&&&$Xx.::.:::.......... .    ...............
..............+$&&&&&XXXXX$&$$$&&&$$$&&&&&x+XX&&$x+++xX$$$$XX;.......................................
.  ..::.....:x$&&&&&&&X$$$X;;;xX&&$$$&&&&&X$XxxxxX$$$$xX$X+.......:.................. ...... ...  ...
............;$$&&&&&$X$X+::X$$$$XX$x++xXX$X;......:.........:........................................
............+$$x+xX$$x:...+$$$$&$Xxx$$$$XX:............................................ .. ... ......
.........:: +x:x$$$$x;.::X$$$$&&&&xX$$$$$X:.........................::;xX$X;$$$$X;::..... ..... .:...
........... .;+$XXXXX$$x;X$$&&&&$$x$$XXX$$$+.::..................;x$$$$&&&&:X&$$$$$$x::..............
.  ...... .  .+x$$XxxXXXx:X$&$$$X;:+$$$$X+:x$$$$$$XX+:::::;+xX$$$$;+&&&&&&$;x$&&&&$+;XXX;............
.  ....  ..:...+xX$$$$&&$XXX$$$x::.:+$$Xx:x$&$$$X$$X:+$$$$$$$$$$&&&x+X&&&$XXxx$$X+:;XXXXXx:... ......
    .............:+xXXXXX$$X+;:...:..:+x++x$&&&&&&X;x&$&&&&+;X&&&&&XxxX$Xx+;;;+x$$xx$$$XxXX;.........
.... ......... ..........:::............;xXx$$$$$x++x&&&&&$+xxX$$XXX+:..........::+XX$XXx++x;........
. ........... .... ...........::...::...:....:;+xxxxXxXXXXXXXXxx;:..................+x++;:::;:.......
   ...  .... ... . ..........::;. ...:....:::... :.........::........................:X$++Xx+X.......
.........:..  .  ..... .......::;;;:..::::.........:.:.....:.::... . ..................+++Xxxx;......
...  .. ....... ..  ......   ...:++;:............................  ..::..::............:;;XXXxx......
...    .......  .... ..... .................:...:.::.:.............   ....... ...........+x:..;::....
.     ......... ....  .............................::... ..... ......... ....:............xxXXx;.....
.     ......... ... .......... .  ............................. ..........................:X$$X;.....
...:......... ...... ....  ...................:.........:..........:.....................:.;+XX+...  
....  . ..  ..... ...  ... .. ........ ............. ............... ......................;+x+;...  
.. .    .......   . .....................:.....:. .............:. . .........  ............:x$$+.... 
.  .  ..  ...  ... ...    . ........................:.. ................:..... .:..... .....x$$+.....
..  .... .......... .  . .............. .:.:..::..... ..........:.. ........................;:;:.....
...........   ....... .    ....  . ......::...::........... ........... .. ....... ...... ..+$$+..   
....    ....... .. ... ........ ................:.............. .......... ....:............;$$+.    
.... ..      . .......  ..........  ....... . .. ....:... .. .......... .........:..........:X$x:.   
 .... .  ........ ......   ..:........ .....:...... ..:........... . ............:.:::.......x++.. . 
.....    ... . .....    .............:..........::.. ......  ..:...........:............. ...;$X:.   
.....   .. ....:. ....  ..:... ...... .. ...  .:..  . ....... . .....: .  ........:... ..... .$$;....
..  ........ ..:...   .   :..:....... .. ...  ......................... ......:....:.. .. ....;;:.. .
.        .    ........................... ... ........      ............  ............... ....:xx;...
 ..  . . .......:... ..  .  . ......... ........ ............:..... ... .:................ ....;Xx:..
..     ...... .......... .  . ..  ...............:.................... ......... .....:...... ..;+;:.
 ...  .... ...............   ....::.........:.. ........ ...... ...........  ....................:XX:
........ .  .:......  .. .. .....  ............................ .............. ....................+X
""","This snake is primarily either black, blue-black, or dark brown with from 23-52 white or cream colored chain-like rings, earning it the name \"Chain snake\". It likes swamps and steambeds, and can be found under logs or debris, or even sometimes out in the open. They like to eat things like rodents, birds, and frogs, but may also eat Timber Rattlesnakes!",animalia,chordata,reptilia,squamata,serpentes,colubridae,lampropeltis)
LT=snake("Lampropeltis triangulum","Eastern Milk Snake",""";;:..............:::::::::::::...............................................:::::::::::.............
;::.............::::.:::::.....................................................:.::::::::............
:::................:::::::.......................................................::::::::::..........
::...............:::::............................................................::::::::::.........
::..............:::::...............................................................:::::::::........
::.............:::::.................................................................:::::::::.......
::............:::::.:.....::........::;::;+++::;;;;;::.......................:;+;+;:..:::::::........
::.........:.:::::::...........:;+;;x+x+xx;;xx+x+xx+++xx+;::...............+X$:;XXxx;:::::::::.......
::.........:.::::::........::;+++xxxxxxxxx;:xx+xxxxxX+:+x+xxxx;::........:xXX$X+X$Xx++;:::::::.......
::...........::::::......;+xxxX+;xxxxxxxxx+::Xxxxxxxx;;Xxxxxx+++xx+:.....+XXXX$X$$XXx++;:::::::......
::..........::::::..::;;+xxxxxxX+:+$XxXXXX$x;$$XXXXX$+:Xxxxxxxxx++xx;+:.:xXXXXX+:+$$Xxx;:::::::......
::........::::::::..;xxxxxxxxxXX$+;x$$XX$$$$+$$$$$$$$xx$$$Xxxxx+;xxxxxxx+XXXXXX+:;x;+xXXx;::::::.....
::........:::::;;::;+;;$XXxXXXX$$$$x$$$$$X$&&$xX$$$$$X$$$$$$$$X;;Xx+xxxx+xx+++X+;;x+xXXXx;;:::::.....
::::...::.:::::::;xxXX;:+x$$$$$$$$$Xx++xXXXXXXX+X$$$$X+$&XX$$$Xx$$XXxxx+xXxx+x+x+;$XxxXXx;X::::::....
::......:::;::::+xxxXX$Xx++X$$$XXx++++x+xXXX$Xx++++xx+X$X$x;+xX$$$$$$XXXx+;xXXXxX+xXXxxxxxX;:::::....
::.......::;:::;xxXXXXX$$$$XXx+;+;;+x$XXxxX+;;;;;;;;;;;+XXX+;;;++X$$$$$+;+XXxXXxXXxXXXXXx+x+:.:::....
::.......::;::;+xXXXX$$$X$Xxx++;;;;XXXXXX+;;;;;;;;;;;;;;+Xxx+;;;;;+xxXX$$XXXX$$XxXx;xxXXX;+;:.:::....
;:::.:+;.::;::xxXX$$$$$$$$x++;;;;;x$XXXX+;;;::::::::::;;;xXX+;;;;;++++X$XXXXX$$$XXx;:+xX+x++:::::....
;:......:::;:;+;+++xXXx$x+;;;;;;;+xxxXX+;::::::::::::::::X$X;;;;;;;++xX$XXXXXX;;;xX;::::++;::::::....
;;:::.::::;;:;xXxxxXXXxXx;;;;;:::x$xxxx;::::::::::::::::+x+x;;+;+xxxXxXx+xxX$$Xx++:;::::::::::.::....
+;::::...;;;:+xXXXX$$$Xx;;;::::::XXxXXx;:::::::::::::::+xxxxxx++xXXxxxX$XXxX$$Xxxx;::::::::::::::....
;;:....::::;+xxXXXXX$XXx;;::::::;XXXXX+::::::.:::::::++$XxxxXXX++XXXXXXXXxX$$$xxXX+::::::::::::::....
;;::..:::::;;;xXXXXX$X$x;;::::::+Xxxxx+:::::::::;;+xx$;+XXXX$$$$Xx$XXXXXXXxxXXXXx+::::::::::..:::....
;;;::.:::::;;;+xXXX$$X;Xx;::::::+xxxX$x:::::;++x+xxXX$Xx;xX$XXxxxxx&$$$X$$x;:+xXx;::::::::::.::::....
;;;::::..:::;;;+X$X+;+$Xx+;:::::;XXXXXX;;x;;:::::;+X$XX$$$X++XXXXX:;xXXXxXXXX;;+;:::::::::::.:::.....
;;;;:::.::::;;;+xx;+XXXXXXxx;::::x$XXXXx;:::::::;+X$$XXX$x+XXxxxxXX;;$XXXXxX+;;::::::::::::..:::.....
;;;;:;:.:::::;;;;+X$XXXXXxXxx++;:;X$$x+xXXx;::::+XxxxX$$XX;;+xXXXXXx:+$XXxx+;::::::.:::::.:.::::.....
;;;;;:::.:::::;;;;+xXXXxxXxXXx++X+;xx+XxxxxXX+xXXXXXx+x$XXx;:+XXxXXX++;;;:::::::...:::::::.::::......
;;;;;;::.:::::;;;;;;+XXXXXXXx;;XXXxXX$$XXxxxX++xxxxXX$$XXxxxX;+x++;:::::::::::....::::::...::::......
;;;;;;;::::::::;;;:;;;+xXX$X+;xXxxXXXXXX$$$XXX:XXXXXXXXXxxxXXx+;:::::::::::::....:::::....::::.......
;;;;;;;;::::::::;;;::;;;;+xX+X$XXxxxxxXXxxXX$$XXXXx+XXXxxxXx+;::::::.....:::....::..::..:::::........
;;;;;;;;;:::::::::;;:::::;;;+xXXXXXXxxxx;;XXXXXXXXX+:xXXXXx+;::::.............::.......::::..........
;;+;;;;;;;:::::::::;;;:::::;;;;;+XXXXXXx:;xxxxxxxXXX+:xxx+;:::...............:::...:.:::::...........
;;;;;;;;;;;::::::::::;;::::::;;;:;;+xxXx;xXXXXXXXXXX$x++;:::.....................:..:::::............
;;;;;;;;;;;;::::.::::::;;:::::::;;;;;:;+++xxxxXXxxx+;;:::::.....................:::::::..............
;;;;;;;;;;;;;;:::..:.:::;;;::::::::;;::::::;::::::::::::::......................::::.................
+;;;;;;;;;;;;;;:::.....::::;;++::::::::::::::::::::::::::::::::::.+:...........:::...................
+++;;;;;;;;;;;;;;:::......:::;;;::..::::::::::::::::::::::::....:.............:......................
++++;;;;;;;;;+++;;;:::......::::;;::::::::::::::........................::...........................
""","This snake typically has alternating red-black-yellow or white-black-red patterns. It likes wooded areas, river banks, and rocky hillsides, and also may make its home in a barn or building with a rodent problem. They are often mistaken for the venomous snakes of New Jersey, the Northern Copperhead and the Timber Rattlesnake. You may hear some mneumonics to help you differentiate them, but they dont exactly work.",animalia,chordata,reptilia,squamata,serpentes,colubridae,lampropeltis)
NSS=snake("Nerodia sipedon sipedon","Northern Water Snake",""";;:::;;+$x;:::;;::::;;++;;:::::.  .:;+xXX+;;;;;:. ..:;;:;;;;;;;;;;;;;;;;;;;::;;:..      ....  ....:x$
;++;;++xX;:..::::..:::;;;::::.:++;;+++;+xxx+;;+;:....::;++;;;;;;;;::;++;;;;;::. .....    ..:..   .;xX
;+;::::+x+;::;:.....::;++::;;;;;;;;;;++++xXX++;;;:::...:;+;;;;::;;::;;;;;;;;:.  .::::::;;;xxx+;::;xxX
.:.....;;::;;:....::;+X$$x+;;;;;+;+;;;+xXXXXx;;;;;;;;;;;;;;:::;;;:.:;;;;++++;.. .:;+;;;+;;+X$$&$XxxXX
......:++:;;;;;:::::+X&&$xxxx+;;++++;;;+xXXxx+;;;;+Xx+;++;;:::;;;::.;;;+xXX+:::.:+;;;:::;;+++++++xXxx
...::;+xxxx+;;+;:...:++++++;::;;++++;;++xXxx++;;+++++;;:;::;:;;;;;;+xxxXXXx;:...;++;+++;;::::::;;+;;;
:;;;+++x++xX+;++;:...:;++x+:::::;+++;::;xxxx++;;+xx+;;:::;;:;;++++++xxxxxx+++;:;+++;++x+++++;::;;;;;+
++++++xxxxxxxx+++;;;++xxxxxxxx+xx+++::::;;;+;+;;;;+;;:::;++;+x++x++++xxxxx++++++++++++;;+xxxx+xxxxxx$
+++x+xXXxxXXXxx+++;+XxxxxXX$$$$$$$$x:;;;;;;;;;;;;;;;;;;;;;;;;;;;::::;;;;;;;;+++++++++;;++++++++xXXxX$
xXXXXX$&$$&&$$$xxXx+++X$$&&$$$XX$&$+:;;;;;;;;;;;;;;;;;;+;;;;;;:;;::::::::::::::::::;+x+++++++;;;+X$&$
$$$XXXX$$$X$&&&X+;;;;::::;;;;++++xxx+;;;;;;;;;;;;;::;;:;;;;:::::::::::::;;+++++xxxXXXXXXXXXXXXXXX$&&$
$xx+xXX$$Xx+++++;;;::::::::::;;;;;;+xX;;++;;x$x;;;;;;:::;:..::::::::::::;;xX$XX$&&&&&&&&&&&&&&&&$$$&&
+;;;;;;;;;;;;;;;;;:::::::::::::;+++;+xXx+++++++++;;;;;;;+;;::;;;;:+X;:::;;;+XX$$&&&&$&&&&&&&&&&&$$$&&
;;;;;;;:;;;;;;;;;;;;;:;;;;;;;+xxxxxXXxXX++++++;;;:....::::..::::;::::;;;:;;;++++xx++x+xxx+xxx+++xX$$&
+++;;;;;;;;++++;;;;;;;;;;;;;+xX$$$$$$$$X;::...::;;;;:::;+++++;;:;;:::;:;;++;;++x+xXx++xXx+;++xxxXX$$&
++++++;;++++;+++++;;;;;;;;;++xX$$$x+;;:....:;+++;;;;;;;;+++++;+;::;:;;++++;;;+X$xx&$XXx;;x;;xX$$XX$$&
+x++++++x+++++++x++++;+;;+xxx+;:;::....::;;;;++;;;+x++++++xx+;:;++;:;;+xx+++;::;;;;;++;:;x+;+XXX$$$&&
+xx+xx+xxXXxxXxxx+xX++++++;;:::;;;;+++++;;+;+xX&&X+;+;;++x++xx+;;;;:;+++x+;;;;;+++;;;;;;+;;;;+$$XX$&&
xxXxXXXXXXXXxXxXXXxx+;:;;::::;;::::;;;;+x++;xx+++;+x++;+xxx;XxxXxx+:+x++++;;;;+;;;;;;+++;:++:;;+xxxXX
+xXX$$X$$$XxX$x+;;++;;;;::;:;++++++++++;;++x;$X++xxx+;+++x++;+++++;+;x+:;;;;;;;++;;;;;;;;;+++;;+;;;+x
xxXXX$X$Xxx:;;;;;++;;;;+++;;;++;++;++;;:;:;+++;:+x+;;;;+++x+xxx+;XX;+:+++++;;+;:x+;+++;;++;;;;+x+++x;
x;XXX$x;:;;;+++++;;;;;+x++;;;;;;;+++++++;;+;;;;;;;;+++;;xXX++xXx+X$;;+++;;+;+x++;+++x+;+x+;;++;++;xx;
xxX+;::;;;;;+++++;+++++;::::;++++;;;::;++;;;;+++;;;+++++;XX++x&X+;X$X$x+;;;;;+x;+++x+++;xx;;x+;;+;+++
;;;:;;;;;+xx+++++++++;+x+xx++++++;;+;;xx++x++X+;;;;xx+++xX&X;;x$$Xx+++;++;++++;+;+xx+++;xx;+x+;;;;++;
;;;;;+x+++xxxx+;;;+;;xXx++++xx++++;;+Xx;++;;+x+;;;+x$&&X;;x$$XX$&$Xx;++++++;+;+;;+;+;;;+;;+++++x+++++
;;+++++xXXxXxxxx++xxxXxx+++xXx+;++;+xx+;;;;;+$XxXXXXxX&$xxxxX&$X++xXxX$X++Xx+xx++x+++++;;;;;++;;+;;x;
+++xxXxx+XX$XXXXxxxxx+++XXX$Xx+++++$$xxxxxxxx&&&X++++xX$$XxXXx+xXx+xx+xXx+xX++$$xX$Xxx++++;++x++++++x
+xxxxxxx+X$$$X$$XXXX++XXxx+;;++xXX$&$xxxxX$Xx+$$xxXXxxX$$XxXxx+xXX+X$$xXXxxxx+X$xxXX$$xx+++;+++x++++x
+++xXXx+X$$$$$$X$XXXXX$XX$$$&X+;:;++::;xx;;++X&$XXxXXXXxxxxXXxxxx+X$&$x$$XX$$XX&$$$XX$X$Xxx+;+;+;++;+
XXXxxxxX$$$&&$$$XXX$$$$$XXX$$$$$$Xx+++X$$XxXXXxxxXXX$$XX$X$XXXXX$&X$&&X$XXX$$X$&$$&&&&$$X$x++++;;;+;+
xxxXXX+x$&&&&&&&&$Xxx+x$&&&&&&&&&&$$$$$$$XXXXxXXXxxXXXXxX$$$$X$$X&&X$&&$&&&&&&&&$&&$&&&&$$XX+++++++x+
XXxxxXXxX&&&&&&&$$$&$$$$X$&&&&$$$$$$$$XXxxX$$XX$$$$X$&&&$$&&$$&&$$&$X&&&&&&&&&&&$&&&&&&&$&&$x++++;;x+
++xxxxXX$&&&&&&&&&$$$$&&&&&$$$$$$$$$XX$$x:..:......::;+xxxxxxX&&&&&&&&&&&&&&&&&&&&&$$&&&&$$&X++++xxxX
++;:::;+X&&&&&&&&&$$X$&&&$$$$$$$$X$$&&&&&&&&&$X+;:..;xXX&&&&&&&&&&&&&&$xX$&&&&&&&&&&&&&&&&&&Xx++++x++
x;;;::::++$&&&&&&&&$$$XX$$$$$XXXx$&&&&&&&&&&&&&&&&X;:;+;++;;;:;+X&&$+;::;x&&&&&&&&&&&&&&&&$$x++;++xxx
+x+;:::::;;$$&&&&&&&&&$$&&&&&$Xxxx+X&&&&&&&&&&$+;;+x+++x+;;;:::;;+x;;;::;X&&&&&&&&&&&&&&&&$$xxx+xxx++
X;++x++;;;;++XXX$$$XXXX$&&&&&&&$xxXxx$X+x$$$&&x;::;x$X;;;++;+;;++;;;;;;;;x&&&&&&&&&&&&&&&&$xxxx+xXx++
$+;;+xX&&&x$X$$X$&$XXX$&&$$&&&&&&$X+x$++xxXX$+;++;:+X&$+:;x+;;;;;;;+;;;+x$&&&&&&&&&&&&&&&$Xxxxx++++xx
$X;;+$&$$$$X&&x;;x$$$$$$&&&&$$&&&&X+++;++++X$&&$x++;+x+;;;;;;;+x+++;:;;+xX$$&&&&&&&&&&&&$xxxxxXXxx+++
x$Xx+XX++xx;;X+;;+X$$&&&$XxXX$$$$$$Xx++xX$&&&&$++x+;;++x+++X$$$XxXx;;;;;+xX$$$&&&&&&&&$Xxxxx++xxXxxxx
&&$$XXX+;;++;x;;+++++X&&&&&$$XX$XXXXX$XX+X&&$+;;;;+xX$&&&XxxXX&&&&&$xx++++x$$$$&&&&&$Xx+x+xXxxxxxxxxx
""","These snakes can be brown, grey, reddish, or brownish-black, with dark neck crossbands and dark blotches everywhere else. It's often misidentified for a copperhead. As they mature, the pattern becomes more obscure, sometimes turning the snake entirely black. You can usually find them in groups basking on logs and rocks along stream banks. They like to eat tadpoles, frogs, worms, leeches, etc. Sometimes they even eat entire fish!",animalia,chordata,reptilia,squamata,serpentes,colubridae,nerodia)
OA=snake("Opheodrys Aestivus","Rough Green Snake","""xxxxxxxxxxxxxxxxxxx+x+++++++++++++++++++++++++xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$$$$$$XxxxxxXXXXX
xxxxxxxxxxxxxxxxx+x++++++++++++++++++++++++++++++xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$&&$$$XxxxxxXX$X
xxxxxxxxxxxxxxxx+++++++++++++++++++++++++++++++++++++x+xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$$&&$$XxxXXXXXX
xxxxxxxxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX$&&$$XXXXXXXX
xxxxxxxxxxxxxxx++++++++++++++++++++++++++++++++++++++++++++xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx$$XXXXXXXXXX
xxxxxxxxxxxxxxxx++++++++++++++++++++++++++++++++++++++++++++++xxxxxxxxxxxxxxxxXXXxxxxxxX$$XXXXXXXXxxx
xxxxxxxxxxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++xxxxxxxxxxxxx$$$$$Xx$$XXXXXXXXXxxx+x
xxxxxxxxxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++++xxxxxxxxxxxxx$$$$$$XXXXXXXXxxxxxxxX
xxxxxxxxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++xxxxxxxxxxX$$XXXXXXXXxxxxxxxxXXx
xxxxxxxxxxxxxx++++++++++++++++++++++++++++++++++++++++++++++++++++++++xxxxxxx$$$$XXXXXxxxxxx+xxX$$XXx
xxxxxxxxxxxxx++++++++++++++++++++++++++++++++++++++++++++++++++++++++++xxxxX$XXXXXXxxxxxxxxxX$&$$$$$X
xxxxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++xxX$XXXXXxxxxxxxxxX$$$$$$$$$$$
xxxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++xXXXXXXXxxxxxxxxx$$&$$$$X$$XXX$
xxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++xXXXXXXxxxx+++xxXX$&&$$$XXXXXXXX$
xxxxxxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++++++xXXXXxxxx+++++++x$&$$$$$$$X$XX$X$$$$
xxxxxxx++++++++++++++++++++++++++++++++++++++++++++++++++++++++xXXxxxxx++;+++++x$$$$$$$$$$$$$$$$$$$&&
xxxxxx++++++++++++++++++++++++++++++++++++++++++++++++++++++xxxxxxx++;+;;++++xX$$$$XXXX$$$$$$$$$&$&$$
xxxxx+++++++++++++++++++++++++++++++++++++++++++++++++++++xxxxx+++++;;;;;;+X$$$$XX$$$$$X$$$$$$$$$XXXX
xxxx++++++++++++++++++++++++++++++++++++++++++++++++++xxx+++++++;;;;;;++X$$XXXXX$XX$$$$$$$$$$XXXXXXXX
xxxx++++++++++++++++++++++++++++++++++++++++++++++xxx++++++;;;;;;;;;x$$$XXX$XXX$$$$$$$$$$XXXXXXXXXXXX
xx++++++++++++++++++++++++++++++++++++++++++++xx+++++++;;;;;;;;;;X$$$XXXXXX$$$$$$$$$$$XXXXXXXXXXXXXXX
xx+++++++++++++++++++xx++++x+++++++xxx+++++++++++;;;;;;;;;+;;;+X$$$$XX$$XXXX$$$$$$$XXXXXXXXXXXXXXXXXX
+++++++++++++++++xxx++xx;+;;+++++++;;;++;++;+;;;;;;;;;;+;+++X$$XXXXXX$XX$$$$$$$$XXXXXXXXXXXXXXXXXXXXX
+++++++++++++xXxx+++X$$X;X:+++++;;;;;;;;;;;:;;;:;:;;+;++xX$$$$XXXXXxX$$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXX
+++++++++++++xxX+x+++xXX+:::::::::::::::::::::;:;;;++X$$$$X$XxxXxX$$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXX
+++++++++++++++;;:;;::;;;;;;;;:::::;::::::::;;;;+xX$$$$XXXXXXXX$X$$$$XxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
+++++++++++++++++++++++++++++++++;;;;+;;;;+;+xX$$$$XXXX$$$xXXX$$$$XxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
+++++++++++++++++++++++++++++++++++xxxxx+++x$$$XXXXxX$XxxXX$$$$XxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
++++++++++++++++++++++++++++++++++++++++xXXXXXXXXXxxxXXXX$$XxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
+++++++++++++++++++++++++++++++++++++xXXXXXxx+xXXxXXXXX$XxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxx
++++++++++++++++++++++++++++++++++xXXXxxxxxXXXXXXXX$$XxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxx
++++++++++++++++++++++++++++++XXXXx++xxXXXXXXxxX$XxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxx
++++++++++++++++++++++++xxXxxXXxxxxXXXXXXXXxXXXxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxx
+++++++++++++++++xxxxXXxxXXXx+xxxxXxXXXXXXXXxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxx
xxx++++++++xxXXXxxxxxxXXXx+xxxxxxxXXXXXXXxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxx
$$XXxx+++xxxxxxxxxxxXXxxxXxXxxX$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxXXXXX
$$$$$XXxxxxxxxxxXXXXxxxxXXXXX$X$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxXXXXXXX
xX$$$$$XxxxxXxXXXXXXXXXXXXXXX$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxXXXXXXXXXX
X$$$$$$$XXXXXxxxXXXXX$$XX$$XXxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxXXXXXXXXXXX
""","One of two green snakes in New Jersey. This one has rough keeled dorsal scales, and it camouflages in vegetation overhanging water. They like to eat insects, tree frogs, and tree snails. See also: Opheodrys vernalis.",animalia,chordata,reptilia,squamata,serpentes,colubridae,opheodrys)
OV=snake("Opheodrys Vernalis","Smooth green snake","""+++++++++++++++++++xxxxxxxxXXXxxXXXXX$$$$$$XXxxxxxxxxxxxxxxxXX$$$XXXXXXXXxxxxx+++++++++++++xxxxxxxxxx
++++++++++++++++++++xxxxxxxxxXXXXXX$$$$$$$$XXxxxxxxxxxxxxxxxxXXX$$$$XXXXXxxxxxx++++++++++xxxxxxxxxxxx
+++++++++++++++++++++xxxxxxxxxxXXXX$$$$$$$$XXXxxxxxxxxxxxxxxxxXXX$$$$$$XXxxxxxx+++++++++xxxxxxxxxxxxx
+++++++++++++++++++++xxxxxxxxxxxXXXX$$$$$$$XXXxxxxxxxxxxxxxxxxxXXX$$$$$XXxxxxxx++++++++++xxxx++xxxxxx
++++++++++++++++++++++xxxxxxxxxxxXXXX$$$&$$XXXXxxxxxxxxxxxxxxxxXXXX$$$$XXXXxxxx++++++++++xxxxxxxxxxxx
+++++++++++++++++++++++xxxxxxxxxxxXXXX$&&$$$XXXXxxxxxxxxxxxxxxxxXXXX$$$XXXXxxxx+xxxxxxxxxxxxxxxxxxxxx
+++++++++++++++++++++++xxxxxxxxxxxXXXXX$&$$$XXXXXxxxxxxxxxxxxxxXXXXX$$$$XXxxxxxxxxxxxxxxxxxxxxXXXXxxx
++++++++++++++++++++++++xxxxxxxxxxxXXXXX$$$$$XXXXXXxxxxxxxxxXxxXXXXXX$$$XXXxxxxxxxxxxxxxxxxxXXXXXXXxx
++++++++++++++++++++++++++xxxxxxxxxXXXXX$$$$$$XXXXXXXxxxxxxxxxxXXXXXX$$$XXXxxxxxxxxxxxxxXXXXXXxxxxxxx
++++++++++++++++++++++++++++xxxxxxxxxXXXX$$$$$$XXXXXXXXxxxxxxxXXXXXXX$$$XXXXxxxxxxxxxxxXXXXxxxxxxxxxx
++++++++++++++++++++++++++++++xxxxxxxxXXXX$$$$$XXXXXXXXXXxxxXXXXXXXX$$$$$XXXXxxxxxxxxXXXXxxxxxxxxxxxx
++++++++++++++++++++++++++++++++xxxxxxXXXXX$$$$$$XXXXXXXXXXXXXXXXX$$$$$$$XXXXXxxxxxxXX$XXxxxxxxxxxxxx
++++++++++++++++++++++++++++++++xxxxxxxxXXXX$$$$$$XXXXXXXXXXXXXXX$$$$$$$$$XXXXXxxxXXXX$XxxxxxxxxxXXXX
++++++++++++++++++++++++++++++++++xxXXXXX$$$$$$$$$$$$$X$$$$$$$$$$$$$$$$$$$$XXXXXXXXXXXXXxXXXXXXXXXXXX
+++++++++++++++++++++++++xxXXX$$$$$$$XX$XXXXXXXXXXXXxXXXxXXXXXXXXXXXX$$$$$$$XXXXXXXXXXXXXXXXX$$X$$$XX
++++++++++++++++++xxXX$$$$$$$$$XX$XXXXXXxXxxxxxx+xx+++++xxxxxxxxxxxxxXxXXXX$$$$$$$$X$$XXX$$$$$$$$$$$$
+++++++++++++xXXX$XXXXXXXXXXXXXXXxxxxxxx++++;;;;;;;;;;;;;;;;;;+;;++++xxxxxxxXXXX$$$$$$$$$$&$$$&$$$$$$
++++++++++xXXXXXXX$XXXxxXXXxxXxxxx+;+++;+;;;:::::;:::;:::::;:;;:;;;;;++++++xxxxXXXX$$$$$&&&&&&&&&&&$$
++++++++XXXXXXXxxxxxx++x++xxx+++++;;;;;;:;:::::::::::::::::::::::::::;;;;;;++++xxxXXXX$$$$$&&&&$&&&&&
++++++XXXXXXxxx++XX+++;;;;;;;;::;;;:::::::.:::.:......::...:..:...::.::::;;;;;;;+++xxxXXX$$$$$$$$$$$$
++++x$$XxxxxXXxxXX$X++;;:::::::::::::::.::::::::::::::::::.::..::..::::::::::;;;;;++++xxxXX$$$&$$$$$$
+++X$XXXxxx+x$$$$X$;;:..::::::::::::::::::::::::::::;;;::;:::::::::::::::::::::;;;;;++++xxXX$$$&$$$$$
x+xXXXXXxx++xx++x;:::::::::;;;:;::::;++xxxxxxxxxxxxxxxxxxxxxxxx+++;;;;::::::::::;:;;;;;+++xxXX$$&$$$$
xxxxxx++;;;:::::;::::::;;++xx+xxxxxxx+++++++++++++++++++++++++++xxxxxxxxxx++;;;;;;;;;;;;++xxXXX$$&&&$
xxxxx+++;;;;;;;;;;+xxxxxxxxxx+++++++++++++++++++++++++++++++++++++++++++xxxxXXXx++++++;+++xxXXX$$&$$$
xxxxx+++x++xxxxxxxxxxxxxx++++++++;;;;;;;;;;+;;;;;;;;;;;+++++++++++++++++++++xxxXX$$$XxxxxxxxXXX$$&&&&
xxxxx+xx++xxxxxxxxxx++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;+++++++++++++++++x++xxxxxxxxxxXXXXXXX$$$&&&&
xxxx+++xxxxxx+++++++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+++;;++++++++++++++xx+xxxxxxxxXXX$$$&&&&&
XXxxxx+++++++++++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++x++++++xxxxxxxxXXXX$&&&
XXxxx+xx+++++++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++++++++xxxxxxxxXXXXX
XXxxxx++++++++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++++++++++xxxxxxxxxx
XXxxxx+++++++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++++++++++++++xxxxxx
XXXxxxx++++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+++++++++++++++++++++++++++++++xxx
XXxxxxx+++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++;;;;;;;;;++++++++++++++++++++++xx
XXXxxx+++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+++++++++++++++++++++++
XXXxxx+++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++
XXXxxxx++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+++++++++++++++
XXXxxx+++++++++++;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+++;;;+++++++++++
XXXXxxx+++++++++;;;;;;;;;;;;;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++
image sourced from https://www.vtherpatlas.org/
""","One of two green snakes in New Jersey. This one has smooth dorsal scales, and it camouflages in marshes, meadows, open woods, and other terrestrial habitats. They like to eat spineless caterpillars, moths, ants, snails, worms, and more. See also: Opheodrys Aestivus.",animalia,chordata,reptilia,squamata,serpentes,colubridae,opheodrys)
RS=snake("Regina septemvittata","Queen Snake","""+xxxxXXXXXXXXXXXXXXXXXXXxxx+;;;::::::::::;+xXXXXXX$$$$XXXXXXXXXXXXX$$XXX$$$$$X$XXx+;;;;;;;;;;;;;;;;;+
++++++xxxxXXXXXXXXXXXXXXXXXXXXXXXx+;;;;;+XXXXXXXXX$$XXXXXXXxXXXXXXXX$XXX$$XX$$$$XXx+;;;;;;;;;;;;;++++
xxx++++++++++xxxXXXXX$$$XX$$XXXX$$XXxxxXXXXXX$$XXX$XXXxXXXXXXXXXXXXX$$XX$$$$$$$$$Xx+;;;;;;;;+++++++++
xxxxxxxxx++++++++xxxxXX$$$$$$$$$XXXXXXXXXXXXXXXXXXXXXxxXXXXxxXXXXX$$$$$$$$$$$$$$$Xx++;;;+++++++++++++
xxxxxxxxxxxx+++++++++xxxXXXX$$$XXXXXXXxxXXXXX$$XxxXXXxxXXXXXxXXXXX$$$$$$$&&$$&&$$Xx++++++++x+++++++++
xxxxxxxxxxxxxxxxxxxxxxx+++xxxXXXXXXXXXXXX$$XXX$XxxXXXXxxXXXXX$$$X$$$$$$$$&&&&&&$$Xx++++++++++++++++++
xxxxxxxxxxxxxxxxxxxxxxxxx+xxXXXXXXXXXXXXX$$XXX$XxxX$$XxxXXXX$$$$$$$$&&&&&&&&$$$$Xxx++++++++++++++++++
xxxxxxxxxxxxxxxx++xxxxxxxxxXXXXXXXXxXX$$$$$XXXXXXXXXXXXX$$$$$&$$$&&&&&$$$$$$$$$$Xxx++++++++++++++++++
xxxxxxxxx++++++++++xxxxxxxXxXXXXXXXXX$$$$$$XXX$$XXXXXXX$$$$$$&&$$$&&&$$$$$$$$$XXxx+++++++++++++++++++
xxxxx++++++++++++++xxxxxXXXXXXXXXxXX$$$$$$$XXX$$$X$$$$$&&&&&&&&$$$$$$$$$$$$XXXxxxxxxxx+++++++++++;;;;
xx++++++++++++++++xxxxxX$$XxxXXXXXXX$$$$$XXX$X$$$$$$$$$$$$$$$$$$$$$$$XXXxxx+++++xxxxxxxx++++++++++;;;
x+++++++++++++++++xxxxXX$XXxXXXXXXX$$$$$$$$$$$$$$$&&$$$$$$$$$$$$$XXx++++;;;;++++++xxxxxxxxx++++++++;;
+++++++++++++++++xxxxXX$$$XXXXXXXXXX$$$$$$$$$$$$$$$$$$$$$$$$$XXXx+;;:::;;;+++++++++xxxxxxxxx++++++++;
+++++++++++++++++xxxxX$$$$XXXXXxxXXX$$$$$$$$$$$$$$$$$$$$$$$Xx++;::::::;;++x++++++++xxxxxxxxx+++++++++
++++++++++++++++xxxxXX$$$XXXXXXXXXXXX$$$$$$$$$$$$$$$$$$$$Xx+;::::::;;++xxxx+++++++++xxxxxxxxxx+++++++
+++++++++++++++xxxxxX$$$$$$$$XXXxXXXXX$$$$$$$$$$$$$$$$$$Xx+;:::::;+xxxxxx+++++++++++xxxxxxxxxxxx+++++
++++++++++++++xxxxxxX$$$$$$XXXXXXXXXXXX$$$$$$$$$$$$$$$$$x;:::::;+xxxx++++++++++;;++++xxxxxxxxxxxxxx++
+++++xx+++++++++++++x$$$$$$X$$XXXxXXXXXX$X$$XX$$$$$$$$$Xx;:::;+xxx+++;+++++++;;;;;;;++xxxxxxxxxxxxxxx
+++++++++++++++++++xX$&&$$$$XXX$XxXXXXxXXXXX$$XX$$$$$$$Xx;::;++++++++++++++++;;;;;;;;++++xxxxxxxxxxxx
++++++++++++++++++++x$&&$$$$$$$$$XxX$XXXXXXXXXXX$$$$$$$XXXXXXXxxxx+++++++++++;;;;;;;;++++++++xxxxxxxx
+++++++++++++;;;;;;;+X&&$$$$$XXX$$X$$$$$$$$XX$$$X$$$$XXXXXXXXXXX$Xxx++++++++++;;;;;;;;++++++++++++xxx
++++++++++++;;;;;;;;+X$&&&$$$$$$XX$$$$$$$X$$$X$XXX$$$$$$XX$$$XXXXXXXxx++++++++++;;;;;;;;;;;;;;;++++++
+++++++++++++;;;;;;;++X$&$&&$$$$XXXXXXX$$XX$X$$$$$$&$$$$XXXXXXXXXXXX$$X++++++++++++++;;;;;;;;;;;;;+++
++++++++++++;;;;;;;;;;+X$$$$$$$$XXXXXXXXXXX$$$$$$$$$$$$$$$$XXXXX$XXXX$$X++++++++++++;;;;;;;;;;;;;;;++
+++++++++++;;;;;;;;;;;;+X$$$$$$$$XXXXXXXXXXXXX;$$$$X$$$$$$$$$$$$$XXXXX$$X+++++++++++++;;;;;;;;;;;;;;+
+++++++++;;;;;;;;;;;;;;;x$$$$$$$$$XXXXXXXXXxxX$$$$$$XXXXXXXX$$$$XXXXXX$$X+;;+++++++++++++;;;;;;;;;;;;
++++++++;;;;;;;;;;;;;;;;X$&$$$$$$$XX$XXXXXXXXXXXxXX$$XXXXXXXXXXXXXXXXXXXX::;++++++++++++++;;;;;;;;;;;
+++++++;;;;;;;;;;;;;;;;+$$$$&$$$$$XX$XXXXX$XXxxxXXXXXXXXXXXXX$XXXXXXXXXXx::;;;+++++++++++++++;;;;;;;;
++++++;;;;;;;;;;;;;;;;;+xxX$$$$$&$$$$$$$$XXXXxXXXXXXXXXXXXXXXX$XXxxxXXXXx;::;;;+++++++++++++++++++;;;
+;;;;++;;;;;;;;;;;;;;;;;++X$&&$$$$$$$$$$XXXXXXXXXXXXXXXXXXXXXXX$XXxxXXxxXX;;;;;;;++++++++++++++++++++
;;;;+++;;;;;;;;;;;;;;;;;;+xX$&&&$$$$$$$$$$XXXXXX$XXXXXXxxxXXXxxxX$xxXXXX&&x;;;;;;;++++++xxx++++++++++
++++;+;;;;;;;;;;;;;;;;;;;;;;+x$&&&&$$$$$$XXXXXXXX$xxXXxxxxXXXXXXxxxxX$$X$&x+;;;;;+++++++++xx+++++++++
+++;;;;;;;;;;;;;;;;;;;;;;;+;;;+xX$&&&&$$&$$XXXXxX$XXXxXXXXXxxxxXXXxxX$$$$XX+;;++++++++++++x++++++++++
++;;;;;;;;;;;;;;;;;;;;;;++;;;:::::+$&&&$$$XX$XXXXXXXxx+++xXxXxXXxxx+xX$$&$X;;++++++++++++x+++++++++++
+;;;;;;;;;;;;;;;;;;;;;;++;;;+;:::::;X&&$$$$X$$$$XxxXxXXXXXXxxxx+x+++xX$$$$X+;++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;;;;;+++;;;;;+;::::::;X$$&&XXX&$$$Xxxxxxx++xxx+xXxxxX$$$XX+;;++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;;;;++++;;;;;;++;;:::::+$$&&$$&&&$$Xxx++xxxxxXXxx+++X$$$XXx;;++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;;;;++++;;;;;;;;++;;::::X$$$$&&&&&$$X$Xxxxx++xx;;;+xx$$$Xx;;++++++++++++++;;;;;;;++++
;;;;;;;;;;;;;;;;;;;+++++++;;;;;;;++++;::;+X$$&&&$&$$$&&$Xx+;+++++++xXXXxx;;;+++++++++++;;;;;;;;;;;+++
;;;;;;;;;;;;;;;;;;;;++++++++;;+++++++x+;:::xX$$$&&$$$&&$xXx+;;;:.:xx+xx;+;;++++++++++;;;;;;;;;;;;;;++
;;;;;;;;;;;;;;;;;;;;++++++++++++++++++++++;;;;+X$$$$$&&$XXx:;:::::::::::;;;++++++++++;;;;;;;;;;;;;+++
;;;;;;;;;;;;;;;;;;;+++++++++++++++++++++x+++;:;+++X+x$xxXx+:::::::::::::;;;++++++++++;;;;;;;;++++++++
;;;;;;;;;;;;;;;;;;+++++++++++++++++++++++++++++;::;+;;+x;::::::;:++x++;+x+;++++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;;++++++++++++++++++++++++++++++++;;++;:;::::+X&&$$x+;+++++++++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;+++++++++++++++++++++++++++++++++++++;;;+;;+$$$&&Xx;;;++++++++++++++++++++++++++++++
;;;;;::::;;;;;;;;;+++++++++++++++++++++++++++++++++++;;+;;;+xxX$&$Xx+++++++xx+++++++++++++++++++x++++
;;;;;;;:;;;;;;;;;;+++++++++++++++++++++++++++++++++++++++++;;+X$&$$XxxxXXXx+++++++++++++++++++x++++++
;;;;;;;;;;;;;;;;;;;;;;+++++++++++++++++++++++++++++++++++++;+x$$XxX$XXx++++++++++++++++++++++xx++++++
;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++++++++++++++++xxxxXXXx+;;;;+++++++++++++++++++++++++xxxx++++
;;;;;;;;;;;;;;+;;;;;;;;;;;;;;+++++++++++++++++++++xxxxxxxx+++;;;;;;;;++++++++++++++++++++++++++++++++
;;;;;;;;;;;;+++;;;;;;;;;;;;;;;+++++++++++++++++++++++++++++;;;;;;;;;;++++++++++++;+++++++++++++++++++
;;;;;;;;;;+++;;;;;;;;;;;;;;;;;;;+++++++++++++++++++++++++++++;;;;;;;;++++++++++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++++++++;;;;;++++++++++++++++++++++++++++++++
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++++++;;;;++++++++++++;;+++++++++++++++++++
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;++++++++++++++;;;;+++++++++++++++++++++++++++++++++
;;;;;;;;;;;;;;;;++++++++;;;;;;;;::::;;;;;;;;;;;;;;;+++++++++++++;;;;+++++++++++++++++++++++++++++++++
;;;;;;;;;;;;;;;;+++++++++;;;;;;;:::::::::::::;;;;;;;;+++++++++++;;;;+++++++++++++++++++++++++++++++++
""","This snake can be from olive to gray or dark brown in color, with peach or yellow stripes that run across its length on its underbelly, a feature no other species has. They are very picky when it comes to living conditions. it lives in areas with at least 10 °C running streams and watersheds with stony, rocky bottoms. The reason for their very specific habitat is because of their diet, consisting of over 90% crayfish. They also eat things like tadpoles, minnows, newts, etc.",animalia,chordata,reptilia,squamata,serpentes,colubridae,regina)

#redefine the allsnakes array now that the snakes are objects
allsnakes=[CAA,CCC,CCConstr,PG,PO,HP,LGG,LT,NSS,OA,OV,RS]
def snakeDex(): #list of all the snakes for the user to interact with
    print("")
    print("########## THE SNAKEDEX ##########")
    iter=0
    for x in allsnakes: #go through the list of snakes and print their names
        iter+=1
        print(iter,": ",x.name,sep="")
    while True:
        choose=input("Input the number of the snake you would like to view.")
        try:
            choose=int(choose)
        except:
            print("ERROR: please input a whole number.")
            continue
        if choose > len(allsnakes) or choose < 0:
            print("ERROR: please choose from the list provided.")
            continue
        else:
            allsnakes[choose-1].snake()
    

snakeDex()
