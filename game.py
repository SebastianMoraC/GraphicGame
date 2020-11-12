import pygame, sys, json
import player
from pygame.draw import circle

#Const

TILEWIDTH = 0
TILEHEIGHT = 0
MAPWIDTH = 0
MAPHEIGHT = 0
MATRIZMAP = []
WIDTH = 800
HEIGHT = 800
speed = 2
trueScroll = [0,0]
#---------------------------------------------------------------------------------------------------
#Map Funtions 
def uploadMap(map):
    #Open File
    global TILEWIDTH, TILEHEIGHT, MAPWIDTH, MAPHEIGHT, MATRIZMAP
    file = open(map+".json","r")
    data = json.load(file)
    file.close

    #Get Size
    TILEWIDTH = data["tilewidth"]
    TILEHEIGHT = data["tileheight"]
    MAPWIDTH = data["width"]
    MAPHEIGHT = data["height"]

    #Get Map
    map = []
    for item in data["layers"]:
        map = item["data"] #Get the map


    for i in range(0,len(map),MAPWIDTH):
        MATRIZMAP.append(map[i:i+MAPWIDTH])
'''    for i in range(MAPHEIGHT):
        print(MATRIZMAP[i])'''
#cut
def cut(image, rectangle):
    rect = pygame.Rect(rectangle)
    imgCut = pygame.Surface(rect.size).convert()
    imgCut.blit(image,(0,0),rect)
    return imgCut

def arrayTileSet(image):
    x,y = 0,0
    leftFiles =[]

    for i in range(30):
        for j in range(27):
            imageCut = cut(image,(x,y,16,16))
            leftFiles.append(imageCut)
            x += 18
        x = 0
        y += 18
        
    return leftFiles

#---------------------------------------------------------------------------------------------------
#Main

def main():
    pygame.init()
    
    #Screen
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Game")
    
    #Player
    myPlayer = player.Xena((50,345),speed)
    
    #Map
    img = pygame.image.load("images/worldMario.png")
    uploadMap("maps/mapGG")
    left = arrayTileSet(img)

    #Font and Text
    white = pygame.Color("#FFFFFF")
    fontOne = pygame.font.Font(None,37)
    timeAux = 1
    while True:
        screen.blit(myPlayer.clipping,myPlayer.rectClip)
        
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        myPlayer.eventS(event)
        
        #Time
        timeS = pygame.time.get_ticks() //1000      #The time is miliseconds so we divide in 1000
        if(timeAux == timeS):
            print(timeAux)
            timeAux += 1
        
        #Draw Map
        for i in range(MAPHEIGHT):
            for j in range(MAPWIDTH):
                numTile = MATRIZMAP[i][j]
                tileImg = left[numTile-1]
                tileImg = pygame.transform.scale(tileImg,(TILEWIDTH, TILEHEIGHT))
                screen.blit(tileImg, (j*TILEWIDTH, i*TILEHEIGHT))
        screen.blit(myPlayer.clipping,(myPlayer.rectClip.x,myPlayer.rectClip.y))

        #Count
        count = fontOne.render("Time left: " + str(60-timeS),0,white)    #Write the cont: 
        screen.blit(count,(635,5)) #Show the cont in the screen

        pygame.display.flip()

if __name__ == "__main__":
    main()