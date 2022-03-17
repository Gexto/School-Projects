#!/usr/bin/env python3

'''Vacumm02.py Gerardo Torres 4 Feb 2022 '''

import random

#----------------------------------------------------------------
def createCarpet (mySize=10, maxDirty=10) :
    '''return a list of length mySize containing random ints from
    zero to MaxDirty'''
    retVal = list ()
    for i in range (0, mySize) :
        retVal.append(random.randint(1, maxDirty))
    return retVal

#----------------------------------------------------------------
def randomStartPosition(myCarpet) :
    '''return a random position on the carpet, in 0...
       (len(carpet)-1)'''
    return random.randint(0, len(myCarpet)-1)

#----------------------------------------------------------------
def reportCarpet(myCarpet, myPosition=None) :
    '''Print the carpet and mark the position of the vacuum robot
       with an asterisk if one is specified'''

    print('+'+'+----'*len(myCarpet)+'++')

    print('|', end='')
    for i in range(0, len(myCarpet)) :
        if (i == myPosition) :
            print(F"|*{myCarpet[i]:^3}", end='')
        else :
             print(F"|{myCarpet[i]:^4}", end='')
    print('||')
    print('+'+'+----'*len(myCarpet)+'++')

#----------------------------------------------------------------
def canGoRight(myCarpet, myPosition) :
    '''return True if an agent atmyPosition can go right and
       still remain on the carpet (as long as not in the last
       cell'''
    return myPosition < (len(myCarpet)-1)

#----------------------------------------------------------------
def canGoLeft(myCarpet, myPosition) :
    '''return True if an agent at myPosition can go left and
       still remain on the carpet (as long as not in the first
       cell'''
    return myPosition > 0

#----------------------------------------------------------------
def isDirty(myCarpet, myPosition) :
    '''return True if myCarpet is dirty at myPosition'''
    return myCarpet[myPosition] > 0

#----------------------------------------------------------------
def goRight(myCarpet, myPosition) :
    '''return the new location for the agent if it moves right,
       so it never goes off the carpet'''
    return min((myPosition+1),(len(myCarpet)-1))

#----------------------------------------------------------------
def goLeft(myCarpet, myPosition) :
    '''return the new location for the agent if it moves left,
        so it never goes off the carpet'''
    return max(0,myPosition-1)

#----------------------------------------------------------------
def clean(myCarpet,myPosition) :
    '''Clean the cell at myPosition on myCarpet, decrimenting 
       the value by one. max guarantess it never goes to 0'''
    myCarpet[myPosition] = max(myCarpet[myPosition]-1,0)
    

#----------------------------------------------------------------
def runVacuum(myCarpet, myPosition) :
    START = 0
    GOINGRIGHT = 1 
    GOINGLEFT = 2
    CLEANING = 3
    PARKING = 4
    DONE = 5
    stateText = ['START', 'GOINGRIGHT', 'GOINGLEFT', 'CLEANING','PARKING', 'DONE']
    position = myPosition
    time = 0
    state = START

    while(state != DONE) and (time < 200) :
        print('Time:', time, 'Position:', position, 'State:', stateText[state])
        reportCarpet(myCarpet, position)
        print()

        if state == START :
            if canGoRight(myCarpet, position) :
                state = GOINGRIGHT
            else :
                state = CLEANING

        elif state == GOINGRIGHT :
            #see if it can keep going right
            position = goRight(myCarpet, position)
            if not canGoRight(myCarpet, position) :
                state = CLEANING

        elif state == GOINGLEFT :
            position = goLeft(myCarpet, position)
            state = CLEANING

        elif state == CLEANING :
            if isDirty(myCarpet, position) :
                clean(myCarpet, position)
            #If not dirty, go left
            elif canGoLeft(myCarpet, position) :
                state = GOINGLEFT
            else :
                #Not dirty or can't go left then park
                state = PARKING
                    
        elif state == PARKING :
            state = DONE
        else :
            print('ERROR: INVALID STATE')
            state = DONE

        time = time + 1
#----------------------------------------------------------------
#MAIN PROGRAM
#----------------------------------------------------------------

if __name__ == '__main__' :
    carpet = createCarpet()
    vacuumPosition = randomStartPosition(carpet)
    runVacuum(carpet, vacuumPosition)
#----------------------------------------------------------------
