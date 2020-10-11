from tqdm.auto import tqdm
from time import sleep
from os import system, name
import sys
import keyboard


#these functions are created for design purpose
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def load():
    print("\n"*2)
    print(" "*4,"LOADING.....")
    print()
    for i in tqdm(range(80)):
        print("", end="\r")
        sleep(0.025)
def drawline():
    print("_"*168)


#home is the main screen of application
def home():
    clear()
    drawline()
    print()
    drawline()
    print("\n"*5)
    print(" "*74,"WELCOME")
    print()
    print(" "*77,"TO")
    print()
    print(" "*70,"DISK SCHEDULER")
    print()
    print(" "*50,"(AN          OPERATING          SYSTEM          PROJECT)" )
    print("\n"*5)
    drawline()
    print()
    drawline()
    print()
    print("     type 'start() to start the application in prompt below")
    print()
    x=input("     >>>>")
    if(x=="start()"):
        print()
        load()
        menu()
    else:
        print("     INVALID COMMAND")
        home()


L,U=int(),int()
#menu takes care of initialization of sequence and initial head and choosing algo
def menu():
    sequence=list()
    clear()
    drawline()
    print()
    drawline()
    print()
    print("     the following process will initialize values")
    print("     1.sequence of requests.")
    print("     2.initial head position.")
    print("     type 'initialize()' in prompt to continue ")
    print()
    c=input("     >>>>")
    if c=='initialize()':
        load()
        clear()
        drawline()
        print()
        drawline()
        print()
        print("     type 'exit()' to exit in sequence prompt")
        print("     Enter request sequence:")
        while True:
            print()
            value=input("     >>>>")
            if value=="exit()":
                break
            try:
                sequence.append(int(value))
            except:
                pass
        while len(sequence)==0:
            print("     there are no track request.type '/a' to do it again")
            a=input("     >>>>")
            if a == "/a":
                menu()
            else:
                print("     INVALID COMMAND")

        print("     Sequence entered.......")
        ipos=int(input("     Enter initial head position:"))
        print("     head position entered....")
        global L
        L=int(input("     Enter Lower Track position:"))
        print("     lower track position entered....")
        global U
        U=int(input("     Enter Upper Track position:"))
        print("     upper track position entered....")
        drawline()
        print()
        drawline()
        print()
        amenu(sequence,ipos)
    else:
        print("     INVALID COMMAND")
        menu()


#amenu takes care of choosing disk scheduling algorithm
def amenu(sequence,ipos):
    load()
    clear()
    drawline()
    print()
    drawline()
    print()
    print("     Type the following command for following algorithm :")
    print()
    print("     1.First come first serve       ->   'cd fcfs'")
    print("     2.Shortest seek time first     ->   'cd sstf'")
    print("     3.Elevator algorithm(SCAN)     ->   'cd scan'")
    print("     4.Look algorithm               ->   'cd look'")
    print("     5.C-Scan  algorithm            ->   'cd cscan'")
    print("     6.C-Look  algorithm            ->   'cd clook'")
    print()
    print("     type your command:")
    command=input("     >>>>")
    print()
    if command=="cd fcfs":
        fcfs(sequence,ipos)
    elif command=="cd sstf":
        sstf(sequence,ipos)
    elif command=="cd scan":
        scan(sequence,ipos)
    elif command=="cd look":
        look(sequence,ipos)
    elif command=="cd cscan":
        cscan(sequence,ipos)
    elif command=="cd clook":
        clook(sequence,ipos)
    else:
        print("     INVALID COMMAND")
        amenu(sequence,ipos)
    drawline()
    print()
    drawline()
    navigate(sequence,ipos)


def navigate(sequence,ipos):
    print("     IF WANTED TO CHECK OTHER METHODS type 'cd algomethods' \n     type 'close()' to exit application")
    q=input("     >>>>")
    if( q=="cd algomethods"):
        amenu(sequence,ipos)
    elif (q=="close()"):
        clear()       
        sys.exit(0)
    else:
        print("     Wrong command")
        navigate(sequence,ipos)

