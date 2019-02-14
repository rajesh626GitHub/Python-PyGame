import pygame
import random
import time
pygame.init()

width =  660
height = 660
gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bomber")
#color
white = (255,255,255)
black = (0,0,0)
dgreen = (0,125,0)
dred = (205,0,0)
dyellow = (255,185,15)
mix = (125,125,125)
blue = (0,0,255)
yel = (255,0,150)
wt = (255,200,200)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
dblue = (0,0,139)
safeCol = (191,62,255)

sfont = pygame.font.SysFont("comicsansms",15)
msfont = pygame.font.SysFont("comicsansms",30)
mfont = pygame.font.SysFont("comicsansms",38)
lfont = pygame.font.SysFont("comicsansms",80)
clock = pygame.time.Clock()
speed = 8
enemySpeed = 10


def makeBomber(bomberList,blockSize):
  for xy in bomberList[:-1]:
    pygame.draw.rect(gameWindow,green,(xy[0],xy[1],50,50))
  xy=bomberList[-1]
  pygame.draw.rect(gameWindow,yel,(xy[0],xy[1],50,50))
  #gameWindow.blit(man,(xy[0],xy[1]))
  pygame.display.update()

def makeEnemy(blockSize):
  global enemyMove
  for index in range(len(enemyList)):
    enemyList[index][1]+=enemyMove[index]
    if enemyList[index][1] <0:
      enemyMove[index] = -enemyMove[index]
      enemyList[index][1]+=enemyMove[index]
    if enemyList[index][1]>height-blockSize:
      enemyMove[index] = -enemyMove[index]
      enemyList[index][1]+=enemyMove[index]
    #pygame.draw.rect(gameWindow,red,(enemyList[index][0],enemyList[index][1],50,50))
    gameWindow.blit(enemy,(enemyList[index][0],enemyList[index][1]))
    pygame.display.update()


def message(text,color,y_disp,size,wid,hei):
  if size == "small":
    testSurface = sfont.render(text,True,color)
  elif size == "medium":
    testSurface = mfont.render(text,True,color)
  elif size == "large":
    testSurface = lfont.render(text,True,color)
  elif size == "msmall":
    testSurface = msfont.render(text,True,color)
  textReact = testSurface.get_rect()
  textReact.center = (wid/2),(hei/2)+y_disp
  gameWindow.blit(testSurface,textReact)

