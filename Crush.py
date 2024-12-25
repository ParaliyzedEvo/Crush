# Libraries
import time

# The disclaimer
print('================================================================================================================================================================================================================================================\n')
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
print('================================================================================================================================================================================================================================================\n')

print('Should you tell your crush you like them? \n')

# Future me who is currently writing this code, past me who is starting this code out will not be writing any comments regarding the code below me because idk what to put, just read the inputs
# For anyone else, good luck
# Edit 1 (before the intial commit): Ok so turns out using match cases fucking sucked ass, so I asked chatgpt to help me out with this and told me on how to restructure my code, so here it is. 

def ask_question(prompt, options=None):
    """Ask a question and return the user's response."""
    while True:
        response = input(prompt).strip().lower()
        if not options or response in options:
            return response
        print(f"\nPlease choose from the following: {', '.join(options)}\n")

def end():
    time.sleep(3)
    exit()

def no():
    print('\nDon\'t tell them. \n')
    end()

def no2():
    print('\nDon\'t tell them because it\'s going to run the purpose they serve in your life rn. \n')
    end()

def yes():
    print('\nTell them. \n')
    end()

def idfk():
    question = ask_question('\nDoes the potential of getting together with your crush and/or potentially breaking up with them outweight the risk of potentially changing the dynamic of the friend group forever? \n\n', ['yes', 'no'])
    if question == 'no':
        no()
    elif question == 'yes':
        yes()

def idk():
    print('\nYeaaah do it, as long as your ok with the fact that getting together with your crush and/or potentially breaking up with them may/will change the dynamic of the friend group forever/breaking the friend group entirely. \n')
    end()

def idek():
    print('\nI meaannnn I wouldn\'t tbh... \n')
    end()

def calculate_cady_law():
    print('\nIs it fucked up for you to ask out your friend\'s ex? \n')
    print("\nWe'll find out using Cady's law (you can put decimals) \n")

    while True:
        d = float(input('\nHow long (in months) has your crush dated your friend? \n\n'))
        if d > 0:
            break
        print('\nPlease put a number greater than 0. \n')

    while True:
        f = float(input('\nHow close are you to your friend on a scale of 1-10 \n\n'))
        if 0 < f <= 10:
            break
        print('\nPlease put a number between 1-10. \n\n')

    while True:
        g = float(input('\nHow long (in months) was it since they broke up and you started to like your crush? \n\n'))
        if g > 0:
            break
        print('\nPlease put a number greater than 0. \n')

    t = (d * f) / g

    if g < 2:
        print(f"\nBro really, only {g} months since they broke up? Don't even think about it. \n")
        end()
    elif t > g:
        print(f"\n{g} months you say? Well, you're cutting it close. Wait it out. \n")
        end()
    elif t <= g:
        while True:
            response = ask_question('\nDo either of them still have feelings for each other? \n\n', ['yes', 'no', 'idk'])
            if response in ['yes', 'idk']:
                idfk()
            elif response == 'no':
                sure = ask_question('\nAre you sure? \n\n', ['yes', 'no'])
                if sure == 'yes':
                    idk()
                elif sure == 'no':
                    idfk()

def idrk():
    in_group = ask_question('\nAre you in a friend group with them? \n\n', ['yes', 'no'])
    if in_group == 'yes':
        dated_in_group = ask_question('\nWas your crush ever seeing someone else in your friend group? \n\n', ['yes', 'no'])
        if dated_in_group == 'yes':
            question = ask_question('\nWas your crush casually hooking up with someone in your friend group (1) or was your crush dating someone else in the friend group? (2) \n\n',['1','2'])
            if question == '1':
                idk()
            elif question == '2':
                while True:
                    serious_level = int(input('\nHow serious was it on a scale of 1-5? (Put 0 to see what the number on the scale means) \n\n'))
                    match serious_level:
                        case n if n in range(1, 3):
                            idk()
                            break
                        case n if n in range(3, 6):
                            calculate_cady_law()
                            break
                        case 0:
                            print('\n1-2: They went on one bad date and are not attracted to each other at all. \n')
                            print('\n3: They dated for a couple weeks and it didn\'t get serious. \n')
                            print('\n4-5: They dated very seriously; they met each others parents; their relationship lasted over three months; they maybe have a kid and/or pet together; they talked about their future plans together. \n')
                            continue
                        case _:
                            print('\nPlease put a number between 1-5. \n')
                            continue
        elif dated_in_group == 'no':
            friend_likes_your_crush = ask_question('\nDoes anyone else in your friend group like your crush? \n\n',['yes','no'])
            if friend_likes_your_crush == 'yes':
                chance = ask_question('\nIs there any chance your crush could like you back? \n\n',['yes','no'])
                if chance == 'no':                                               
                    idek()
                if chance == 'yes':
                    idfk()
                elif friend_likes_your_crush == 'no':
                    idek()
    elif in_group == 'no':
        print('\nTell them, but be mentally prepared. \n')
        end()

