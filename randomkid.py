### randomkid.py ###

import random

def randompick (kids):
    pick = random.choice(kids)
    return pick

def recordpick (pick):
    outFile = open('randompick_record.txt', 'a')
    outFile.write(pick)
    outFile.write('\n')
    outFile.close()
    
def pickhistory ():
    inFile = open('randompick_record.txt')
    hist = inFile.read()
    inFile.close()
    return hist

def stats_run ():
    inFile = open('randompick_record.txt')
    history = inFile.read()
    Nathan_count = history.count('Nathan')
    Zachary_count = history.count('Zachary')
    print ("Nathan: ", Nathan_count, "\nZachary: ", Zachary_count)
    inFile.close()

def main ():
    kids = ['Nathan', 'Zachary']
    menu_select = input("(P)ick a kid\n(H)istory\n(S)tats\n")
    if menu_select == 'p' or menu_select == 'P':
        pick = randompick (kids)
        print (pick)
        print ()
        recordpick (pick)
        main ()
    if menu_select == 'h' or menu_select == 'H':
        hist = pickhistory ()
        print (hist)
        print ()
        main ()
    if menu_select == 's' or menu_select == "S":
        stats_run ()
        print ()
        main ()
        
#    if menu_select == 'e' or menu_select == 'E':

main ()