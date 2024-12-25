# Libraries
import time

# The disclaimer
print('==========================================================================================================================================================================================\n')
print('DISCLAIMER!!!!!\n')
print('All opinions on wether you should as your crush out are NOT mine and opinions of a Youtuber by the name of Crystal.\n')
print('Don\'t take her advice/guidance seriously (but I would recommend as her advice on things are really helpful!) \n')
print('Hope it works well for you and your crush if you actually decide to ask her out, but like I said, that\'s on you. \n')
# Credits
print('Credits: \n')
print('Made by: Paraliyzed_evo \n')
print('Crystal\'s Youtube Channel: https://www.youtube.com/@888_crystal \n')
print('Crystal\'s Youtube Video of where I got the idea from: https://www.youtube.com/watch?v=hpwyjcd3Ioc \n')
print('Source code: https://github.com/ParaliyzedEvo/Simulation \n')
print('Website: https://paraliyzed.net \n')
print('==========================================================================================================================================================================================\n')

print('Should you tell your crush you like them? \n')

# Future me who is currently writing this code, past me who is starting this code out will not be writing any comments regarding the code below me because idk what to put, just read the inputs
# For anyone else, good luck
while True:
    question = input('Is your crush seeing someone? (Put idk for idk) \n\n').lower()
    match question:
        case 'idk':
            print('\nFind out \n')
            time.sleep(3)
            exit()
        case 'no': 
            while True:
                question = input ('\nHow do you know your crush? (Online or in person?) \n\n').lower()
                match question:
                    case 'online':
                        print('\nplaceholder')
                    case 'in person':
                        while True:
                            question = input('\nHow did you meet your crush? (Friends, school, work, other) \n\n').lower()
                            match question:
                                case 'friends':
                                    question = input('\nAre you friends with your crush (1) or did you meet via friends (2)? \n\n')
                                    match question:
                                        case '1':
                                            while True:
                                                question = input('\nAre you in a friend group with them? \n\n').lower()
                                                match question:
                                                    case 'yes':
                                                        while True:
                                                            question = input('\nWas your crush ever seeing someone else in your friend group? \n\n').lower()
                                                            match question:
                                                                case 'yes':
                                                                    while True:
                                                                        question = input('\nWas your crush casually hooking up with someone in your friend group (1) or was your crush dating someone else in the friend group (2)? \n\n').lower()
                                                                        match question:
                                                                            case '1':
                                                                                print('\nplaceholder')
                                                                            case '2':
                                                                                while True:
                                                                                    question = int(input('\nHow serious was it on a scale of 1-5? (Put 0 to see what the number on the scale means) \n\n'))
                                                                                    match question:
                                                                                        case n if n in range(1,3):
                                                                                            print('\nYeaaah do it, as long as your ok with the fact that getting together with your crush and/or potentially breaking up with them may/will change the dynamic of the friend group forever/breaking the friend group entirely. \n')
                                                                                            time.sleep(3)
                                                                                            exit()
                                                                                        case n if n in range(3, 6):
                                                                                            print('\nIs it fucked up for you to ask out your friend\'s ex? \n')
                                                                                            print('\nWe\'ll find out using Cady\'s law (you can put decimals) \n')
                                                                                            # Providing inputs for calculating if it's fucked up to ask out your crush who your dated dated prior to you liking them using Cady's law (prolly my only comment in this code bunch)
                                                                                            while True:
                                                                                                d = float(input('\nHow long (in months) as your crush dated your friend? \n\n'))
                                                                                                if d <= 0:
                                                                                                    print('\nPlease put a number greater than 0. \n')
                                                                                                    continue
                                                                                                else:
                                                                                                    break
                                                                                            while True:
                                                                                                f = float(input('\nHow close are you to your friend on a scale of 1-10 \n\n'))
                                                                                                if f <= 0 or f > 10:
                                                                                                    print('\nPlease put a number between 1-10. \n\n')
                                                                                                    continue
                                                                                                else:
                                                                                                    break
                                                                                            while True:
                                                                                                g = float(input('\nHow long (in months) was it since they broke up and you starting to like your crush? \n\n'))
                                                                                                if g <= 0:
                                                                                                    print('\nPlease put a number greater than 0. \n')
                                                                                                    continue
                                                                                                else:
                                                                                                    break
                                                                                                #Doing the calculations
                                                                                            t = (d*f)/g
                                                                                            if g < 2:
                                                                                                print(f'\nBro really, only {g} months since they broke up? Don\'t even think about it. \n')
                                                                                                time.sleep(3)
                                                                                                exit()
                                                                                            elif t > g:
                                                                                                print(f'\n{g} months you say? Well your cutting it close, wait it out. \n')
                                                                                                time.sleep(3)
                                                                                                exit()
                                                                                            elif t <= g:
                                                                                                while True:
                                                                                                    question = input('\nDo either of them still have feelings for each other? \n\n').lower()
                                                                                                    match question:
                                                                                                        case n if 'yes' or 'idk':
                                                                                                            break
                                                                                                        case 'no':
                                                                                                            while True:
                                                                                                                question = input('\nAre you sure? \n\n').lower()
                                                                                                                match question:
                                                                                                                        case 'yes':
                                                                                                                            goto line 62
                                                                                                                        case 'no':
                                                                                                                            goto line 121
                                                                                                                        case _:
                                                                                                                            print('\nPlease put either \'yes\' or \'no\' as your answer. \n')
                                                                                                                            continue
                                                                                                        case _:
                                                                                                            print('\nPlease put either \'yes\', \'no\', or \'idk\' as your answer. \n')
                                                                                                            continue
                                                                                            while True:
                                                                                                question = input('\nDoes the potential of getting together with your crush and/or potentially breaking up with them outweight the risk of potentially changing the dynamic of the friend group forever? \n\n')
                                                                                                match question:
                                                                                                    case 'yes':
                                                                                                        print('\nTell them. \n')
                                                                                                        time.sleep(3)
                                                                                                        exit()
                                                                                                    case 'no':
                                                                                                        print('\nDon\'t tell them. \n')
                                                                                                        time.sleep(3)
                                                                                                        exit()
                                                                                                    case _:
                                                                                                        print('\nPlease put either \'yes\' or \'no\' as your answer. \n')
                                                                                                        continue

                                                                                        case n if n == 0:
                                                                                            print('\n1-2: They went on one bad date and are not attracted to each other at all. \n')
                                                                                            print('\n3: They dated for a couple weeks and it didn\'t get serious. \n')
                                                                                            print('\n4-5: They dated very seriously; they met each others parents; their relationship lasted over three months; they maybe have a kid and/or pet together; they talked about their future plans together. \n')
                                                                                            continue
                                                                                        case _:
                                                                                            print('\nPlease put a number between 1-5. \n')
                                                                                            continue
                                                                            case _:
                                                                                print('\nPlease put either 1 or 2 as your answer. \n')
                                                                                continue
                                                                case 'no':
                                                                    print('\nplaceholder')
                                                                case _: 
                                                                    print('\nPlease put either \'yes\' or \'no\' as your answer. \n')
                                                                    continue
                                                    case 'no':
                                                        print('\nTell them, but be mentally prepared. \n')
                                                        time.sleep(3)
                                                        exit()
                                                    case _:
                                                        print('\nPlease put either \'yes\' or \'no\' as your answer. \n')
                                                        continue
                                        case '2':
                                            print('\nplaceholder')
                                        case _: 
                                            print('\nPlease put either 1 or 2 as your answer. \n')
                                            continue
                                case 'school':
                                    print('\nplaceholder')
                                case 'work': 
                                    print('\nplaceholder')
                                case 'other':
                                    print('\nplaceholder')
                                case _:
                                    print('\nPlease put either \'friends\',  \'school\', \'work\', or \'other\'as your answer. \n')
                                    continue
                    case _:
                        print('\nPlease put either \'online\' or \'in person\' as your answer. \n')
                        continue
        case 'yes':
            print('\nCooked, move on. Why where you liking them in the first place? \n')
            time.sleep(3)
            exit()
        case _:
            print('\nPlease put either \'yes\', \'no\', or \'idk\' as your answer. \n')
            continue