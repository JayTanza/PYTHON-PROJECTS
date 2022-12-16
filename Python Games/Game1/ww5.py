#woodways

import xml.etree.ElementTree as ET
import numpy as np
import time
import keyboard
import pyautogui
    
def read_map(levelname):
    global level_map
    global w
    global h
    for level in root:
        if level.attrib['name'] == levelname:
            w = int(level.attrib['width'])
            h = int(level.attrib['height'])
            for child in level:
                if child.tag == "map":
                    map = child.attrib['content']
    level_map = np.full([w, h], -1)

    k=0
    for j in range(h):
        for i in range (w):
            ch = " "
            while ch not in "0123":
                ch = map[k]
                k += 1
            level_map[i,j] = int(ch)

             
    


def zero_step(levelname):
    solutions.append(ww())
    solutions[0].objects = []
    solutions[0].animals = []
    for level in root:
        if level.attrib['name'] == levelname:
            for child in level:
                if child.tag == "objects":
                    for obj in child:
                        solutions[0].objects.append((obj.tag, int(obj.attrib["x"]), int(obj.attrib["y"])))
                if child.tag == "animals":
                    for obj in child:
                        solutions[0].animals.append((obj.tag, int(obj.attrib["x"]), int(obj.attrib["y"])))
    solutions[0].do_hash()



def do_move(prev, move):
    def has_wood(obj, x, y):
        for tile in obj:
            if tile[0]=="wood" and tile[1] == x and tile[2]==y:
                return True
        return False
    def crash_wood(obj, x, y):
        for i in range(len(obj))[::-1]:
            if obj[i][0]=="wood" and obj[i][1] == x and obj[i][2]==y:
                del obj[i]
    def on_exit(new_objects, animal):
        for obj in new_objects:
            if obj[0]=="exit" and obj[1]==animal[1] and obj[2]==animal[2]:
                return True
        return False
    def has_portal(obj, x, y):
        for tile in obj:
            if tile[0]=="portal" and tile[1] == x and tile[2]==y:
                return True
        return False
    def other_portal(obj, x, y):
        for tile in obj:
            if tile[0]=="portal" and (tile[1] != x or tile[2] != y):
                return (tile[1], tile[2])
        return False
    

    global drawn
    global collapse
    global duplicates

    show_steps = False
    
    new_move =  prev.moves + move  
    #print (new_move)
    dx = 0
    dy = 0
    if move == "U":
        dy = -1
    if move == "R":
        dx = 1
    if move == "D":
        dy = 1
    if move == "L":
        dx = -1
        
    new_animals = prev.animals.copy()
    new_objects = prev.objects.copy()
    teleported = 0 # count of teleportts
    for i in range(len(new_animals)):

        # new coord aftter the move
        curr_x = new_animals[i][1]
        curr_y = new_animals[i][2]
        new_x = new_animals[i][1]+dx
        new_y = new_animals[i][2]+dy


        #print (new_animals[i], "to", new_x, new_y)
        
        # move if it is a legal move
        if 0<new_x<w+1 and 0<new_y<h+1 and level_map[new_x-1][new_y-1] != 2:
            new_animals[i] = new_animals[i][0], new_x, new_y
        else:
            continue # no movement for this one

        # slide on ice
        while 0<new_x<w+1 and 0<new_y<h+1 and level_map[new_x-1][new_y-1] == 3:
            new_x = new_x+dx
            new_y = new_y+dy
            if 0<new_x<w+1 and 0<new_y<h+1 and level_map[new_x-1][new_y-1] != 2:
                new_animals[i] = new_animals[i][0], new_x, new_y

        # if teleporter - teleport
        if has_portal(new_objects, new_x, new_y):
            new_x, new_y = other_portal(new_objects, new_x, new_y)
            new_animals[i] = new_animals[i][0], new_x, new_y
            teleported += 1 
            
            
        # if fox goes off wood - wood disapears
        if new_animals[i][0]=="fox" and has_wood(new_objects, curr_x, curr_y):
            crash_wood (new_objects, curr_x, curr_y)
            
    # if water - drown
    for i in range(len(new_animals)):
        if level_map[new_animals[i][1]-1][new_animals[i][2]-1] == 0 and \
           (( new_animals[i][0]=="buffalo") or (new_animals[i][0]=="fox" and not has_wood(new_objects, new_animals[i][1], new_animals[i][2]))):
            if show_steps:
                print (new_move + " drown")
            drawn += 1
            return "drown"

    # check for collapses
    for i in range(len(new_animals)):
        for j in range(len(new_animals)):
            if i!=j and new_animals[i][1] == new_animals[j][1] and new_animals[i][2] == new_animals[j][2]:
                if show_steps:
                    print (new_move + " collapse")
                collapse += 1
                return "collapse"

    # count animals on portals
    on_portals = 0
    for animal in new_animals:
        if has_portal(new_objects, animal[1], animal[2]):
            on_portals += 1
    # collapse on stepping into portal
    if on_portals==2 and teleported == 1:
        if show_steps:
            print (new_move + " collapse")
        collapse += 1
        return "collapse"        

    # check if solution is found
    for animal in new_animals:
        if not on_exit(new_objects, animal):
            break
    else:
        if show_steps:
            print (new_move + " solved!")
        return new_move

    #dedup
    new_hash = hash((str(new_objects)+(str(new_animals))))
    for solution in solutions:
        if solution.hashed == new_hash:
                if show_steps:
                    print (new_move + " duplicate")
                duplicates += 1
                return "duplicate"
            
    # new etrance in solutions
    if show_steps:
        print (new_move + " ok")
    #print (new_objects)
    #print (new_animals)
    solutions.append(ww())
    solutions[-1].moves = new_move
    solutions[-1].animals = new_animals
    solutions[-1].objects = new_objects
    solutions[-1].do_hash()


        


