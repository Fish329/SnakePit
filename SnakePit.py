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
CAA=()
CCC=()
CCCon=()
PG=()
PA=()
HP=()
LGG=()
LT=()
NSS=()
OA=()
OV=()
RS=()
allsnakes=[CAA,CCC,CCCon,PG,PA,HP,LGG,LT,NSS,OA,OV,RS]
class kingdom:
    def __init__(self,name,details,snakes): #define all the kinds of levels
        self.name=name
        self.details=details
        self.snakes=snakes
        self.level="Kingdom"
    def printLevel(self):
        print("")
        print("=[",self.level," ",self.name,"]=",sep="")
        print(self.details)
        print("Snakes in this list that are in this level:")
        iter=0
        for x in self.snakes:
            iter+=1
            print(iter,": ",x,sep="")
        
class phylum(kingdom):
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
class snake:
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
    def snake(self):
        print("")
        print("=[",self.name, " (",self.comname,") ]=", sep="")
        print(self.picture)
        print(self.details)
        print("")
        print("[TAXONOMY:]")
        print("1. Kingdom:",self.k.name)
        print("2. Phylum:",self.p.name)
        print("3. Class:",self.c.name)
        print("4. Order:",self.o.name)
        print("5. Suborder:",self.so.name)
        print("6. Family:",self.f.name)
        print("7. Genus:",self.f.name)
        while True:
            choice=input("Input 0 to return to SnakeDex, or input the number of a Taxonomy level to see details about it. ")
            try:
                choice=int(choice)
            except:
                print("ERROR: please input a whole number.")
                continue
            choice=int(choice)
            if choice > 7 or choice < 0:
                print("ERROR: there is no item at that index. please choose from the list given.")
            else:
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
coluber=genus("Coluber","This genus contains only one species of snake, the Coluber Constricter.",snakes=[CCCon])
lampropeltis=genus("lampropeltis","commonly called Kingsnakes, the snakes of this genus eat other snakes!! Some kingsnakes are muted brown in color, but others are more colorful with red, yellow, gray, and lavender coloring.",[LGG,LT])
heterodon=genus("Heterodon","The upturned snouts of these snakes have earned them the name Hognose snakes. Those poor guys. They have distinct threatening tactics.",[HP])
regina=genus("Regina","The snakes in this genus are semiaquatic. They get their common name, crayfish snakes, from their primary diet.",[RS])
opheodrys=genus("Opheodrys","A genus containing two green snakes, of opposite scale-smoothness.",[OA,OV])
nerodia=genus("Nerodia","A genus of heavy snakes that vary in size. They have flat heads, with varying patterns per species. usually brown or olive-green colored.",[NSS])
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
#TODO: finish writing all this.
CAA.snake()
