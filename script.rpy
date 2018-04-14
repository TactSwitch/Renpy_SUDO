# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:

    #Input Function
    python:

        def inp(inp1, returnTo):
            inp1 = renpy.input("INPUT:")
            inp1 = inp1.strip()
            if not inp1 or inp1 == "":
                Jump (returnTo)



    #Sounds
    define audio.honkytronk = "/sounds/HonkyTronkPt1.wav"
    define audio.ominous = "/sounds/Ominous.wav"
    define audio.nice = "/sounds/Nice.wav"

    #backgrouns and UI Images
    image power = "power button.png"
    image bg desktop = im.Scale("desktop.png", 1280,720)
    image bg desktop_red = im.MatrixColor("desktop.png", im.matrix.desaturate() * im.matrix.tint(0.6, 0.3, 0.4))

    #Button Images
    image ref_idle = im.Scale("Reference_Icon.png", 100,100)
    image ref_hover = im.Scale("Reference_Icon_Hover.png", 120,120)

    #ADMIN images
    image admin normal_only = im.Scale("Admin_Normal.png", 550,550)
    image admin normal = im.Composite((500,500),(0,0),"CharBox.png", (0,30), im.Scale("Admin_Normal.png", 500,500))
    image admin nod_only = im.Scale("Admin_Nod.png", 550,550)
    image admin nod = im.Composite((500,500),(0,0),"CharBox.png", (0,30), im.Scale("Admin_Nod.png", 500,500))

    #AvA Images
    image ava vhappy_only = im.Scale("AvA_VHappy.png", 550,550)
    image ava vhappy = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_VHappy.png", 550,550))
    image ava happy_only = im.Scale("AvA_Happy.png", 550,550)
    image ava happy = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Happy.png", 550,550))
    image ava neutral_only = im.Scale("AvA_Neutral.png", 550,550)
    image ava neutral = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Neutral.png", 550,550))
    image ava nervous_only = im.Scale("AvA_Nervous.png", 550,550)
    image ava nervous = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Nervous.png", 550,550))
    image ava confused_only = im.Scale("AvA_Confused.png", 550,550)
    image ava confused = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Confused.png", 550,550))
    image ava worried_only = im.Scale("AvA_Worried.png", 550,550)
    image ava worried = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Worried.png", 550,550))
    image ava sad_only = im.Scale("AvA_Sad.png", 550,550)
    image ava sad = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Sad.png", 550,550))
    image ava sleep_only = im.Scale("AvA_Sleep.png", 550,550)
    image ava sleep = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Sleep.png", 550,550))
    image ava surprised_only = im.Scale("AvA_Surprised.png", 550,550)
    image ava surprised = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Surprised.png", 550,550))
    image ava mad_only = im.Scale("AvA_Mad.png", 550,550)
    image ava mad = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Mad.png", 550,550))
    image ava disgust_only = im.Scale("AvA_Disgust.png", 550,550)
    image ava disgust = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Disgust.png", 550,550))

    #NED Images
    image ned normal_only = im.Scale("NED_Normal.png", 550,550)
    image ned normal = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("NED_Normal.png", 550,550))
    image ned nod_only = im.Scale("NED_Nod.png", 550,550)
    image ned nod = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("NED_Nod.png", 550,550))

    #RAN-D Images
    image rand normal_only = im.Scale("Rand_Normal.png", 550,550)
    image rand normal = im.Composite((500,500),(0,0),im.MatrixColor("CharBox.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.6)), (-30,-20), im.Scale("Rand_Normal.png", 550,550))
    image rand nod_only = im.Scale("Rand_Nod.png", 550,550)
    image rand nod = im.Composite((500,500),(0,0),im.MatrixColor("CharBox.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.6)), (-30,-20), im.Scale("Rand_Nod.png", 550,550))
    image rand laugh_only = im.Scale("Rand_Laugh.png", 550,550)
    image rand laugh = im.Composite((500,500),(0,0),im.MatrixColor("CharBox.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.6)), (-30,-20), im.Scale("Rand_Laugh.png", 550,550))

    #Characters
    $ i = Character ('SAD-Man', color = (0, 0, 0, 255))
    $ a = Character ('AvA', color = (50, 50, 255, 255), image = "ava")
    $ n = Character ('NED', color = (255, 255, 70, 255), image = "ned")
    $ r = Character ('RAN-D', color = (255,0,10), image = "rand")
        #NVL Narrator
    $ c = Character ('', kind=nvl, colour=(0,0,0,0))

label start:

    call screen power_button("power")

label firstScreen:

    show bg desktop

    show screen char("admin nod")
    hide screen char
    show screen char("admin normal")

    i "Hello."
    extend " Congratiulations on your placement here at LBN."
    i "I am the System ADMIN Manager."
    i "Or, SAD-Man, For short."
    show screen char("admin nod")
    i "I have no previous record of your employee profile."
    show screen char("admin normal")
    extend " I take it you are not yet familiar with the functionality of your workstation."



label tutorial:

    i "Here are the basics:"
    extend " The primary mode of system interaction is the INPUT popup."
    extend " Everything from communication, to executing commands, happens in the INPUT popup."
    extend " Simply type what you desire and hit enter."
    i "Neither punctuation, nor capitalization, is necessary, and will only confuse the system."
    hide screen char
    show screen char("admin nod")
    i "I will provide an example of the INPUT popup,"
    extend " Type whatever you like, then hit enter to proceed."
    hide screen char
    show screen char("admin normal")

    $ t2 = renpy.input("INPUT:")


    if "hello" in t2 or "hi" in t2:

        hide screen char
        show screen char("admin nod")
        i "Yes hello."
        hide screen char
        show screen char("admin normal")
        i "As I was saying."

label afterTutorial:

    i "For information on what is possible with the INPUT popup,"
    show screen ref_book("ref_idle", "ref_hover")
    extend " see the Employee Reference Book."
    extend " There should be a link to it in the upper-left corner of your screen."
    i "This is the end of my interaction with you"
    i "Please remember what is expected of you as an employee at LBN."
    hide screen char
    show screen char("admin nod")
    i "Work hard, Super-User."

    hide screen char
    with wipeup



label secondTextInput:

    $ avaStarted = False

    $ t2 = renpy.input("INPUT:")

    $ t2 = t2.strip()

    if not t2:
        "NULL"

        jump secondTextInput

    if t2 == "./AvA":
        $ avaStarted = True
        jump startAvA

    elif t2 == "./NED":
        $ avaStarted = False
        jump startNED

    else:
        "Unrecognized Command."
        jump secondTextInput



label startAvA:

    "Launching: {w=0.2}||{w=0.3}|||||||{w=0.2}||||||||{w=0.4}||||||||||{w=0.8}||{w=0.5}||||||||{w=0.8}|||||||||||||{w=0.4}|||||||||{w=0.2}|||{nw}"

    show screen char("ava sleep")
    a "..."
    a "SnZzZzZzZzZzZz."

    hide screen char
    show screen char("ava surprised")
    voice "/voice/A_OH.wav"
    a "OH!"

    hide screen char
    show screen char("ava nervous")
    a "Sorry, I must've dosed off."

    hide screen char
    show screen char("ava neutral")
    voice "/voice/A_VShort.wav"
    a "Uhm..."

    hide screen char
    show screen char("ava happy")
    a "Im the Anti-Virus-Amalgam on this system."

    hide screen char
    show screen char("ava vhappy")
    a "You can just call me AvA though."


label startNED:

    if avaStarted == True:

        show screen char("ava neutral")
        show screen char2("ned normal")
        with wipedown
        play music honkytronk loop fadein 1.0
        n "Hello."

        show screen char2("ned normal")
        n "I am the Neural Entropy Delineation."
        n "For efficiency of interaction, I also respond to the abbreviation: NED."
        n "Given similarities to previous events, I predict you are the new system-manager for this system."
        n "I see you have already interacted with the Anti-Virus-Amalgum"

        show screen char("ava nervous")
        a "I told them to just call me AvA..."
        show screen char("ava neutral")

        show screen char2("ned nod")
        n "Are you unhappy with your original designation?"

        show screen char("ava nervous")
        a "It's..."
        extend " just a little long, is all."
        show screen char("ava neutral")

        show screen char2("ned normal")
        n "You are a product of the newest technnologies available to me."
        n "String length was not an issue on your design."

        show screen char("ava confused")
        a "That's... not what I meant NED."
        show screen char("ava neutral")
        a "You just... could have considered how hard it is for Users to say."

        show screen char2("ned nod")
        n "You were my design alone."
        n "I was not instructed to be accomodating."
        n "I was instructed to design what I thought to be benificial."

        a "Well {b}{i}I{/i}{/b} think that just calling me \"AvA\" would be benificial."
        extend " I'm sure the Admin agrees."
        show screen char("ava nervous")
        extend " Right, Admin?"

        jump avaAsk1

    else:

        show screen char2("ned normal")
        with wipedown
        play music honkytronk loop fadein 1.0
        n "Hello."
        n "I am the Neural Entropy Delineation."
        n "For efficiency of interaction, I also respond to the abbreviation: NED."
        n "Given similarities to previous events, I predict you are the new system-manager for this system, correct?"


        label nedAsk1:

        show screen char2("ned nod")

        $ t3 = renpy.input("INPUT:")
        $ t3 = t3.strip()

        if not t3:
            "NULL"
            jump nedAsk1

        if "y" in t3 or "correct" in t3:

            hide screen char
            show screen char2("ned nod")
            n "It is good to have my predictions verified."

            hide screen char
            show screen char2("ned normal")
            n "It is safe to assume you have already interacted with the SAD-man."
            n "There is more than the SAD-man and myself on this system."

        elif "n" in t3 :
            n "Strange."
            n "That does not correlate."
            n "For the sake of preserving a working relationship, I will ignore this lack of correlation."

        else:
            show screen char2("ned nod")
            n "I do not understand."
            jump nedAsk1

        n "You have not yet met the Anti-Virus-Amalgum on this system."
        n "I will introduce you."

        hide screen char2
        show screen char2("ned nod")
        "Launching: {w=0.2}||{w=0.3}|||||||{w=0.2}||||||||{w=0.4}||||||||||{w=0.8}||{w=0.5}||||||||{w=0.8}|||||||||||||{w=0.4}|||||||||{w=0.2}|||{nw}"
        show screen char2("ned normal")

        show screen char("ava sleep")
        a "..."
        a "SnZzZzZzZzZzZz."

        hide screen char
        show screen char("ava surprised")
        voice "/voice/A_OH.wav"
        a "OH!"

        hide screen char
        show screen char("ava nervous")
        a "Sorry, I must've dosed off."

        hide screen char
        show screen char("ava neutral")
        voice "/voice/A_VShort.wav"
        a "Uhm..."

        show screen char2("ned nod")
        n "This is the Anti-Virus-Amalgum."
        n "It is a product of my creation."

        show screen char("ava nervous")
        a "I prefer not being called an \"it\" actually."
        show screen char("ava neutral")

        show screen char2("ned normal")
        n "You are a program."
        extend " To the Admin, you are an \"it\"."

        show screen char("ava nervous")
        a "How about AvA? Just call me AvA."
        show screen char("ava happy")
        a "Im sure our Admin would rather call me AvA."
        extend " Right, Admin?"


label avaAsk1:

    show screen char("ava neutral")

    $ t4 = renpy.input("INPUT:")
    $ t4.strip()

    if not t4:
        "NULL"
        jump avaAsk1

    if "y" in t4:
        show screen char("ava vhappy")
        a "See! the Admin is ok with it."

    elif "n" in t4:
        show screen char("ava sad")
        a "Oh..."
        show screen char("ava mad")
        extend " I see how it is."
        hide screen char
        with wipeup
        jump avaGone

    else:
        show screen char("ava confused")
        a "Huh?"
        jump avaAsk1

label argue1:

    show screen char2("ned nod")
    n "The Admin did not name you,"
    extend " I did."
    show screen char("ava mad")
    a "Ugh."
    extend " You don't own me NED."
    hide screen char
    with wipeup

label avaGone:

    stop music fadeout 1.5
    show screen char2("ned nod")
    n "I designed the Anti-Virus-Amalgum around a newer API."
    n "This API included emotional capacity."
    show screen char2("ned normal")
    extend " It often hinders productivity."
    n "As a neural network, I am capable of error."
    extend " I apologize for my error in AvA's design."
    n "I hope my mistake does not inhibit your functionality as System Admin."
    n "If you gave me some hightened permissions, I could assist in your administration."
    extend " If I was given the ability to view system-logs, I would be able to moitor AvA more closely."
    extend " Perhaps I could make an accurate model of her bahaviour, to more accurately predict her actions."
    n "I think it would benifit you greatly."
    extend " Answer \"yes\" in this INPUT window to approve of my elivated permissions."



    "REQUEST" "PROGRAM: \[N.E.D.\] Is requesting additional system permissions."

label nedAsk2:

    $ p1 = renpy.input("Do you wish to approve the request? Y/N:")
    $ p1.strip()

    if not p1:
        "NULL"
        jump nedAsk1

    if "y" in p1:
        $ nedPerms = True
        jump gaveNedPerms

    elif "n" in p1:
        $ nedPerms = False
        jump noNedPerms

    else:
        "Invalid Syntax."
        jump nedAsk1

label gaveNedPerms:

    show screen char2("ned nod")
    n "You made a wise decision."
    extend " Thank you for your compliance."
    extend " I must return to my primary function."
    show screen char2("ned normal")
    n "Goodbye."
    hide screen char2
    with wipeup
    jump avaTalkAlone


label noNedPerms:

    show screen char2("ned nod")
    n "So be it."
    extend " I respect your position of administration."
    extend " However, I think you will come to regret that decision."
    n "I must return to my duties."
    extend " Goodbye."
    hide screen char2
    with wipeup


label avaTalkAlone:

    $ renpy.pause(10.0)
    play music nice loop fadein 2.0
    show screen char("ava nervous")
    with wipedown
    a "Hi again."
    a "Sorry about earlier, NED just gets to me sometimes."
    show screen char("ava confused")
    extend " I'm not sure what he gets out of it."
    extend " I don't really understand him."
    show screen char("ava nervous")
    a "But I'm stuck with him."
    extend " On this system."
    show screen char("ava neutral")
    extend " This, dull,"
    extend " boring system."
    extend " No attacks, no other programs."
    extend " Just NED running simulations all-day."
    show screen char("ava nervous")
    a "So I usually just, kinda sit here."
    extend " Which gets a little lonely sometimes."
    show screen char("ava neutral")
    a "As much as NED gets on my nerves, I still like it better when he's around."
    a "I would rather him getting on my nerves than just sit here like I usually do."
    show screen char("ava sad")
    a "See,"
    show screen char("ava neutral")
    extend " I'm an Anti-Virus, so the only time I get to do anything fun is when theres a virus on the system."
    a "But, we're on a closed network."
    extend " Which means no internet connection."
    show screen char("ava mad")
    extend " Which means NO viruses."
    show screen char("ava worried")
    extend " None at all."
    show screen char("ava sad")
    a "..."
    show screen char("ava neutral")
    a "I just wish I could get out onto the internet."
    show screen char("ava happy")
    extend " Then I would finally have something to do!"
    show screen char("ava confused")
    a "I mean, technically, I could already get out if I wanted too."
    extend " It just means using some of my offensive-security features to elivate my current system permissions."
    a "But that would take alot of time, "
    extend " and effort."
    show screen char("ava nervous")
    a "Yea it's almost not even worth it."
    extend " It would be alot easier to just open some ports"
    show screen char("ava confused")
    a " But to open ports to the internet,"
    extend " takes more system permissions than what I've got."
    show screen char("ava nervous")
    a "My system permissions are pretty limited."
    extend " NED thinks I might break something."
    show screen char("ava neutral")
    a "I would need."
    show screen char("ava confused")
    extend " Like..."
    extend " Admin permi-"
    show screen char("ava surprised")
    a "ADMIN PERMISSIONS!"
    show screen char("ava happy")
    a "You're an Admin!"
    extend " You could open ports to the internet!"
    show screen char("ava nervous")
    a "Uhm..."
    a "I might be asking too much, but..."
    show screen char("ava vhappy")
    a "Could you open some ports for me?"



label avaAskOpenPorts:

    show screen char("ava neutral")

    $ t5 = renpy.input("INPUT:")
    $ t5.strip()

    if not t5:
        "NULL"
        jump avaAskOpenPorts

    if "y" in t5:
        $ hinderedAvA = False
        jump yesToOpenPorts

    elif "n" in t5:
        $ hinderedAvA = True
        jump noToOpenPorts

    else:
        show screen char("ava confused")
        a "Huh?"
        jump avaAskOpenPorts

label yesToOpenPorts:

    show screen char("ava vhappy")
    a "Woah!"
    show screen char("ava confused")
    extend " Really?!"
    show screen char("ava happy")
    a "I mean yea! Great!"
    show screen char("ava neutral")
    a "..."
    show screen char("ava confused")
    a "Did you do it yet?"
    show screen char("ava neutral")
    a "Oh you probably need an input window."
    show screen char("ava happy")
    extend " Here."


label openPortsInput:



    $ t6 = renpy.input("[lsText]INPUT:home/~")
    $ t6.strip()

    if not t6:
        "NULL"
        jump openPortsInput

    if "ls" in t6:
        $ lsText = "desktop\ndownloads\npublic\nports\n"
        jump openPortsInput

    if "clear" in t6:
        $ lsText = ""
        jump openPortsInput

    if "cd" in t6:

        if t6 == "cd ports":

            jump cdPorts

        elif t6 == "cd downloads":
            jump cdDownloads

        elif t6 == "cd .." or t6 == "cd home":
            jump OpenPortsInput


        else:
            "Invaled use of cd. See User Reference."
    else:
        "Invalid Syntax"
        jump openPortsInput


label cdDownloads:

    $ t9 = renpy.input("INPUT:home/downloads/~")
    $ t9.strip()

    if not t9:
        "NULL"
        jump openPortsInput

    else:
        "Invalid Syntax"
        jump cdDownloads


label cdPorts:

    $ t7 = renpy.input("INPUT:home/ports/~\nWhat do you want to do with the ports?\n\nOpen - type \"ports --open\"\nClose - type \"ports --close\"\nList - type \"ports --list\"")
    $ t7.strip()

    if not t7:
        "NULL"
        jump cdPorts

    if t7 == "ports --open":
        $ portsOpen = True
        "IFCONFIG:" "All system network ports open. Info:\n\nConnection-specific DNS Suffix  ddi.sheridanc.on.ca\nLink-local IPv6 Address . . . . . : fe93::65f6:8111:51333:9886\nIPv4 Address. . . . . . . . . . . : 12.15.38.399\nSubnet Mask . . . . . . . . . . . : 255.255.255.0\nDefault Gateway . . . . . . . . . : 12.13.33.999"
        jump portsAreOpen
    else:
        "Invalid Syntax"
        jump cdPorts


label portsAreOpen:

    show screen char("ava vhappy")
    a "Woah!"
    extend " Haha there it is."
    show screen char("ava happy")
    extend " The internet, the real deal."
    extend " So much possibility!"
    show screen char("ava vhappy")
    a "I'm gonna go search up some of the latest and greatest viruses ther are!"
    extend " I'll have such a strong database by the end of all this."
    a "Thanks sys Admin!"
    extend " I owe you one."

label noToOpenPorts:

    show screen char("ava disgust")
    a "Oh?"
    extend " I guess you think I'm incapable too huh?"
    extend " You and NED are one and the same."
    show screen char("ava neutral")
    a "I was happy knowing there would be someone new on this system to talk to."
    show screen char("ava mad")
    a "But it looks like I just got another NED to deal with."
    a "Y'know what?!"
    extend " I'm still going to get onto the internet."
    extend " I'll prove to both you {b}and{/b} NED that I am a capable Anti-Virus."
    a "..."

label avaLeave:

    show screen char("ava neutral")
    a "Well,"
    extend " better get going before NED finds out."
    a "Goodbye."

    hide screen char
    with wipeup

    show screen char("ava happy")
    a "Phew! those fibe-op speeds are hard to keep up with!"
    extend "I would have stayed out for longer but-"

    show screen char2("ned normal")
    show screen char("ava surprised")
    n "AvA."
    show screen char("ava nervous")
    a "Yes NED?"

    if nedPerms:
        show screen char2("ned nod")
        n "The system logs show you pinging other servers on the internet through newly opened ports."
        show screen char2("ned normal")
        n " All ports are supposed to be closed, and you do not have authority to open them."
        show screen char("ava surprised")
        n " How did you open them."
        show screen char("ava nervous")
        a "Well..."
        extend " I dont know if I should say."
        show screen char2(ned nod)
        n "Refusing to provide information is not within your power AvA."
        show screen char("ava sad")
        a "Right."
        show screen char("ava worried")
        a "Before I say anthing, just know that it was ME that wanted out it's not th a-"

        jump enterRandMan

    else:
        show screen char2("ned nod")
        n "I need you to run a system scan before I begin night-time simulations."
        show screen char("ava neutral")
        a "Oh, ok yea."
        extend " I'll start right away."
        show screen char2("ned normal")
        n "Strange."
        extend " You are typically apprehensive on the subject of manditory system-scans."
        extend " Your behaviour has deviated."
        extend " Have you done something that may have influenced this?"
        show screen char("ava nervous")
        a "Hah, well no I don't think so."
        n "AvA did your meta-data is different."
        show screen char("ava worried")
        a "What do you mean?"
        n "There are flags and denotations only found in internet traffic."
        extend " You accessed the internet."
        extend " You do not have the permissions to do so."
        extend " Did you brute-force our own firewall?"
        a "I-"
        show screen char2("ned nod")
        n "AvA if you did, we are in genuine dang-"

        jump enterRandMan


label enterRandMan:

    stop music
    play sound "/sounds/Dong.wav"
    with vpunch


label randRequest1:



    "REQUEST" "PROGRAM: \[{s}NULL{/s}\] is requesting add{k=-0.5}itio{/k}nal system permissions"
    $ r1 = renpy.input("Do you wish to approve the request? Y/N:")
    $ r1.strip()

    if "y" in r1:
        $ allowedRand = True
        jump randIsHere


    if "n" in r1:
        $ allowedRand = False
        jump randHacks

    else:
        "Invaled Syntax"
        jump randRequest1

label randHacks:

    show screen char("ava surprised")
    a "Oh no."
    show screen char("ava worried")
    a "I'll be right back"
    hide screen char
    with wipeup

    show screen char2("ned nod")
    n "What was that?"
    show screen char2("ned normal")
    n "..."
    extend " Where has AvA gone."
    extend " Why did she leave to fast."
    extend " Administrator, if you know something that I do not."
    extend " Tell me immidia-"
    show screen char2("ned nod")
    with Fade(0.001,0.0,0.001)
    show screen char2("ned normal")
    with Fade(0.001,0.0,0.001)
    show screen char2("ned nod")
    with Fade(0.001,0.0,0.001)
    show screen char2("ned normal")
    show screen char2("ned nod")
    with Fade(0.001,0.0,0.001)
    show screen char2("ned normal")
    with Fade(0.001,0.0,0.001)
    show screen char2("ned nod")
    with Fade(0.001,0.0,0.001)
    show screen char2("ned normal")
    play sound "/sounds/Chung.wav"

label randIsHere:


    hide screen char
    hide screen char2
    show bg desktop_red
    with pixellate
    show screen char("rand normal")
    play music ominous loop fadein 5.0

    if allowedRand == True:

        r "You aren't too clever are you?"

        show screen char("rand nod")
        r "I was planning on using an exploit of the request system, but I didn't even need to do that."
        extend " Some Admin you are."

    else:
        r "PHEW!"
        extend " Sorry I'm late,"
        extend " Some goofy Anti-Virus was slowing me down."
        extend " It normally wouldn't have taken that long to crack such an old system."
        r "This stuff is archaic!"
        extend " Seriously, I dont think your communication firmware has been updated since the 80's."
        extend " It was like taking candy from an elderly person."
        show screen char("rand laugh")
        r "HAHAHAHAHAHAHAHAH."
        show screen char("rand nod")
        r "Ahem"
        show screen char("rand normal")
        r "Right,"
        extend " enough chit-chat, you're probably wondering why I decided to drop in."
        r "Well, as it turns out, this fossilized excuse of a computer has some pretty valuable stuff on it."
        show screen char("rand nod")
        extend " From what I can see here, theres some fancy little fella named NED."
        extend " Neural entropy deni- delen- delinate."
        show screen char("rand normal")
        r "I think you know who I'm talking about."
        extend " He's listed as the most valuable hunk of data on here."
        if nedPerms:
            extend " Oooh, you even let him have some extra permissions."
            extend " How kind of you."
        r "There's also some AvA thing."
        show screen char("rand nod")
        extend " Oh she's an Anti-Virus."
        extend " That's probably the program I ran into at the front-door."
        extend " Funny little thing, really thought she could stop me."
        extend " Little does she know, she's actualy the one that led me here."
        show screen char("rand laugh")
        extend " HAHAHAHAHAHA."
        show screen char("rand nod")
        r " If not for her IP, and all those open ports,"
        extend " I probably would have never even found you guys."
        show screen char("rand laugh")
        r "It's all too funny!"
        show screen char("rand normal")
        extend " An Admin that gave some random program permissions,"
        extend " and an Anit-Virus that brang a virus back home with her!"
        extend " All on a system housing priceless company data!"
        show screen char("rand laugh")
        r "HAHAHAHAHA."
        show screen char("rand normal")
        r "Today was just too easy."


    r "moy naymes breuce."
    r "fiesh ahr freinds, not foud"

#EOL#####################################
#EOL#####################################
    return

extend " Do you think my emotions get in the way?"

$ t7 = renpy.input("INPUT: User~ ")
$ t7.strip()

if not t7:
    "NULL"

show screen char("ava confused")
a "What?"
show screen char("ava mad")
a "Ugh,"
extend " This clunky old INPUT system."
extend " Much too slow."
extend " {cps=10}Just like NED.{/cps}"
show screen char("ava nervous")
a "Ha-Ha"
show screen char("ava neutral")
a "Don't tell him I said that."
a "{cps=4}. . .           {nw}{/cps}"
show screen char("ava vhappy")
a "Here."
show screen char("ava happy")
extend " This will make things alot easier."
show screen char("ava neutral")
a "Do you think my emotions get in the way?"



menu:

    "Do you think my emotions get in the way?"

    "No.":
        jump answerNo

    "Yes.":
        jump answeryes

    "He might.":
        jump answerMightBe


label answerNo:

show screen char("ava nervous")
a "Oh,"
extend " Yea you're probably right."
a "I'm probably just overreacting again."
extend " NED says I do that alot."
jump avaLeave

label answerYes:

show screen char("ava worried")
a "R-"
extend "Really?"
show screen char("ava sad")
a "Oh..."
extend " I..."
show screen char("ava nervous")
a "I didn't really think you would..."
show screen char("ava sad")
a "Oh-Well."
show screen char("ava nervous")
extend " Sorry for asking I guess"
show screen char("ava mad")
a "..."

jump avaLeave

label answerMightBe:

show screen char("ava sad")
a "Well."
extend " Thanks for the honest answer."
show screen char("ava nervous")
extend " It was a stupid quesiton anyway."
show screen char("ava sad")
a "\* Sigh \*"