#these function are disk scheduling algorithms
def fcfs(sequence,head):
    seek_count = 0;
    distance, cur_track = 0, 0;
    for i in sequence:
        cur_track = i;
        # calculate absolute distance
        distance = abs(cur_track - head);
        # increase the total count
        seek_count += distance;
        # accessed track is now new head
        head = cur_track;
    print("     Seek Sequence is");
    print("     >>>>>",end="  ")
    for i in sequence:
        print(i,end="--->");
    print()

    print("     Total number of seek operations = ",seek_count);
    print()


def sstf(sequence,head):
    sequence1=sequence.copy()
    pos=head
    mov=0
    print("     Seek Sequence is");
    print("     >>>>>",end="  ")
    while sequence1:
        closest=abs(pos-sequence1[0])
        index=0
        for j in range(1,len(sequence1)):
            if(abs(pos-sequence1[j])<closest):
                closest=abs(pos-sequence1[j])
                index=j
        mov+=abs(pos-sequence1[index])
        pos=sequence1[index]
        print(pos,end="--->")
        sequence1.remove(pos)
    print("     Total number of seek operations = ",mov);
    print()



def scan(sequence,head):
    print("     Enter Direction:")
    direction=input("     >>>>")
    sequence1=sequence.copy()
    pos=head
    mov=0
    print("     Seek Sequence is");
    print("     >>>>>",end="  ")
    while sequence1:
        if pos in sequence1:
            print(pos,end="--->")
            sequence1.remove(pos)
            if not sequence1:
                break
        if direction=="left" and pos> L:
            pos-=1
        if direction=="right"and pos<= U:
            pos+=1
        mov+=1
        if pos == 0:
            direction="right"
        if pos==U:
            direction="left"
    print("     Total number of seek operations = ",mov);
    print()


#
def cscan(sequence,head):
    print("     Enter Direction:")
    direction=input("     >>>>")
    sequence1=sequence.copy()
    pos=head
    mov=0
    print("     Seek Sequence is");
    print("     >>>>>",end="  ")
    while sequence1:
        if direction=="right":
            if pos in sequence1:
                print(pos,end="--->")
                sequence1.remove(pos)
                if not sequence1:
                    break
            mov+=1
            pos+=1
            if pos == U:
                pos=0
                mov+=U
        if direction=="left":
            if pos in sequence1:
                print(pos,end="--->")
                sequence1.remove(pos)
                if not sequence1:
                    break
            pos-=1
            mov+=1
            if pos == 0:
                pos=U
                mov+=U
    print("     Total number of seek operations = ",mov);
    print()



def look(sequence,head):
    print("     Enter Direction:")
    direction=input("     >>>>")
    sequence1=sequence.copy()
    pos=head
    mov=0
    print("     Seek Sequence is");
    print("     >>>>>",end="  ")
    while sequence1:
        if pos in sequence1:
            print(pos,end="--->")
            sequence1.remove(pos)
            if not sequence1:
                break
        if direction=="left" and pos> L:
            pos-=1
        if direction=="right"and pos< U:
            pos+=1
        mov+=1
        if pos == min(sequence):
            direction="right"
        if pos==max(sequence):
            direction="left"
    print("     Total number of seek operations = ",mov);
    print()


def clook(sequence,head):
    print("     Enter Direction:")
    direction=input("     >>>>")
    sequence1=sequence.copy()
    pos=head
    mov=0
    print("     Seek Sequence is");
    print("     >>>>>",end="  ")
    while sequence1:
        if direction=="right":
            if pos in sequence1:
                print(pos,end="--->")
                sequence1.remove(pos)
                if not sequence1:
                    break
            mov+=1
            pos+=1
            if pos == max(sequence)+1:
                pos=min(sequence)
                mov+=(abs(max(sequence)-min(sequence))-1)
        if direction=="left":
            if pos in sequence1:
                print(pos,end="--->")
                sequence1.remove(pos)
                if not sequence1:
                    break
            pos-=1
            mov+=1
            if pos == min(sequence)-1:
                pos=max(sequence)
                mov+=(abs(max(sequence)-min(sequence))-1)
    print("     Total number of seek operations = ",mov);
    print()


home()