def i_ran_out_of_name_ideas_lol():
    mutiple = ask_question('\nSame person (1) or multiple people? (2) \n\n',['1','2'])
    if mutiple == '2':
        print('\nTell them, but it depends what you want out of this. \n')
        end()
    if mutiple == '1':
        print('\nOk they\'re in a situationship')
        role = ask_question('\nWhat\'s their role in the situationship? (They\'re in a situationship and they\'re being dragged along by the person who won\'t commit (1) or they\'re in a situationship and they\'re the one who won\'t commit and is dragging the other person along (2).) \n\n',['1','2'])
        if role == '2':
            print('\nYou should tell your crush you like them, but it\'s likely they\'ll be too blinded by that other person to reciprocate your feelings. \n')
            end()
        if role == '1':
            print('\nDon\'t tell them unless you also want to be in a situationship. \n')
            end()

def irdk():
    do_you_like_them = ask_question('\nDo you actually like them (1) or do you only have a crush on them because you\'re in a forced proximity with them? (2) \n\n',['1','2'])
    if do_you_like_them == '2':
        no2()
    elif do_you_like_them == '1':
        you_sure = ask_question('\nYour saying you would have a crush on this person even if you didn\'t see them everyday? \n\n',['yes','no'])
        if you_sure == 'no':
            no2()
        elif you_sure == 'yes':
            print('\nTell them (either the best relationship of yoru life and you\'ll be married or make things incredibly awkward and uncomfortable for yourself everyday when you\'re forced to see them. \n')
            end()

