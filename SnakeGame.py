import pygame
import random

pygame.init()

width = 1000
height = 600
gameWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
#color
white = (255,255,255)
black = (0,0,0)
green = (0,125,0)
red = (255,0,0)
mix = (125,125,125)
blue = (0,0,255)
yel = (255,0,150)
wt = (255,200,200)


sfont = pygame.font.SysFont("comicsansms",15)
mfont = pygame.font.SysFont("comicsansms",38)
lfont = pygame.font.SysFont("comicsansms",80)
clock = pygame.time.Clock()
icon = pygame.image.load("G:/apple.png")
pygame.display.set_icon(icon)


def makeSnake(snakeList,blockSize):
  
  for xy in snakeList[:-1]:
    pygame.draw.rect(gameWindow,green,(xy[0],xy[1],blockSize,blockSize))
  xy=snakeList[-1]
  pygame.draw.rect(gameWindow,yel,(xy[0],xy[1],blockSize,blockSize))
  pygame.display.update()
    
def makeBoarder(sizeApple):
  pygame.draw.rect(gameWindow,mix,(0,20,sizeApple,height))
  pygame.draw.rect(gameWindow,mix,(width-sizeApple,20,-width,sizeApple))
  pygame.draw.rect(gameWindow,mix,(0,height-sizeApple,width,sizeApple))
  pygame.draw.rect(gameWindow,mix,(width-sizeApple,height-sizeApple,sizeApple,-height+41))
  pygame.display.update()
  



def message(text,color,y_disp,size,wid,hei):
  if size == "small":
    testSurface = sfont.render(text,True,color)
  elif size == "medium":
    testSurface = mfont.render(text,True,color)
  elif size == "large":
    testSurface = lfont.render(text,True,color)
  textReact = testSurface.get_rect()
  textReact.center = (wid/2),(hei/2)+y_disp
  gameWindow.blit(testSurface,textReact)

def pause():
  paus = True
  while paus == True:
    message("Press P to Pause game!.",white,y_disp=-80,size="medium",wid=width,hei=height)
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
def GameOver(snakeLength):
  gameover = True
  
  while gameover is True:
    message("Press P to Pause game!.",white,y_disp=-80,size="medium",wid=width,hei=height)
    message("Game Over!",blue,y_disp=-80,size="large",wid=width,hei=height)
    message("Score : "+str(snakeLength-1),green,y_disp=20,size="large",wid=width,hei=height)
    message("Press  N to New Game (or) Q to quit!.",black,y_disp=120,size="medium",wid=width,hei=height)
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
def intro():
  intro = True
  while intro == True:
    gameWindow.fill(mix)
    message("Snake Game!",green,y_disp=-175,size="large",wid=width,hei=height)
    message("1) Eat more Apples and get high score. ",blue,y_disp=-80,size="medium",wid=width,hei=height)
    message("2) Use arrow keys to move snake.",blue,y_disp=-30,size="medium",wid=width,hei=height)
    message("3) For Pause Game press P ; while playing game ",blue,y_disp=20,size="medium",wid=width,hei=height)
    message("4) Warning!!! Don't allow snake to strike walls.",blue,y_disp=70,size="medium",wid=width,hei=height)
    message("Press  C to continue (or) Q to quit!.",black,y_disp=140,size="medium",wid=width,hei=height)
    message("By RajeshLalam",white,y_disp=190,size="small",wid=width,hei=height)
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
    
def playGame():
  snakeSpeed=8
  gameOver = False
  xAxis = width/2
  yAxis = height/2
  blockSize = 10
  xMove = 0
  yMove = 0
  sizeApple = 20
  snakeList = []
  snakeLength = 1
  gameWindow.fill(white)
  mod=50
  score = 0
  xApple = random.randrange(sizeApple,width-2*sizeApple)
  yApple = random.randrange(sizeApple+2*blockSize,height-2*sizeApple)
  while gameOver is False :
    for event in pygame.event.get():
      if event.type == pygame.QUIT :
        pygame.quit()
        quit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT :
          xMove = -blockSize
          yMove = 0
        elif event.key == pygame.K_RIGHT :
          xMove = blockSize
          yMove = 0
        elif event.key == pygame.K_UP :
          yMove = -blockSize
          xMove = 0
        elif event.key == pygame.K_DOWN :
          yMove = blockSize
          xMove = 0
        elif event.key == pygame.K_p :
          pause()
    xAxis+=xMove
    yAxis+=yMove
    if xAxis < sizeApple or xAxis > width-sizeApple-blockSize or yAxis < sizeApple+2*blockSize or yAxis > height-sizeApple-blockSize:
      xAxis-=xMove
      yAxis-=yMove
      gameOver = True
    newMove =[xAxis,yAxis]
    snakeList.append(newMove)
    if len(snakeList) > snakeLength:
      del snakeList[0]
    if newMove in snakeList[:-1]:
      if len(snakeList)>=3 and newMove == snakeList[-3]:
        xMove*=-1
        yMove*=-1
        xAxis+=(xMove)
        yAxis+=(yMove)
        newMove =[xAxis,yAxis]
        del snakeList[-1]
        snakeList.append(newMove)
      else:
        xAxis-=xMove
        yAxis-=yMove
        gameOver = True
    gameWindow.fill(white)
    makeBoarder(sizeApple)
    message("Score : "+str(snakeLength-1),blue,y_disp=0,size="small",wid=100,hei=20)
    message("Press P to Pause game!.",wt,y_disp=-80,size="medium",wid=width,hei=height)
    pygame.display.update()
    #pygame.draw.rect(gameWindow,red,(xApple,yApple,sizeApple,sizeApple))
    gameWindow.blit(icon,(xApple,yApple))
    pygame.display.update()
    makeSnake(snakeList,blockSize)

    if xAxis > xApple and xAxis < xApple+sizeApple or  xAxis+blockSize > xApple and xAxis+blockSize < xApple+sizeApple:
      if yAxis > yApple and yAxis < yApple+sizeApple or  yAxis+blockSize > yApple and yAxis+blockSize < yApple+sizeApple:
        xApple = random.randrange(sizeApple,width-2*sizeApple)
        yApple = random.randrange(sizeApple+2*blockSize,height-2*sizeApple)
        #pygame.draw.rect(gameWindow,red,(xApple,yApple,sizeApple,sizeApple))
        gameWindow.blit(icon,(xApple,yApple))
        pygame.display.update()
        snakeLength+=1
        message("Score : "+str(snakeLength-1),blue,y_disp=0,size="small",wid=100,hei=20)
        pygame.display.update()
    if snakeLength!=1 and (snakeLength-1)%mod ==0:
      snakeSpeed+=2
      mod+=50
    clock.tick(snakeSpeed)
  if gameOver ==True:
    GameOver(snakeLength)
intro()

pygame.quit()