def pause():
  paus = True
  while paus == True:
    gameWindow.fill(white)
    message("Paused!",blue,y_disp=-80,size="large",wid=width,hei=height)
    message("Press  C to continue (or) Q to quit!.",black,y_disp=60,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_c :
          paus = False
def setMode():
  global enemyMax
  intro = True
  while intro == True:
    gameWindow.fill(white)
    message(" click E to Easy ",red,y_disp=-120,size="medium",wid=width,hei=height)
    message(" In Easy mode you have to complete game with in 50 sec ",red,y_disp=-70,size="msmall",wid=width,hei=height)
    message(" click M to Medium",green,y_disp=-20,size="medium",wid=width,hei=height)
    message(" In Medium mode you have to complete game with in 75 sec ",green,y_disp=30,size="msmall",wid=width,hei=height)
    message(" click H to Hard ",blue,y_disp=80,size="medium",wid=width,hei=height)
    message(" In Hard mode you have to complete game with in 100 sec ",blue,y_disp=120,size="msmall",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e :
          enemyMax = 9
          playGame()
        elif event.key == pygame.K_m :
          enemyMax = 18
          playGame()
        elif event.key == pygame.K_h :
          enemyMax = 27
          playGame()

    
def GameOver():
  gameover = True
  while gameover is True:
    gameWindow.fill(white)
    message("Game Completed!",blue,y_disp=-150,size="medium",wid=width,hei=height)
    message("Press  N to New Game (or) Q to quit!.",black,y_disp=150,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_n :
          playGame()
def gameCompleted(seconds):
  gameover = True
  while gameover is True:
    gameWindow.fill(white)
    message("WOW CONGRATS!!!",blue,y_disp=-150,size="large",wid=width,hei=height)
    message("Score : "+str(score),green,y_disp=-40,size="large",wid=width,hei=height)
    message("Time : "+str(int(seconds))+" sec",green,y_disp=60,size="large",wid=width,hei=height)
    message("Press  N to New Game (or) Q to quit!.",black,y_disp=150,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_n :
          setMode()
          playGame()

def intro():
  intro = True
  while intro == True:
    gameWindow.fill(mix)
    message("Bomber Game!",green,y_disp=-175,size="large",wid=width,hei=height)
    message("1) Place bomb Smash enemy and get high score. ",blue,y_disp=-80,size="medium",wid=width,hei=height)
    message("2) Use arrow keys to move bomber.",blue,y_disp=-30,size="medium",wid=width,hei=height)
    message("3) Press B to put Bomb. And keep bomber away from bomb ",blue,y_disp=20,size="msmall",wid=width,hei=height)
    message("4) Warning!!! Don't allow bomber to touch enemy",blue,y_disp=70,size="medium",wid=width,hei=height)
    message("Press  C to continue (or) Q to quit! or p to pause.",black,y_disp=140,size="medium",wid=width,hei=height)
    message("By RajeshLalam",white,y_disp=190,size="medium",wid=width,hei=height)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q :
          pygame.quit()
          quit()
        elif event.key == pygame.K_c :
          playGame()
topDown = []
DownTop = []
enemyList = []
enemyMove = []
bomb = [-1,-1]
def makeWall():
  global topDown
  global DownTop
  for i in range(50,width,200):
    topDown.append([i,0])
  for i in range(150,width,200):
    DownTop.append([i,height])
def topDownWall():
  for xy in topDown:
    for i in range(xy[1],height-50,50):
      gameWindow.blit(rock,(xy[0],i))
    #pygame.draw.rect(gameWindow,green,(xy[0],xy[1],50,height-50))
def DownTopWall(blockSize):
  for xy in DownTop:
    for i in range(xy[1],49,-50):
      gameWindow.blit(rock,(xy[0],i))
  #pygame.draw.rect(gameWindow,green,(xy[0],xy[1],50,-height+51))

def checkDash(blockSize,sizeEnemy):
  global enemyList
  global score
  if bomb!=[-1,-1]:
    xAxis=bomb[0]
    yAxis=bomb[1]
    for ind  in range(len(enemyList)):
      xEnemy,yEnemy=enemyList[ind][0],enemyList[ind][1]
      if (xAxis==xEnemy) and ((yAxis >= yEnemy and yAxis <= yEnemy+sizeEnemy) or  (yAxis+blockSize >= yEnemy and yAxis+blockSize <= yEnemy+sizeEnemy)):
        del enemyList[ind]
        score+=100
        return 1
  return 0
boardList=[]
redList=[]
blueList=[]
yellowList=[]
greenList=[]
safeZone = []
def firstPlayer(x,y,xi,yi):
  gameWindow.fill(white)
  col = dred
  for i in range(x,4,xi):
    for j in range(y,4,yi):
      if i!=x and j !=y and i !=3 and j !=3:
        redList.append(boardList[i][j])
      else:
        pygame.draw.rect(gameWindow,col,(boardList[i][j][0],boardList[i][j][1],60,60))
        pygame.display.update()
      
def secondPlayer(x,y,xi,yi):
  col = dblue
  for i in range(x,4,xi):
    for j in range(y,6,yi):
      if i!=x and j !=y and i !=3 and j !=7:
        blueList.append(boardList[i][j])
      else:
        pygame.draw.rect(gameWindow,col,(boardList[i][j][0],boardList[i][j][1],60,60))
        pygame.display.update()
      
def thirdPlayer(x,y,xi,yi):
  col = dgreen
  for i in range(x,6,xi):
    for j in range(y,4,yi):
      
      if i!=x and j !=y and i !=7 and j !=3:
        greenList.append(boardList[i][j])
      else:
        pygame.draw.rect(gameWindow,col,(boardList[i][j][0],boardList[i][j][1],60,60))
        pygame.display.update()
      
def fourthPlayer(x,y,xi,yi):
  col = dyellow
  for i in range(x,6,xi):
    for j in range(y,6,yi):
      
      if i!=x and j !=y and i !=7 and j !=7:
        yellowList.append(boardList[i][j])
      else:
        pygame.draw.rect(gameWindow,col,(boardList[i][j][0],boardList[i][j][1],60,60))
        pygame.display.update()
def makeClear(called,i,xy,ind,dis,same):
  if called =="r":
    colorList=redCome
    col=red
    dcol=dred
  elif called == "b":
    colorList  = blueCome
    col=blue
    dcol=dblue
  elif called == "g":
    colorList = greenCome
    col=green
    dcol=dgreen
  else:
    colorList = yellowCome
    col=yellow
    dcol=dyellow

  if i in safeZone or i == redStart[0] or i==greenStart[0] or i==blueStart[0] or i==yellowStart[0]:
    if xy ==[-1,-1] and i in safeZone:
      pygame.draw.rect(gameWindow,safeCol,(i[0],i[1],60,60))
    elif xy==[-1,-1] and i == redStart[0]:
      pygame.draw.rect(gameWindow,dred,(i[0],i[1],60,60))
    elif xy==[-1,-1] and i == greenStart[0]:
      pygame.draw.rect(gameWindow,dgreen,(i[0],i[1],60,60))
    elif xy==[-1,-1] and i == blueStart[0]:
      pygame.draw.rect(gameWindow,dblue,(i[0],i[1],60,60))
    elif xy==[-1,-1] and i == yellowStart[0]:
      pygame.draw.rect(gameWindow,dyellow,(i[0],i[1],60,60))
    elif xy != [-1,-1]:
      pygame.draw.rect(gameWindow,col,(i[0]+dis[ind][0],i[1]+dis[ind][1],15,15))
  else:
    if xy==[-1,-1] and( i in redStart[-4:] or i in greenStart[-4:] or i in blueStart[-4:] or i in yellowStart[-4:]):
      pygame.draw.rect(gameWindow,dcol,(i[0],i[1],60,60))
    elif xy ==[-1,-1] and (i in redList or i in greenList or i in yellowList or i in blueList):
      pygame.draw.rect(gameWindow,white,(i[0],i[1],60,60))
    elif xy !=[-1,-1] and (i in redList or i in greenList or i in yellowList or i in blueList):
      pygame.draw.rect(gameWindow,col,(i[0],i[1],60,60))
    elif xy == [-1,-1] :
      if colorList.count(i)>1:
        pygame.draw.rect(gameWindow,white,(i[0],i[1],60,60))
      else:
        pygame.draw.rect(gameWindow,white,(i[0],i[1],60,60))
    elif xy != [-1,-1] :
      if colorList.count(i)>1:
        pygame.draw.rect(gameWindow,col,(i[0]+same[ind][0],i[1]+same[ind][1],30,30))
      else:
        pygame.draw.rect(gameWindow,col,(i[0],i[1],60,60))
def botsVisible(xy):
  dis=[[0,0],[0,15],[15,0],[15,15]]
  same = [[0,0],[0,30],[30,0],[30,30]]
  ind=0
  for i in redCome:
    makeClear("r",i,xy,ind,dis,same)
    ind+=1
  pygame.display.update()
  dis=[[30,0],[30,15],[45,0],[45,15]]
  ind=0
  for i in blueCome:
    makeClear("b",i,xy,ind,dis,same)
    ind+=1
  pygame.display.update()
  dis=[[0,30],[0,45],[15,30],[15,45]]
  ind=0 
  for i in yellowCome:
    makeClear("y",i,xy,ind,dis,same)
    ind+=1
  pygame.display.update()
  dis=[[30,30],[30,45],[45,30],[45,45]]
  ind=0
  for i in greenCome:
    makeClear("g",i,xy,ind,dis,same)
    ind+=1
  pygame.display.update()

redStart = []
blueStart = []
greenStart = []
yellowStart=[]
redCome = []
greenCome = []
blueCome = []
yellowCome = []
def safeZones():
  for xy in safeZone:
    pygame.draw.rect(gameWindow,safeCol,(xy[0],xy[1],60,60))
  pygame.display.update()

def makeBoard():
  for i in range(0,height,60):
    temp=[]
    for j in range(0,width,60):
      temp.append([j,i])
    boardList.append(temp)

def startAndSafe():
  global redCome,greenCome,blueCome,yellowCome
  
  l = len(boardList)
  pygame.draw.rect(gameWindow,red,(boardList[l/2][l/2][0],boardList[l/2][l/2][1],60,60))
  text_to_screen( "Roll", boardList[l/2][l/2][0], boardList[l/2][l/2][1], 30,black)
  mid = boardList[l/2][l/2]
  pygame.draw.rect(gameWindow,dblue,(mid[0],mid[1]-60,60,60))
  start = mid[1]-120
  for i in range(3):
    pygame.draw.rect(gameWindow,dblue,(mid[0],start,60,60))
    start-=60
  blueStart.append([mid[0]+60,start+60])
  safeZone.append([blueStart[0][0]-120,blueStart[0][1]])
  pygame.draw.rect(gameWindow,dblue,(mid[0]+60,start+60,60,60)) #blue start
  pygame.draw.rect(gameWindow,dyellow,(mid[0]+60,mid[1],60,60))
  start = mid[0]+120
  for i in range(3):
    pygame.draw.rect(gameWindow,dyellow,(start,mid[1],60,60))
    start+=60
  yellowStart.append([start-60,mid[1]+60])
  safeZone.append([yellowStart[0][0],yellowStart[0][1]-120])
  pygame.draw.rect(gameWindow,dyellow,(start-60,mid[1]+60,60,60)) #yellow start
  pygame.draw.rect(gameWindow,dgreen,(mid[0],mid[1]+60,60,60))
  start = mid[1]+120
  for i in range(3):
    pygame.draw.rect(gameWindow,dgreen,(mid[0],start,60,60))
    start+=60
  greenStart.append([mid[0]-60,start-60])
  safeZone.append([greenStart[0][0]+120,greenStart[0][1]])
  pygame.draw.rect(gameWindow,dgreen,(mid[0]-60,start-60,60,60)) # green start
  pygame.draw.rect(gameWindow,dred,(mid[0]-60,mid[1],60,60))
  start = mid[0]-120
  for i in range(3):
    pygame.draw.rect(gameWindow,dred,(start,mid[1],60,60))
    start-=60
  redStart.append([start+60,mid[1]-60])
  safeZone.append([redStart[0][0],redStart[0][1]+120])
  pygame.draw.rect(gameWindow,dred,(start+60,mid[1]-60,60,60)) # red start
  pygame.display.update()

def text_to_screen( text, x, y, size,color):
  text = str(text)
  font = sfont = pygame.font.SysFont("comicsansms",size)
  text = font.render(text, True, color)
  gameWindow.blit(text, (x, y))
def check(lis):
  for i,j in lis:
    pygame.draw.rect(gameWindow,white,(i,j,60,60))
  pygame.display.update()
turn=[1,2,3,4]
point = 0
def howManyOut(bots,num,colCome):
  count = 0
  inBots = []
  outBots=[]
  valid = []
  for i in range(len(bots)):
    if bots[i]==-1:
      inBots.append(colCome[i])
    else:
      outBots.append(colCome[i])
    if bots[i]!=-1 and bots[i]+num<len(redStart):
      valid.append(colCome[i])
  return inBots,outBots,valid
def wait():
  for i in range(1999999):
    c=1
def goRight(start,limit):
  path = []
  for i in range(start[0],start[0]+limit*60,60):
    path.append([i,start[1]])
  return path
def goUp(start,limit):
  path = []
  for i in range(start[1],start[1]-limit*60,-60):
    path.append([start[0],i])
  #print start,path
  return path
def goLeft(start,limit):
  path = []
  for i in range(start[0],start[0]-limit*60,-60):
    path.append([i,start[1]])
  return path
def goDown(start,limit):
  path = []
  for i in range(start[1],start[1]+limit*60,60):
    path.append([start[0],i])
  return path
fullPath=[]
def setPath():
  global redStart,blueStart,yellowStart,greenStart,fullPath
  fullPath.append(redStart[0])
  path = goRight(fullPath[-1],4)
  for i in path[1:]:
    fullPath.append(i)
  path =goUp(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goRight(fullPath[-1],3)
  for i in path[1:]:
    fullPath.append(i)
  path =goDown(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goRight(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goDown(fullPath[-1],3)
  for i in path[1:]:
    fullPath.append(i)
  path =goLeft(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goDown(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goLeft(fullPath[-1],3)
  for i in path[1:]:
    fullPath.append(i)
  path =goUp(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goLeft(fullPath[-1],5)
  for i in path[1:]:
    fullPath.append(i)
  path =goUp(fullPath[-1],3)
  for i in path[1:]:
    fullPath.append(i)
  for i in range(1,len(fullPath)-1):
    redStart.append(fullPath[i])
  path =goRight(redStart[-1],5)
  for i in path[1:]:
    redStart.append(i)
  for i in fullPath[11:]:
    blueStart.append(i)
  for i in fullPath[0:9]:
    blueStart.append(i)
  path =goDown(blueStart[-1],5)
  for i in path[1:]:
    blueStart.append(i)
  for i in fullPath[21:]:
    yellowStart.append(i)
  for i in fullPath[:19]:
    yellowStart.append(i)
  path =goLeft(yellowStart[-1],5)
  for i in path[1:]:
    yellowStart.append(i)
  for i in fullPath[31:]:
    greenStart.append(i)
  for i in fullPath[:29]:
    greenStart.append(i)
  path =goUp(greenStart[-1],5)
  for i in path[1:]:
    greenStart.append(i)
  
redBots=[-1,-1,-1,-1]
greenBots=[-1,-1,-1,-1]
blueBots=[-1,-1,-1,-1]
yellowBots=[-1,-1,-1,-1]

comple = []
def visibleWinner():
  for i in range(len(comple)):
    if comple[i]==0:
      text_to_screen( str(i+1), 100,60 , 80,black)
    elif comple[i]==1:
      text_to_screen( str(i+1), blueList[0][0]-25,blueList[0][1] , 80,black)
    elif comple[i]==2:
      text_to_screen( str(i+1), yellowList[0][0]-30,yellowList[0][1]-60 , 80,black)
    elif comple[i]==3:
      text_to_screen( str(i+1), greenList[0][0]+30,greenList[0][1]-60 , 80,black)
glag=0

def makeBoarder():
  for i in fullPath:
    pygame.draw.rect(gameWindow,black,(i[0],i[1],60,2))
    pygame.draw.rect(gameWindow,black,(i[0]+59,i[1],1,60))
    pygame.draw.rect(gameWindow,black,(i[0],i[1]+59,60,1))
    pygame.draw.rect(gameWindow,black,(i[0],i[1],60,1))
  pygame.display.update()
def playGame():
  global turn ,point,redBots,blueBots,greenBots,yellowBots,win,comple,glag
  comple=[]
  gameOver = False
  if glag==0:
    makeBoard()
    glag=1
  l = len(boardList)
  xMid = boardList[l/2][l/2][0]
  yMid = boardList[l/2][l/2][1]
  firstPlayer(0,0,1,1)
  secondPlayer(0,len(boardList[0])-1,1,-1)
  thirdPlayer(len(boardList[0])-1,0,-1,1)
  fourthPlayer(len(boardList[0])-1,len(boardList[0])-1,-1,-1)
  startAndSafe()
  safeZones()
  
  for i in range(4):
    redCome.append(redList[i])
    greenCome.append(greenList[i])
    blueCome.append(blueList[i])
    yellowCome.append(yellowList[i])
  botsVisible([-11,-11])
  setPath()
  makeBoarder()

  while gameOver is False :
    makeBoarder()
    flag=0
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT :
        pygame.quit()
        quit()
      if evento.type == pygame.MOUSEBUTTONDOWN:
        pos=pygame.mouse.get_pos()
        xy=[xMid,yMid]
        if (xy[0]<pos[0] and xy[0]+60>pos[0] ) and (xy[1]<pos[1] and xy[1]+60>pos[1]):
          flag=1
        visibleWinner()
        if point ==0 and flag==1 :
          if point in comple:
            point = (point+1)%4
            continue
          #print "valid red"
          for rep in range(6):
            num = random.randint(1,6)
          #print num
          pygame.draw.rect(gameWindow,red,(xMid,yMid,60,60))
          text_to_screen( "  " +str(num), xMid, yMid, 30,black)
          pygame.display.update()
          Move =False
          inBots,outBots,valid = howManyOut(redBots,num,redCome)
          #print "bots ",inBots,outBots,valid
          if len(inBots)==4 and num!=6:
            wait()
            Move=True
          if len(valid) ==1 and (num!=6 or len(inBots)==0 ):
            wait()
            i=redCome.index(valid[0])
            botsVisible([-1,-1])
            pygame.display.update()
            pre = redBots[i]+1
            redBots[i]+=num
            #for i in range(pre,redBots[i],1):
            redCome[i]=redStart[redBots[i]]
            botsVisible(redCome[i])
            Move=True
            if num==6:
              repeat=True
            if  redBots[i]== len(redStart)-1:
              repeat=True
            if  (redCome[i] not in safeZone and redCome[i] not in redStart[0] and redCome[i] not in greenStart[0] and redCome[i] not in blueStart[0] and redCome[i] not in yellowStart[0]):
              if (redCome[i] in blueCome ):
                ind = blueCome.index(redCome[i])
                blueCome[ind]=blueList[ind]
                blueBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if (redCome[i] in blueCome ):
                  ind = blueCome.index(redCome[i])
                  blueCome[ind]=blueList[ind]
                  blueBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
              elif redCome[i] in yellowCome :
                ind = yellowCome.index(redCome[i])
                yellowCome[ind]=yellowList[ind]
                yellowBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if redCome[i] in yellowCome :
                  ind = yellowCome.index(redCome[i])
                  yellowCome[ind]=yellowList[ind]
                  yellowBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
              elif( redCome[i] in greenCome):
                ind = greenCome.index(redCome[i])
                greenCome[ind]=greenList[ind]
                greenBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if( redCome[i] in greenCome):
                  ind = greenCome.index(redCome[i])
                  greenCome[ind]=greenList[ind]
                  greenBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
          if len(valid)==0 and num!=6:
            Move=True
          if len(inBots)==0 and len(valid)==0:
            Move=True
          repeat=False
          glag=0
          for i in redBots:
            if i != len(redStart)-1:
              glag=1
              break
          if glag==0:
            comple.append(0)
            Move = True
          while not Move:
            makeBoarder()
            for evento in pygame.event.get():
              if evento.type == pygame.QUIT :
                pygame.quit()
                quit()
              if evento.type == pygame.MOUSEBUTTONDOWN :
                #print "taken"
                pos=pygame.mouse.get_pos()
                flag=0
                for i in range(4):
                  xy= redCome[i]
                  #print xy,inBots
                  if (xy[0]<=pos[0] and xy[0]+60>=pos[0] ) and (xy[1]<=pos[1] and xy[1]+60>=pos[1]):
                    flag=1
                    break
                if flag==0 :
                  continue
                if xy in inBots and num!=6:
                  continue
                if xy in outBots and xy not in valid:
                  continue
                if xy in inBots and num==6:
                  #print xy,inBots
                  botsVisible([-1,-1])
                  pygame.display.update()
                  redBots[i]+=1
                  redCome[i]=redStart[redBots[i]]
                  botsVisible(redCome[i])
                  repeat=True
                  Move=True
                if xy not in valid :
                  continue
                if xy in valid and num==6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = redBots[i]+1
                  redBots[i]+=num
                  #for i in range(pre,redBots[i],1):
                  redCome[i]=redStart[redBots[i]]
                  botsVisible(redCome[i])
                  if  (redCome[i] not in safeZone and redCome[i] not in redStart[0] and redCome[i] not in greenStart[0] and redCome[i] not in blueStart[0] and redCome[i] not in yellowStart[0]):
                    if (redCome[i] in blueCome ):
                      ind = blueCome.index(redCome[i])
                      blueCome[ind]=blueList[ind]
                      blueBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if (redCome[i] in blueCome ):
                        ind = blueCome.index(redCome[i])
                        blueCome[ind]=blueList[ind]
                        blueBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif redCome[i] in yellowCome :
                      ind = yellowCome.index(redCome[i])
                      yellowCome[ind]=yellowList[ind]
                      yellowBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if redCome[i] in yellowCome :
                        ind = yellowCome.index(redCome[i])
                        yellowCome[ind]=yellowList[ind]
                        yellowBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif( redCome[i] in greenCome):
                      ind = greenCome.index(redCome[i])
                      greenCome[ind]=greenList[ind]
                      greenBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if( redCome[i] in greenCome):
                        ind = greenCome.index(redCome[i])
                        greenCome[ind]=greenList[ind]
                        greenBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                  repeat=True
                  Move=True
                if xy in valid and num!=6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = redBots[i]+1
                  redBots[i]+=num
                  #for i in range(pre,redBots[i],1):
                  redCome[i]=redStart[redBots[i]]
                  botsVisible(redCome[i])
                  Move=True
                  if  redBots[i]== len(redStart)-1:
                    repeat=True
                  if  (redCome[i] not in safeZone and redCome[i] not in redStart[0] and redCome[i] not in greenStart[0] and redCome[i] not in blueStart[0] and redCome[i] not in yellowStart[0]):
                    if (redCome[i] in blueCome ):
                      ind = blueCome.index(redCome[i])
                      blueCome[ind]=blueList[ind]
                      blueBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if (redCome[i] in blueCome ):
                        ind = blueCome.index(redCome[i])
                        blueCome[ind]=blueList[ind]
                        blueBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif redCome[i] in yellowCome :
                      ind = yellowCome.index(redCome[i])
                      yellowCome[ind]=yellowList[ind]
                      yellowBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if redCome[i] in yellowCome :
                        ind = yellowCome.index(redCome[i])
                        yellowCome[ind]=yellowList[ind]
                        yellowBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif( redCome[i] in greenCome):
                      ind = greenCome.index(redCome[i])
                      greenCome[ind]=greenList[ind]
                      greenBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if( redCome[i] in greenCome):
                        ind = greenCome.index(redCome[i])
                        greenCome[ind]=greenList[ind]
                        greenBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True

          if repeat == True:
            continue
          #print "com " ,comple
          if 1 not in comple:
            pygame.draw.rect(gameWindow,blue,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=1
          elif 2 not in comple:
            pygame.draw.rect(gameWindow,yellow,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=2
          elif 3 not in comple:
            pygame.draw.rect(gameWindow,green,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=3
          else:
            GameOver()
          continue

        if point ==1 and flag==1 :
          if point in comple:
            point = (point+1)%4
            continue
          #print "valid blue"
          for rep in range(6):
            num = random.randint(1,6)
          #print num
          pygame.draw.rect(gameWindow,blue,(xMid,yMid,60,60))
          text_to_screen( "  " +str(num), xMid, yMid, 30,black)
          pygame.display.update()
          Move =False
          inBots,outBots,valid = howManyOut(blueBots,num,blueCome)
          #print "bots ",inBots,outBots,valid
          if len(inBots)==4 and num!=6:
            Move=True
            wait()
          if len(valid) ==1 and (num!=6 or len(inBots)==0 ):
            wait()
            i=blueCome.index(valid[0])
            botsVisible([-1,-1])
            pygame.display.update()
            pre = blueBots[i]+1
            blueBots[i]+=num
            #for i in range(pre,blueBots[i],1):
            blueCome[i]=blueStart[blueBots[i]]
            botsVisible(blueCome[i])
            Move=True
            if num==6 :
              repeat=True
            if  blueBots[i]== len(blueStart)-1:
              repeat=True
            if  (blueCome[i] not in safeZone and blueCome[i] not in redStart[0] and blueCome[i] not in greenStart[0] and blueCome[i] not in blueStart[0] and blueCome[i] not in yellowStart[0]):
              if (blueCome[i] in redCome ):
                ind = redCome.index(blueCome[i])
                redCome[ind]=redList[ind]
                redBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if (blueCome[i] in redCome ):
                  ind = redCome.index(blueCome[i])
                  redCome[ind]=redList[ind]
                  redBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
              elif blueCome[i] in yellowCome :
                ind = yellowCome.index(blueCome[i])
                yellowCome[ind]=yellowList[ind]
                yellowBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if blueCome[i] in yellowCome :
                  ind = yellowCome.index(blueCome[i])
                  yellowCome[ind]=yellowList[ind]
                  yellowBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
              elif( blueCome[i] in greenCome):
                ind = greenCome.index(blueCome[i])
                greenCome[ind]=greenList[ind]
                greenBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if( blueCome[i] in greenCome):
                  ind = greenCome.index(blueCome[i])
                  greenCome[ind]=greenList[ind]
                  greenBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
          if len(valid)==0 and num!=6:
            Move=True
          if len(inBots)==0 and len(valid)==0:
            Move=True
          repeat=False
          glag=0
          for i in blueBots:
            if i != len(blueStart)-1:
              glag=1
              break
          if glag==0:
            comple.append(1)
            Move = True
          while not Move:
            makeBoarder()
            for evento in pygame.event.get():
              if evento.type == pygame.QUIT :
                pygame.quit()
                quit()
              if evento.type == pygame.MOUSEBUTTONDOWN :
                #print "taken"
                pos=pygame.mouse.get_pos()
                flag=0
                for i in range(4):
                  xy= blueCome[i]
                  #print xy,inBots
                  if (xy[0]<=pos[0] and xy[0]+60>=pos[0] ) and (xy[1]<=pos[1] and xy[1]+60>=pos[1]):
                    flag=1
                    #print "saticified"
                    break
                if flag==0 :
                  continue
                if xy in inBots and num!=6:
                  continue
                if xy in outBots and xy not in valid:
                  continue
                if xy in inBots and num==6:
                  #print xy,inBots
                  botsVisible([-1,-1])
                  pygame.display.update()
                  blueBots[i]+=1
                  blueCome[i]=blueStart[blueBots[i]]
                  botsVisible(blueCome[i])
                  repeat=True
                  Move=True
                if xy not in valid :
                  continue
                if xy in valid and num==6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = blueBots[i]+1
                  blueBots[i]+=num
                  #for i in range(pre,blueBots[i],1):
                  blueCome[i]=blueStart[blueBots[i]]
                  botsVisible(blueCome[i])
                  if  (blueCome[i] not in safeZone and blueCome[i] not in redStart[0] and blueCome[i] not in greenStart[0] and blueCome[i] not in blueStart[0] and blueCome[i] not in yellowStart[0]):
                    if (blueCome[i] in redCome ):
                      ind = redCome.index(blueCome[i])
                      redCome[ind]=redList[ind]
                      redBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if (blueCome[i] in redCome ):
                        ind = redCome.index(blueCome[i])
                        redCome[ind]=redList[ind]
                        redBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif blueCome[i] in yellowCome :
                      ind = yellowCome.index(blueCome[i])
                      yellowCome[ind]=yellowList[ind]
                      yellowBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if blueCome[i] in yellowCome :
                        ind = yellowCome.index(blueCome[i])
                        yellowCome[ind]=yellowList[ind]
                        yellowBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif( blueCome[i] in greenCome):
                      ind = greenCome.index(blueCome[i])
                      greenCome[ind]=greenList[ind]
                      botsVisible([-11,-11])
                      greenBots[ind]=-1
                      repeat = True
                      if( blueCome[i] in greenCome):
                        ind = greenCome.index(blueCome[i])
                        greenCome[ind]=greenList[ind]
                        botsVisible([-11,-11])
                        greenBots[ind]=-1
                        repeat = True
                  repeat=True
                  Move=True
                if xy in valid and num!=6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = blueBots[i]+1
                  blueBots[i]+=num
                  #for i in range(pre,blueBots[i],1):
                  blueCome[i]=blueStart[blueBots[i]]
                  botsVisible(blueCome[i])
                  Move=True
                  if  blueBots[i]== len(blueStart)-1:
                    repeat=True
                  if  (blueCome[i] not in safeZone and blueCome[i] not in redStart[0] and blueCome[i] not in greenStart[0] and blueCome[i] not in blueStart[0] and blueCome[i] not in yellowStart[0]):
                    if (blueCome[i] in redCome ):
                      ind = redCome.index(blueCome[i])
                      redCome[ind]=redList[ind]
                      redBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if (blueCome[i] in redCome ):
                        ind = redCome.index(blueCome[i])
                        redCome[ind]=redList[ind]
                        redBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif blueCome[i] in yellowCome :
                      ind = yellowCome.index(blueCome[i])
                      yellowCome[ind]=yellowList[ind]
                      yellowBots[ind]=-1
                      botsVisible([-11,-11])
                      repeat = True
                      if blueCome[i] in yellowCome :
                        ind = yellowCome.index(blueCome[i])
                        yellowCome[ind]=yellowList[ind]
                        yellowBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif( blueCome[i] in greenCome):
                      ind = greenCome.index(blueCome[i])
                      greenCome[ind]=greenList[ind]
                      botsVisible([-11,-11])
                      greenBots[ind]=-1
                      repeat = True
                      if( blueCome[i] in greenCome):
                        ind = greenCome.index(blueCome[i])
                        greenCome[ind]=greenList[ind]
                        botsVisible([-11,-11])
                        greenBots[ind]=-1
                        repeat = True

          if repeat == True:
            continue
          #print "com " ,comple
          if 2 not in comple:
            pygame.draw.rect(gameWindow,yellow,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=2
          elif 3 not in comple:
            pygame.draw.rect(gameWindow,green,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=3
          elif 0 not in comple:
            pygame.draw.rect(gameWindow,red,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=0
          else:
            GameOver()
          continue
      
          
        if point ==2 and flag==1 :
          if point in comple:
            point = (point+1)%4
            continue
          #print "valid yellow"
          for rep in range(6):
            num = random.randint(1,6)
          #print num
          pygame.draw.rect(gameWindow,yellow,(xMid,yMid,60,60))
          text_to_screen( "  " +str(num), xMid, yMid, 30,black)
          pygame.display.update()
          Move =False
          inBots,outBots,valid = howManyOut(yellowBots,num,yellowCome)
          #print "bots ",inBots,outBots,valid
          if len(inBots)==4 and num!=6:
            Move=True
            wait()
          if len(valid) ==1 and (num!=6 or len(inBots)==0 ):
            wait()
            i=yellowCome.index(valid[0])
            botsVisible([-1,-1])
            pygame.display.update()
            pre = yellowBots[i]+1
            yellowBots[i]+=num
            #for i in range(pre,yellowBots[i],1):
            yellowCome[i]=yellowStart[yellowBots[i]]
            botsVisible(yellowCome[i])
            Move=True
            if num==6:
              repeat=True
            if  yellowBots[i]== len(yellowStart)-1:
              repeat=True
            if  (yellowCome[i] not in safeZone and yellowCome[i] not in redStart[0] and yellowCome[i] not in greenStart[0] and yellowCome[i] not in blueStart[0] and yellowCome[i] not in yellowStart[0]):
              if (yellowCome[i] in redCome ):
                ind = redCome.index(yellowCome[i])
                redCome[ind]=redList[ind]
                redBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if (yellowCome[i] in redCome ):
                  ind = redCome.index(yellowCome[i])
                  redCome[ind]=redList[ind]
                  redBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
              elif yellowCome[i] in blueCome :
                ind = blueCome.index(yellowCome[i])
                blueCome[ind]=blueList[ind]
                blueBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if yellowCome[i] in blueCome :
                  ind = blueCome.index(yellowCome[i])
                  blueCome[ind]=blueList[ind]
                  blueBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
              elif( yellowCome[i] in greenCome):
                ind = greenCome.index(yellowCome[i])
                greenCome[ind]=greenList[ind]
                greenBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if( yellowCome[i] in greenCome):
                  ind = greenCome.index(yellowCome[i])
                  greenCome[ind]=greenList[ind]
                  greenBots[ind]=-1
                  botsVisible([-11,-11])
                  repeat = True
          if len(valid)==0 and num!=6:
            #print "invalid"
            Move=True
          if len(inBots)==0 and len(valid)==0:
            Move=True
          repeat=False
          glag=0
          for i in yellowBots:
            if i != len(yellowStart)-1:
              glag=1
              break
          if glag==0:
            comple.append(2)
            Move = True
          while not Move:
            makeBoarder()
            for evento in pygame.event.get():
              if evento.type == pygame.QUIT :
                pygame.quit()
                quit()
              if evento.type == pygame.MOUSEBUTTONDOWN :
                #print "taken"
                pos=pygame.mouse.get_pos()
                flag=0
                for i in range(4):
                  xy= yellowCome[i]
                  #print xy,inBots
                  if (xy[0]<=pos[0] and xy[0]+60>=pos[0] ) and (xy[1]<=pos[1] and xy[1]+60>=pos[1]):
                    flag=1
                    #print "saticified"
                    break
                if flag==0 :
                  continue
                if xy in inBots and num!=6:
                  continue
                if xy in outBots and xy not in valid:
                  continue
                if xy in inBots and num==6:
                  #print "moved",xy,inBots
                  botsVisible([-1,-1])
                  pygame.display.update()
                  yellowBots[i]+=1
                  yellowCome[i]=yellowStart[yellowBots[i]]
                  botsVisible(yellowCome[i])
                  repeat=True
                  Move=True
                if xy not in valid :
                  continue
                if xy in valid and num==6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = yellowBots[i]+1
                  yellowBots[i]+=num
                  #for i in range(pre,yellowBots[i],1):
                  yellowCome[i]=yellowStart[yellowBots[i]]
                  botsVisible(yellowCome[i])
                  if  (yellowCome[i] not in safeZone and yellowCome[i] not in redStart[0] and yellowCome[i] not in greenStart[0] and yellowCome[i] not in blueStart[0] and yellowCome[i] not in yellowStart[0]):
                    if (yellowCome[i] in redCome ):
                      ind = redCome.index(yellowCome[i])
                      redCome[ind]=redList[ind]
                      botsVisible([-11,-11])
                      redBots[ind]=-1
                      repeat = True
                      if (yellowCome[i] in redCome ):
                        ind = redCome.index(yellowCome[i])
                        redCome[ind]=redList[ind]
                        redBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif yellowCome[i] in blueCome :
                      ind = blueCome.index(yellowCome[i])
                      blueCome[ind]=blueList[ind]
                      blueBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if yellowCome[i] in blueCome :
                        ind = blueCome.index(yellowCome[i])
                        blueCome[ind]=blueList[ind]
                        blueBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    elif( yellowCome[i] in greenCome):
                      ind = greenCome.index(yellowCome[i])
                      greenCome[ind]=greenList[ind]
                      greenBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if( yellowCome[i] in greenCome):
                        ind = greenCome.index(yellowCome[i])
                        greenCome[ind]=greenList[ind]
                        greenBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                
                  
                  repeat=True
                  Move=True
                if xy in valid and num!=6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = yellowBots[i]+1
                  yellowBots[i]+=num
                  #for i in range(pre,yellowBots[i],1):
                  yellowCome[i]=yellowStart[yellowBots[i]]
                  botsVisible(yellowCome[i])
                  Move=True
                  if  yellowBots[i]== len(yellowStart)-1:
                    repeat=True
                  if  (yellowCome[i] not in safeZone and yellowCome[i] not in redStart[0] and yellowCome[i] not in greenStart[0] and yellowCome[i] not in blueStart[0] and yellowCome[i] not in yellowStart[0]):
                    if (yellowCome[i] in redCome ):
                      ind = redCome.index(yellowCome[i])
                      redCome[ind]=redList[ind]
                      botsVisible([-11,-11])
                      redBots[ind]=-1
                      repeat = True
                      if (yellowCome[i] in redCome ):
                        ind = redCome.index(yellowCome[i])
                        redCome[ind]=redList[ind]
                        redBots[ind]=-1
                        botsVisible([-11,-11])
                        repeat = True
                    elif yellowCome[i] in blueCome :
                      ind = blueCome.index(yellowCome[i])
                      blueCome[ind]=blueList[ind]
                      blueBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if yellowCome[i] in blueCome :
                        ind = blueCome.index(yellowCome[i])
                        blueCome[ind]=blueList[ind]
                        blueBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    elif( yellowCome[i] in greenCome):
                      ind = greenCome.index(yellowCome[i])
                      greenCome[ind]=greenList[ind]
                      greenBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if( yellowCome[i] in greenCome):
                        ind = greenCome.index(yellowCome[i])
                        greenCome[ind]=greenList[ind]
                        greenBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                

          if repeat == True:
            continue
          #print "com " ,comple
          if 3 not in comple:
            pygame.draw.rect(gameWindow,green,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=3
          elif 0 not in comple:
            pygame.draw.rect(gameWindow,red,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=0
          elif 1 not in comple:
            pygame.draw.rect(gameWindow,blue,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=1
          else:
            GameOver()
          continue

        if point ==3 and flag==1 :
          if point in comple:
            point = (point+1)%4
            continue
          #print "valid green"
          for rep in range(6):
            num = random.randint(1,6)
          #print num
          pygame.draw.rect(gameWindow,green,(xMid,yMid,60,60))
          text_to_screen( "  " +str(num), xMid, yMid, 30,black)
          pygame.display.update()
          Move =False
          inBots,outBots,valid = howManyOut(greenBots,num,greenCome)
          #print "bots ",inBots,outBots,valid
          if len(inBots)==4 and num!=6:
            Move=True
            wait()
          if len(valid) ==1 and (num!=6 or len(inBots)==0 ):
            wait()
            i=greenCome.index(valid[0])
            botsVisible([-1,-1])
            pygame.display.update()
            pre = greenBots[i]+1
            greenBots[i]+=num
            #for i in range(pre,greenBots[i],1):
            greenCome[i]=greenStart[greenBots[i]]
            botsVisible(greenCome[i])
            Move=True
            if num==6:
              repeat=True
            if  greenBots[i]== len(greenStart)-1:
              repeat=True
            if  (greenCome[i] not in safeZone and greenCome[i] not in redStart[0] and greenCome[i] not in greenStart[0] and greenCome[i] not in blueStart[0] and greenCome[i] not in yellowStart[0]):
              if (greenCome[i] in redCome ):
                ind = redCome.index(greenCome[i])
                redCome[ind]=redList[ind]
                redBots[ind]=-1
                botsVisible([-11,-11])
                repeat = True
                if (greenCome[i] in redCome ):
                  ind = redCome.index(greenCome[i])
                  redCome[ind]=redList[ind]
                  redBots[ind]=-1
                  repeat = True
                  botsVisible([-11,-11])
              elif greenCome[i] in blueCome :
                ind = blueCome.index(greenCome[i])
                blueCome[ind]=blueList[ind]
                blueBots[ind]=-1
                repeat = True
                botsVisible([-11,-11])
                if greenCome[i] in blueCome :
                  ind = blueCome.index(greenCome[i])
                  blueCome[ind]=blueList[ind]
                  blueBots[ind]=-1
                  repeat = True
                  botsVisible([-11,-11])
              elif( greenCome[i] in yellowCome):
                ind = yellowCome.index(greenCome[i])
                yellowCome[ind]=yellowList[ind]
                yellowBots[ind]=-1
                repeat = True
                botsVisible([-11,-11])
                if greenCome[i] in yellowCome :
                  ind = yellowCome.index(greenCome[i])
                  yellowCome[ind]=yellowList[ind]
                  yellowBots[ind]=-1
                  repeat = True
                  botsVisible([-11,-11])
          if len(valid)==0 and num!=6:
            Move=True
          if len(inBots)==0 and len(valid)==0:
            Move=True
          repeat=False
          glag=0
          for i in greenBots:
            if i != len(greenStart)-1:
              glag=1
              break
          if glag==0:
            comple.append(3)
            Move = True
          while not Move:
            makeBoarder()
            for evento in pygame.event.get():
              if evento.type == pygame.QUIT :
                pygame.quit()
                quit()
              if evento.type == pygame.MOUSEBUTTONDOWN :
                #print "taken"
                pos=pygame.mouse.get_pos()
                flag=0
                for i in range(4):
                  xy= greenCome[i]
                  #print xy,inBots
                  if (xy[0]<=pos[0] and xy[0]+60>=pos[0] ) and (xy[1]<=pos[1] and xy[1]+60>=pos[1]):
                    flag=1
                    #print "saticified"
                    break
                if flag==0 :
                  continue
                if xy in inBots and num!=6:
                  continue
                if xy in outBots and xy not in valid:
                  continue
                if xy in inBots and num==6:
                  #print xy,inBots
                  botsVisible([-1,-1])
                  pygame.display.update()
                  greenBots[i]+=1
                  greenCome[i]=greenStart[greenBots[i]]
                  botsVisible(greenCome[i])
                  repeat=True
                  Move=True
                if xy not in valid :
                  continue
                if xy in valid and num==6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = greenBots[i]+1
                  greenBots[i]+=num
                  #for i in range(pre,greenBots[i],1):
                  greenCome[i]=greenStart[greenBots[i]]
                  botsVisible(greenCome[i])
                  if  (greenCome[i] not in safeZone and greenCome[i] not in redStart[0] and greenCome[i] not in greenStart[0] and greenCome[i] not in blueStart[0] and greenCome[i] not in yellowStart[0]):
                    #print "kill"
                    if (greenCome[i] in redCome ):
                      ind = redCome.index(greenCome[i])
                      redCome[ind]=redList[ind]
                      redBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if (greenCome[i] in redCome ):
                        ind = redCome.index(greenCome[i])
                        redCome[ind]=redList[ind]
                        redBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    elif greenCome[i] in blueCome :
                      ind = blueCome.index(greenCome[i])
                      blueCome[ind]=blueList[ind]
                      blueBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if greenCome[i] in blueCome :
                        ind = blueCome.index(greenCome[i])
                        blueCome[ind]=blueList[ind]
                        blueBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    elif( greenCome[i] in yellowCome):
                      ind = yellowCome.index(greenCome[i])
                      yellowCome[ind]=yellowList[ind]
                      yellowBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if greenCome[i] in yellowCome :
                        ind = yellowCome.index(greenCome[i])
                        yellowCome[ind]=yellowList[ind]
                        yellowBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    
                  repeat=True
                  Move=True
                if xy in valid and num!=6:
                  botsVisible([-1,-1])
                  pygame.display.update()
                  pre = greenBots[i]+1
                  greenBots[i]+=num
                  #for i in range(pre,greenBots[i],1):
                  greenCome[i]=greenStart[greenBots[i]]
                  botsVisible(greenCome[i])
                  Move=True
                  if  greenBots[i]== len(greenStart)-1:
                    repeat=True
                  if  (greenCome[i] not in safeZone and greenCome[i] not in redStart[0] and greenCome[i] not in greenStart[0] and greenCome[i] not in blueStart[0] and greenCome[i] not in yellowStart[0]):
                    #print "kill"
                    if (greenCome[i] in redCome ):
                      ind = redCome.index(greenCome[i])
                      redCome[ind]=redList[ind]
                      redBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if (greenCome[i] in redCome ):
                        ind = redCome.index(greenCome[i])
                        redCome[ind]=redList[ind]
                        redBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    elif greenCome[i] in blueCome :
                      ind = blueCome.index(greenCome[i])
                      blueCome[ind]=blueList[ind]
                      blueBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if greenCome[i] in blueCome :
                        ind = blueCome.index(greenCome[i])
                        blueCome[ind]=blueList[ind]
                        blueBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    elif( greenCome[i] in yellowCome):
                      ind = yellowCome.index(greenCome[i])
                      yellowCome[ind]=yellowList[ind]
                      yellowBots[ind]=-1
                      repeat = True
                      botsVisible([-11,-11])
                      if greenCome[i] in yellowCome :
                        ind = yellowCome.index(greenCome[i])
                        yellowCome[ind]=yellowList[ind]
                        yellowBots[ind]=-1
                        repeat = True
                        botsVisible([-11,-11])
                    
          if repeat == True:
            continue
          #print "com " ,comple
          if 0 not in comple:
            pygame.draw.rect(gameWindow,red,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=0
          elif 1 not in comple:
            pygame.draw.rect(gameWindow,blue,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=1
          elif 2 not in comple:
            pygame.draw.rect(gameWindow,yellow,(xMid,yMid,60,60))
            text_to_screen( "Roll", xMid, yMid, 30,black)
            pygame.display.update()
            point=2
          else:
            GameOver()
          continue
    
      



playGame()
pygame.quit()


