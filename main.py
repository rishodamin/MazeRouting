from pathFinder import FindPath
import pygame
pygame.init()

# color variables
white = (250,250,250)
greenL = (150,255,150)
dark = (50,50,50)
halfwhite = (199,189,153)
darkgrey = (100,100,100)
red = (255,100,140)
blue = (50,80,255)
grey = (130,130,130)
yellow =(246,190,0)
brown = (65,25,0)

# font variables
font128 = pygame.font.Font("font/font.ttf",128)
font32 = pygame.font.Font("font/font.ttf",32)

#   Window  setting......
win_width = 1000
win_height = 680
pygame.display.set_caption("Maze Router")
win = pygame.display.set_mode((win_width,win_height))
clock = pygame.time.Clock()
FPS = 60

# Maze...........
side = 40 
goals = [((1,1),(3,7)),((5,5),(8,0)),((4,8),(7,3))]
start = None
goal = None
goal_num = 0
searched_box_ind = 0
route_ind = 0
path = None
route = None

           # 0 1 2 3 4 5 6 7 8 9 10 11
maze = [[0,0,0,0,0,0,0,0,0,0,0,0,0,],#0
              [0,0,1,0,0,0,1,0,0,1,1,0,0],#1
              [0,0,1,1,1,1,1,1,0,0,1,0,0],#2
              [0,0,1,0,0,0,1,0,1,0,1,0,0],#3
              [0,0,0,0,0,0,1,0,0,0,1,0,0],#4
              [0,0,1,1,1,0,0,1,1,0,0,0,1],#5
              [0,0,1,0,1,0,0,0,1,0,0,0,0],#6
              [0,0,1,0,1,0,0,0,0,0,0,0,0],#7
              [0,0,1,1,1,0,0,1,1,0,0,0,0],#8
              [0,1,0,1,0,0,0,0,0,0,0,0,0],#9
              [1,0,1,0,0,0,0,1,0,0,0,0,0],#10
              [0,1,0,0,0,0,0,1,1,0,0,0,1]]#11

def splash():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    color = 255
    while color >= 0:
        clock.tick(FPS)
        text1 = font128.render("Risho's",True,(color,color,color),1)
        text2 = font128.render("Project",True,(color,color,color),1)
        win.blit(text1,(win_width/5,win_height/5))
        win.blit(text2,(win_width/5.5,win_height/2))
        pygame.display.update()
        color-=3.5
        
def drawMaze(side):
    box_wid = win_width/3.5-(side/2)*len(maze[0])
    box_hig = win_height/2-(side/2)*len(maze)
    pygame.draw.rect(win,dark,(box_wid,box_hig,side,side),7)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col]:
                pygame.draw.rect(win,grey,(box_wid+col*side,box_hig+row*side,side,side))
            else:
                pygame.draw.rect(win,greenL,(box_wid+col*side,box_hig+row*side,side,side),7)
    pygame.draw.rect(win,red,(box_wid+start[1]*side,box_hig+start[0]*side,side,side)) ## StartBox coloring
    pygame.draw.rect(win,brown,(box_wid+goal[1]*side,box_hig+goal[0]*side,side,side)) ## GoalBox coloring
    
def info():
    status_text = font32.render("Status : "+status,True,brown)
    steps_text = font32.render("Steps : "+str(path.steps),True,brown)
    calls_text = font32.render("Calls : "+str(path.calls),True,brown)
    win.blit(status_text,(win_width*0.03,win_height*0.05))
    win.blit(steps_text,(win_width*0.6,win_height*0.30))
    win.blit(calls_text,(win_width*0.6,win_height*0.60))
                
def interface(search=False):
    clock.tick(FPS)
    win.fill(white)
    drawMaze(side)
    if search:
        find()
    info()
    pygame.display.update()

    
def find():
    global searched_box_ind, route_ind,status
    box_wid = win_width/3.5-(side/2)*len(maze[0])
    box_hig = win_height/2-(side/2)*len(maze)
    for count, pos in enumerate(path.path_history):
        pygame.draw.rect(win,yellow,(box_wid+pos[1]*side,box_hig+pos[0]*side,side,side),7)
        if count==searched_box_ind:
            break
    if searched_box_ind<len(path.path_history)+1:
        searched_box_ind += 1
    else:
        status = "Path found :)"
        for count, pos in enumerate(route):
            pygame.draw.rect(win,brown,(box_wid+pos[1]*side,box_hig+pos[0]*side,side,side))
            if count==route_ind:
                break
        if route_ind<len(route)+1:
            route_ind += 1

run = True
enter = False
ispath = True
restart = True
splash()

while run:
    if restart: 
        restart = False
        path = FindPath(maze)
        start = goals[goal_num%len(goals)][0]
        goal = goals[goal_num%len(goals)][1]
        route = path.find_path(start,goal)
        if route[0]!=goal:
            ispath = False
            route.clear()
            status = "Can\'t reach the destination Bitch!"
            path.steps = "infinite"
        else:
            status = "Shortest path available :)"
            del route[0]
    if enter and ispath:
        interface(search=True)
        status = "Working on it..."
    else:
        interface()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                side += 1
            if event.key == pygame.K_DOWN:
                side -= 1
            if event.key == pygame.K_RETURN:
                if enter:
                    goal_num += 1
                    searched_box_ind = 0
                    route_ind = 0
                    route.clear()
                    restart = True
                    enter = False
                    ispath  = True
                    continue
                enter = True
                