def main():
    while True:
        question = ask_question('Is your crush seeing someone? (Put idk for idk) \n\n', ['yes', 'no', 'idk'])
        match question:
            case 'idk':
                print('\nFind out. \n')
                end()
            case 'yes':
                define_seeing = ask_question('Are they casually dating someone (1) or are they in a relationship together (2) or are they hooking up with someone? (3) \n\n',['1','2','3'])
                if define_seeing == '3':
                    i_ran_out_of_name_ideas_lol()
                elif define_seeing == '2':
                    no()
                elif define_seeing == '1':
                    casual = ask_question('\nIs it actually casual? \n\n',['yes','no'])
                    if casual == 'no':
                        no()
                    elif casual == 'yes':
                        i_ran_out_of_name_ideas_lol()
            case 'no':
                question = ask_question('\nHow do you know your crush? (Online or in person?) \n\n', ['online', 'in person'])
                if question == 'online':
                    celebrity = ask_question('\nAre they a celebrity? \n\n',['yes','no'])
                    if celebrity == 'yes':
                        print('\nYou can tell them, but they\'re never gonna know about it. \n')
                        end()
                    elif celebrity == 'no':
                        dating_app = ask_question('\nDid you meet this person on a dating app? \n\n',['yes','no'])
                        if dating_app == 'yes':
                            print('\nYea, you should tell them, but I already assume they already know you like them (assuming you matched). \n')
                        elif dating_app == 'no':
                            rl = ask_question('\nHave you ever met in real life? \n\n',['yes','no'])
                            if rl == 'yes':
                                yes()
                            elif rl == 'no':
                                print('\nYou can tell them, but there\'s a chance you won\'t be attracted to them irl. \n')
                                end()
                elif question == 'in person':
                    question = ask_question('\nHow did you meet your crush? (Friends, school, work, other) \n\n', ['friends', 'school', 'work', 'other'])
                    match question:
                        case 'friends':
                            response = ask_question('\nAre you friends with your crush (1) or did you meet via friends? (2) \n\n', ['1', '2'])
                            if response == '1':
                                idrk()
                            elif response == '2':
                                crush_and_friend = ask_question('\nDo you and your crush have a mutual friend (1) or your crush is related to your friend? (2) \n\n',['1','2'])
                                if crush_and_friend == '1':
                                    idrk()
                                elif crush_and_friend == '2':
                                    sibling = ask_question('\nAre they your friend\'s sibling? \n\n')
                                    if sibling == 'yes':
                                        print('\nOh my god. \n')
                                        are_you_sure = ask_question('Do you think you like them just because they\'re your friend\'s sibling? \n\n')
                                        if are_you_sure == 'yes':
                                            print('\nFor the love of god, don\'t tell them, like that\'s actually wildddddddddddd. \n')
                                            end()
                                        elif are_you_sure == 'no':
                                            why_are_you_going_down_this_path_anyway = ask_question('\nDoes the prospect of being with your crush outweight the fact that you may ruin/make awkward (at least for a time) your relationship with your friend? \n\n',['yes','no'])
                                            if why_are_you_going_down_this_path_anyway == 'no':
                                                no()
                                            elif why_are_you_going_down_this_path_anyway == 'yes':
                                                print('\nUuuuhhhhh tell them, but it\'ll be a fucking shit show. \n')
                                    elif sibling == no:
                                        print('\nParent????? \n')
                                        print('\nYou don\'t deserve to run this code, but instead, you deserve to go to a psychiatric ward!!! \n')
                                        time.sleep(1)
                                        exit()
                        case 'school':
                            often = ask_question('\nDo you see your crush often? (No as in big campus/school, different majors. Yes as in you guys are in the same classes.) \n\n',['yes','no'])
                            if often == 'no':
                                yes()
                            elif often == 'yes':
                                irdk()
                        case 'work':
                            fired = ask_question('\nDo you fear of getting fired from your job? \n\n',['yes','no'])
                            if fired == 'yes':
                                no()
                            elif fired == 'no':
                                so_your_sure_about_this = ask_question('\nAre you sure? (No as in you kinda need to pay rent. Yes as in you hate your job.) \n\n',['yes','no'])
                                if so_your_sure_about_this == 'no':
                                    no()
                                elif so_your_sure_about_this == 'yes':
                                    same_level = ask_question('\nIs your crush the same level as you in the work hierarchy? \n\n',['yes','no'])
                                    if same_level == 'yes':
                                        irdk()
                                    elif same_level == 'no':
                                        surperior = ask_question('\nAre they your superior? \n\n',['yes','no'])
                                        if surperior == 'yes':
                                            while True:
                                                surperior_kink = input('\nDo you like them because you have a weird thing for authority figures? \n\n')
                                                if surperior_kink == 'no':
                                                    print('\nThere\'s only one option here and it\'s not this one. Try again. \n\n')
                                                    continue
                                                if surperior_kink == 'yes':
                                                    break
                                            print('\nOfc you have a werid thing for authority figures which is why your here in the first place, but that\'s not the point. \n')
                                            print('\nIf you do it, there is a one percent chance you\'ll get a promotion and a ninety-nine percent chance you\'ll be fired immediately. \n')
                                            end()
                                        elif surperior == 'no':
                                            cooking = ask_question('\nIs there any chance at all your crush actually likes you (1) or is this some sick power play that will make your crush incredibly uncomfortable for the rest of their limited time working there before they inevitably resign? (2) \n\n',['1','2'])
                                            if cooking == '2':
                                                no()
                                            elif cooking == '1':
                                                print('\nHR will hear about this. \n')
                                                end()
                        case 'other':
                            yes()
if __name__ == "__main__":
    main()