def step(n):
    for solution in solutions:
        if len(solution.moves)==n-1:
            for next_move in ["U", "R", "D", "L"]:
                move_res = do_move(solution, next_move)
                if move_res != None and move_res != "drown"  and move_res != "collapse" and move_res != "duplicate":
                    return move_res

class ww:
    moves=""
    objects=[]
    animals=[]
    hashed = 0 # to hash obj_animals

    def do_hash(self):
        self.hashed = hash((str(self.objects)+(str(self.animals))))
    

    
    


level_map = np.full([5, 5], -1)
solutions = []
w = 0
h = 0

xml = ET.parse('levels.xml')
root = xml.getroot()

drawn = 0
collapse = 0
duplicates = 0


def do_puzzle(levelname):
    global level_map
    global solutions
    global drawn
    global collapse
    global duplicates
    drawn = 0
    collapse = 0
    duplicates = 0
    t = time.time()    
    solutions.clear()

    level_map = np.full([5, 5], -1)
##    print ("="*40)
##    print ("Level: ", levelname)
    read_map(levelname)
    #print (level_map.transpose())
        
    zero_step(levelname)
    #print (solutions[0].objects)
    #print (solutions[0].animals)

    j=1 # step counter
    result = None    
    while result == None and j <40:
        result = step(j)
        j+=1
##        print ("*", end='')
        
    print ("")
    print ("It took {} steps, {} drawn, {} collapsed, {} duplicates, {} valid".format\
           (j-1, drawn, collapse, duplicates, len(solutions)))
    print ("Solution is: ", result)
    print ("Time: ", time.time()-t)
    print ("Level:", levelname, "Solution:", result)
    return result

for i in range (1, 57):
    levelname = "{:02}".format(i)
    do_puzzle(levelname)
    
##do_puzzle("56")

def color_distance(sample, standard):
    sum=0
    for i in range (3):
        sum += (sample[i]-standard[i])**2
    return sum

# is the movement over
def no_difference(was, now):
    w = was.load()
    n = now.load()
    diff = 0
    for i in range(0, was.size[0], 50):
        for j in range(0, was.size[1], 50):
            diff += color_distance(w[i,j], n[i,j])
    #print (diff)
    if diff > 10000:
        return False
    return True

def do_movement(solution):
    for move in solution:
        now = pyautogui.screenshot()
        for i in range(10):
            #print (i)
            was = now
            time.sleep(0.01)
            now = pyautogui.screenshot()
            if no_difference(was, now):
                break
        if move =="U":
            keyboard.send('up')
        if move =="D":
            keyboard.send('down')
        if move =="L":
            keyboard.send('left')
        if move =="R":
            keyboard.send('right')

            


k=''
wait_number1 = ''
wait_number2 = ''
while k!='esc':
    k = keyboard.read_key()
    time.sleep(0.2)
    if k in "1234567890":
        if k in "012345" and wait_number1 == '' and wait_number2 == '':
            wait_number1 = k
##            print ("first", k)            
        elif k in "0123456789" and wait_number1 != '' and wait_number2 == '':
            wait_number2 = k
##            print ("second", k)            
    else:
        wait_number1 = ''
        wait_number2 = ''
##        print("reset")
    if wait_number1 != '' and wait_number2 != '':
        print (wait_number1, wait_number2)
        solution = do_puzzle(str(wait_number1)+str(wait_number2))
        print (solution)
        do_movement(solution)
        wait_number1 = ''
        wait_number2 = ''    
