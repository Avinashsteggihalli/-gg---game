from time import sleep
import random

bullet_strt = [
    " 1|2|3|4|5|6",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]
bullet_1 = [
    " ◘|2|3|4|5|6",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]
bullet_2 = [
    " 1|◘|3|4|5|6",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]
bullet_3 = [
    " 1|2|◘|4|5|6",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]
bullet_4 = [
    " 1|2|3|◘|5|6",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]
bullet_5 = [
    " 1|2|3|4|◘|6",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]
bullet_6 = [
    " 1|2|3|4|5|◘",
    " ___________",
    "(___________)======|!|}",
    "             (;) \\\ \\\  ",
    "                  \\\ \\\ ",
    "                   \\\ \\\ "
]





lst = [1,2,3,4,5,6]

print("GUN GAme Starting.........")
print("-------------------------------------------------------------------")

for line in bullet_strt:
    print(line)





random.shuffle(lst)
new_lst=lst

while True:
    ans=input("where is the bullet?: ")
    ans=int(ans)
    if (new_lst[ans]) == 1:
        print("you are alive")
        print("the bullet pos was:")
        if ans == 0:
            for line in bullet_1:
                print(line)
        if ans == 1:
            for line in bullet_2:
                print(line)
        if ans == 2:
            for line in bullet_3:
                print(line)
        if ans == 3:
            for line in bullet_4:
                print(line)
        if ans == 4:
            for line in bullet_5:
                print(line)
        if ans == 5:
            for line in bullet_6:
                print(line)
    
    else:
        print("you are dead")
        
        for i in range(len(new_lst)):
            if new_lst[i]==1:
                print(f'it was in {i} position')
                if i == 0:
                    for line in bullet_1:
                        print(line)
                if i == 1:
                    for line in bullet_2:
                        print(line)
                if i == 2:
                    for line in bullet_3:
                        print(line)
                if i == 3:
                    for line in bullet_4:
                        print(line)
                if i == 4:
                    for line in bullet_5:
                        print(line)
                if i == 5:
                    for line in bullet_6:
                        print(line)
            
                
        break
    
       
        
        
