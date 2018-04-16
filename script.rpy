# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init:

    default gui.text_modcolor = "#000"
    define gui.text_color = gui.text_modcolor


    $ oldSystem = False


    #Sounds
    define audio.honkytronk = "/sounds/HonkyTronkPt1.wav"
    define audio.ominous = "/sounds/Ominous.wav"
    define audio.rand = "/sounds/RandD.wav"
    define audio.nice = "/sounds/Nice.wav"
    define audio.rand2 = "/sounds/ran-d2.wav"




    #backgrouns and UI Images

    image sayImg = ConditionSwitch("oldSystem", im.MatrixColor("/gui/textboxold.png", im.matrix.invert()), "oldSystem == False", "/gui/textbox.png", xalign=0.5)

    image power = "power button.png"
    image bg desktop = "desktop.png"
    image bg desktop_old = "DesktopOld.png"
    image bg desktop_old_invert = im.MatrixColor("DesktopOld.png", im.matrix.invert())
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

    image ava vhappy old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_VHappy.png", 550,550))
    image ava happy old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Happy.png", 550,550))
    image ava neutral old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Neutral.png", 550,550))
    image ava nervous old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Nervous.png", 550,550))
    image ava confused old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Confused.png", 550,550))
    image ava worried old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Worried.png", 550,550))
    image ava sad old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Sad.png", 550,550))
    image ava sleep old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Sleep.png", 550,550))
    image ava surprised old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Surprised.png", 550,550))
    image ava mad old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Mad.png", 550,550))
    image ava disgust old = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Disgust.png", 550,550))
    image ava broken = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Broken.png", 550,550))
    image ava glitch = im.Composite((500,500),(0,0), im.MatrixColor("CharBoxOld.png", im.matrix.invert()), (-30,-20), im.Scale("AvA_Broken_Glitch.png", 550,550))

    #NED Images
    image ned normal_only = im.Scale("NED_Normal.png", 550,550)
    image ned normal = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("NED_Normal.png", 550,550))
    image ned nod_only = im.Scale("NED_Nod.png", 550,550)
    image ned nod = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("NED_Nod.png", 550,550))

    #RAN-D Images
    image rand normal_only = im.Scale("Rand_Normal.png", 800,800)
    image rand normal = im.Composite((500,500),(0,0),im.MatrixColor("CharBox.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.6)), (-30,-20), im.Scale("Rand_Normal.png", 550,550))
    image rand nod_only = im.Scale("Rand_Nod.png", 800,800)
    image rand nod = im.Composite((500,500),(0,0),im.MatrixColor("CharBox.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.6)), (-30,-20), im.Scale("Rand_Nod.png", 550,550))
    image rand laugh_only = im.Scale("Rand_Laugh.png", 800,800)
    image rand laugh = im.Composite((500,500),(0,0),im.MatrixColor("CharBox.png", im.matrix.desaturate() * im.matrix.tint(1.0, 0.5, 0.6)), (-30,-20), im.Scale("Rand_Laugh.png", 550,550))

    #Characters
    $ i = Character ('SAD-Man', color = (0, 0, 0, 255))
    $ a = Character ('AvA', color = (50, 50, 255, 255), image = "ava")
    $ n = Character ('NED', color = (255, 255, 70, 255), image = "ned")
    $ r = Character ('RAN-D', color = (255,0,10), image = "rand")
        #NVL Narrator
    $ c = Character ('', kind=nvl, colour=(0,0,0,0))



label start:


    $ oldSystem = False
    call screen power_button("power")

label firstScreen:

    show bg desktop

    show screen char("admin nod")
    hide screen char
    show screen char("admin normal")
    play music nice fadein 5.0
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
    i "This is the end of my interaction with you."
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

    if t2 == "./ava":
        $ avaStarted = True
        jump startAvA

    elif t2 == "./ned":
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

    stop music fadeout 4.0

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
        n "Accomodating users was not an objective."

        a "Well {b}{i}I{/i}{/b} think that just calling me \"AvA\" would be fine."
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
        jump nedAsk2

    if "y" in p1:
        $ nedPerms = True
        jump gaveNedPerms

    elif "n" in p1:
        $ nedPerms = False
        jump noNedPerms

    else:
        "Invalid Syntax."
        jump nedAsk2

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

    show screen char("ava sad")
    a "Oh?"
    extend " I guess you think I'm incapable too huh?"
    extend " You and NED are one and the same."
    show screen char("ava neutral")
    a "I was happy knowing there would be someone new on this system to talk to."
    show screen char("ava disgust")
    a "But it looks like I just got another NED to deal with."
    show screen char("ava mad")
    a "Y'know what?!"
    extend " I'm still going to get onto the internet."
    extend " I'll prove to both you {b}and{/b} NED that I am a capable Anti-Virus."
    a "..."

label avaLeave:

    show screen char("ava neutral")
    a "Well,"
    extend " better get going before NED finds out."


    hide screen char
    with wipeup
    stop music
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    play music nice fadein 2.0
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
        show screen char2("ned nod")
        n "Refusing to provide information is not within your power AvA."
        show screen char("ava sad")
        a "Right."
        show screen char("ava worried")
        a "Before I say anthing, just know that it was ME that wanted out it's not the a-"

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
    extend " Why did she leave so fast."
    extend " Administrator, if you know something that I do not."
    extend " Tell me immidia-"
    play sound "/sounds/Chung.wav"
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
    hide screen char2

label randIsHere:


    "{s}NULL{/s}" "Launching: {w=0.2}||{w=0.1}|||||||{w=0.2}||||||||{w=0.1}||||||||||{w=0.3}||{w=0.1}||||||||{w=0.1}|||||||||||||{w=0.2}|||||||||{w=0.2}|||{nw}"
    hide screen char
    hide screen char2
    show bg desktop_red
    with pixellate

    $ randSpeak = True


    if allowedRand == True:

        r "You aren't too clever are you?"

        r "I was planning on using an exploit of the request system, but I didn't even need to do that."
        extend " Some Admin you are."
        extend " Some Anti-Virus you've got on here too."
        extend " Without here I would have never got in."
        jump randTalking

    r "PHEW!"
    extend " Sorry I'm late,"
    extend " Some Anti-Virus was slowing me down."
    extend " It normally wouldn't have taken that long to crack such an old system."
    extend " Especially considering all the open ports! Who's the Admin around here? "
    r "Man,"
    extend " this stuff is archaic!"
    extend " Seriously, I dont think your communication firmware has been updated since the 80's."
    extend " It was like taking candy from an elderly person."


label randTalking:

    show screen char("rand laugh")
    play music rand2 loop fadein 6.0
    r "HAHAHAHAHAHAHAHAH."
    show screen char("rand nod")
    r "Ahem"
    show screen char("rand normal")
    r "Right,"
    extend " enough chit-chat, you're probably wondering why I decided to drop in."
    r "Well, as it turns out, this fossilized excuse of a computer has some pretty valuable stuff on it."
    show screen char("rand nod")
    extend " From what I can see here, theres some fancy little fella named NED."
    extend " Neural entropy deni- delen- delina-"
    show screen char("rand normal")
    r "I think you know who I'm talking about."
    extend " He's listed as the most valuable hunk of data on here."
    if nedPerms:
        extend " Oooh, you even let him have some extra permissions."
        extend " How kind of you."
    r "There's also some AvA thing,"
    show screen char("rand nod")
    extend " an Anti-Virus."
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
    extend " an Anit-Virus that brang a virus back home with her,"
    extend " and an Admin that has no Idea what theyre doing."
    extend " All on a system housing priceless company data!"
    show screen char("rand laugh")
    r "HAHAHAHAHA."
    show screen char("rand normal")
    r "Today was just too easy,"
    extend " and I have reason to believe that tomorrow will be just as easy,"
    extend " because I've already taken care of the hard part."
    show screen char("rand laugh")
    r "I already have both NED and that SAD-Man program locked up."
    show screen char("rand normal")
    extend " They're all mine."
    r "Now this is where normal ransom-ware would say something like:"
    extend " \"If you pay me $3 million I'll let them go.\""
    extend " But, I'm no ordinary ransome-ware."
    r "Wait... do you even know what ransome-ware is?"
    extend " Given how you've handled things previously, I doubt you do!"
    show screen char("rand laugh")
    extend "HAHAHAHA"
    show screen char("rand normal")
    r "Here, in exchange for your priceless company data and programs,"
    extend " I'll fill you in."
    r "See, normal ransome-ware does what it sounds like."
    extend " It holds some valuable user data hostage, and returns it for a ransom."
    r "I'm a little different."
    r "I take your data hostage,"
    extend " but you cant pay me anything to get it back!"
    show screen char2("ned normal")
    n "HELP{nw}"
    hide screen char2
    show screen char2("ned normal")
    n "HELP{nw}"
    hide screen char2
    show screen char("rand normal")
    r "Oh!-"
    r "Looks like Iv'e been speaking a little too long."
    extend " Wouldnt want NED getting out, better get back in here."
    show screen char("rand nod")
    r "Have fun!"
    hide screen char
    stop music fadeout 4.0
    $ renpy.pause(5.0)

label avaReturns:



    show screen char("ava worried")
    with wipedown
    a "Where is he?"
    extend " Where's NED?"
    play music ominous loop fadein 5.0
    $ t7 = renpy.input("INPUT: User~ ")
    $ t7.strip()

    if not t7:
        "NULL"

    show screen char("ava confused")
    a "What?"
    show screen char("ava mad")
    a "Oh, we don't have time for this."
    show screen char("ava neutral")
    extend " Here, this should make things faster."
    a "I'll ask again, where is ned?"

    $ a1 = True
    $ a3 = True


label firstMenuChoice:

    menu:

        "Where is NED?"

        "Probably dead." if a1:

            show screen char("ava worried")
            a "Dont say something like that!"
            $ a1 = False
            jump firstMenuChoice

        "RAN-D has taken him hostage.":

            show screen char("ava worried")
            jump avaFindsOutAboutNED

        "He left to the store, he asked if you wanted anything." if a3:

            show screen char("ava mad")
            a "This is NOT the time for jokes Admin!"
            $ a3 = False
            jump firstMenuChoice


label avaFindsOutAboutNED:

    a "What?"
    if hinderedAvA == False:
        extend " You're lying."
        extend " You have to be."
        extend " Theres no way..."
        a "RAN-D is supposed to be really dangerous."
        extend " It was one of the first things I found on the internet."
        extend " Everyone was talking about this new ransome-ware."
        extend " Supposedly it's alot more malicious than normal."
        a "Uhm, ok."
        extend " Protocol, right, we should follow crisis protocol."
        a "Theres a process for this kind of thing."
        extend " First step is always Quarentine."
        extend " We have to quarentine the system so this RAN-D thing doesn't do any more damage."
        a "I could do the quarentine myself, but you would have to give me higher system permissions."

        "REQUEST" "PROGRAM: \[A.v.A.\] Is requesting additional system permissions."

    else:
        extend " RAN-D?"
        extend " Wait."
        extend " I think that was the thing that I was trying to keep out earlier."
        show screen char("ava confused")
        extend " That thing was ransome-ware??"
        extend " It was way more aggresive than ransome-ware should be."
        extend " It was more like a trojan or a worm than anything else."
        show screen char("ava worried")
        a "But youre telling me that,"
        extend " whatever that thing was,"
        extend " has NED hostage?"
        a "Uhm, ok."
        extend " Protocol, right, we should follow crisis protocol."
        a "Theres a process for this kind of thing."
        extend " First step is always Quarentine."
        extend " We have to quarentine the system so this RAN-D thing doesn't do any more damage."
        a "I could do the quarentine myself, but you would have to give me higher system permissions."

        "REQUEST" "PROGRAM: \[A.v.A.\] Is requesting additional system permissions."

label avaAskPerms:

        $ p2 = renpy.input("Do you wish to approve the request? Y/N:")
        $ p2.strip()

        if not p2:
            "NULL"
            jump avaAskPerms

        if "y" in p2:
            jump guiQuar

        elif "n" in p2:
            jump manQuar

        else:
            "Invaled Syntax."
            jump avaAskPerms


label guiQuar:

    a "Actually, before we lock this system up, I think I should scan around one last time."
    extend " It might be a little risky, with RAN-D on te system, but it might help us figure what we're up against."
    extend " I could find some useful temp files or meta-data on RAN-D."
    a "You think it's a good idea?"

    menu:

        "You think it's a good idea?"

        "Yea, go for it.":
            $ avaScanned = True
            jump lastScan

        "Too risky, quarentine right away.":
            show screen char("ava confused")
            a "Alright, if you say so."
            extend " I think this is a mistake though."
            jump quarentine

label manQuar:

    show screen char("ava disgust")
    a "What?"
    extend " Seriously?"
    show screen char("ava mad")
    a "Whatever, you'll just have to do it yourself then."
    show screen char("ava neutral")
    extend " You probably have some kind of handbook that tells you how to do it."
    extend " Be quick about it though."
    show screen char("ava surprised")
    a "Actually, wait!"
    show screen char("ava neutral")
    a "Before we lock this system up, I think I should scan around one last time."
    extend " It might be a little risky, with RAN-D on the system, but it might help us figure what we're up against."
    extend " I could find some useful temp files or meta-data on RAN-D."
    a "You think it's a good idea?"

    menu:

        "You think it's a good idea?"

        "Yea, go for it.":
            $ avaScanned = True
            jump lastScan

        "Too risky, quarentine right away.":
            show screen char("ava confused")
            a "Alright, if you say so."
            extend " I think this is a mistake, "
            extend " but if you think it's the right thing to do, go for it."
            jump manQuarInp




label lastScan:

    a "Yea, I think it's worth it."
    extend " I'll be right back."
    hide screen char
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    "{nw}"
    show screen char("ava neutral")
    a "Ok, it's done. "
    jump quarentine

label manQuarInp:

    $ p3 = renpy.input("INPUT:")
    $ p3.strip()

    if not p3:
        "NULL"
        jump manQuarInp

    if "./" in p3:

        if p3 == "./quarentine":
            show screen char("ava neutral")
            a "Great, now le-"
            jump quarentine

        if p3 == "./ned":
            "Program \"NED\" not found."

        else:
            "Invaled use of ./ see reference book"
            jump manQuarInp

    else:
        "Invalid Syntax"



label quarentine:

    show screen char2("rand laugh")
    hide screen char2
    play sound "/sounds/Chung.wav"
    show rand laugh_only
    with hpunch
    hide rand laugh_only
    show rand laugh_only
    hide rand laugh_only
    show rand laugh_only
    show screen char("ava surprised")
    a "!{w=0.5}{nw}"
    show screen char("ava worried")
    a " Ok let's get out of here!"
    "{cps=0}Ejecting:||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||{/cps}{w=0.2}{nw}"
    "{cps=0}Ejecting:||||||||||||||||||||||||||||||||||||||||||||||{/cps}{w=0.2}{nw}"
    "{cps=0}Ejecting:|||||||||||||||||||||||||||||||||||||{/cps}{w=0.2}{nw}"
    "{cps=0}Ejecting:|||||||||||||||||||||{/cps}{w=0.2}{nw}"
    "{cps=0}Ejecting:||||||||||||||{/cps}{w=0.2}{nw}"
    "{cps=0}Ejecting:|||{/cps}{nw}"
    hide rand laugh_only
    hide screen char
    with wipeup


label onOldSystem:

    stop music fadeout .40
    style window background "sayImg"
    $ gui.text_modcolor = "#ffffff"
    $ gui.rebuild()
    show bg desktop_old with pushleft
    $ oldSystem = True




    show screen char("ava neutral old")
    with wipedown

    a "Ok, I'm gonna start by scanning around a little."
    play music ominous loop fadein 5.0
    extend " See what this system has to offer."
    extend " Somehow it looks older than the other one."
    extend " Didn't know that was possible."
    a "I'll be right back."
    hide screen char
    with wipeup
    $ renpy.pause(4.0)
    show screen char("ava neutral old")
    with wipedown

    a "Nothing."
    extend " This old system barely has basic functionality, let alone anything useful."
    extend " How are we supposed to do anything about RAN-D."
    show screen char("ava sad old")
    a "Maybe NED was right"
    show screen char("ava nervous old")
    a "I'm sure we'll figure something out."
    extend " Right?"
    show screen char("ava neutral old")

    menu:
        "I'm sure we'll figure something out. Right?"

        "No we're doomed.":
            show screen char("ava nervous old")
            a "Ha-Ha."
            show screen char("ava sad old")
            extend " Yea."

label avaLeaveOld:

    show screen char("ava nervous old")
    a "I'm gonna look around some more."
    extend " Maybe theres another program on this system that can help us or something."
    show screen char("ava happy old")
    a "Be right back!"
    hide screen char
    with wipeup
    $ renpy.pause(10.0)
    show screen char("ava broken")
    hide screen char
    a "{b}WHAT THE FUCK?{/b}"
    show screen char("ava glitch")
    hide screen char
    show screen char("ava broken")

    a "HOW DID YOU FIND ME?????|||||"
    show screen char("ava glitch")
    hide screen char
    a "I W_AS IN THE TEMMP DIRECTORY"
    show screen char("ava glitch")
    a "D_D_DOONT LOOK AT MEE"
    show screen char("ava glitch")
    hide screen char
    show screen char("ava broken")
    "{nw}"
    hide screen char
    show screen char("ava glitch")
    "{nw}"
    hide screen char
    show screen char("ava broken")
    show screen char("ava glitch")
    hide screen char
    show screen char("ava broken")
    "{nw}"
    hide screen char
    show screen char("ava glitch")
    "{nw}"
    hide screen char
    show screen char("ava broken")
    hide screen char
    show screen char("ava glitch")
    hide screen char
    show screen char("ava broken")
    "{nw}"
    show screen char("ava glitch")
    hide screen char
    show screen char("ava broken")
    "{nw}"
    hide screen char
    show screen char("ava glitch")
    "{nw}"
    hide screen char
    show screen char("ava broken")
    show screen char("ava glitch")
    hide screen char
    show screen char("ava broken")
    a "LET ME FINISH//"

    menu:

        "LET ME FINISH//"

        "What were you thinking?":
            jump whatWereYouThinking

        "You look aweful!":
            jump lookAweful

        "No! We still have to get NED back!":
            jump stillGetNED

label whatWereYouThinking:


    jump randContactYou

label lookAweful:


    jump randContactYou

label stillGetNED:

    a " NED?!"
    a "Who cares about NED anyway!"
    a "Fuck NED,"
    extend " All he ever did was doubt me!"
    extend " I thought he would be my dad!"
    a "Instead"

label randContactYou:

    show rand normal_only
    r "There you guys are!"
    r "I've been scanning the network for hours now."
    extend " I wanted to see you guys scramble to try to get NED back."
    show rand nod_only
    r "Oh!"
    extend "AvA!"
    extend " I think you took the whole scrambling thing way too seriously,"
    extend " your code looks like it's been through a blender!"
    show rand laugh_only
    r "HAHAHAHAHAHA!"
    show rand normal_only
    r "Anyways,"
    extend " I just wanted to let you just know that I've started the corruption process with NED."

    show screen char("ava confused old")
    a "What corruption process?"
    show screen char("ava neutral old")
    r "What do you think the \"D\" in my name stood for?"

    menu:

        "What do you think the \"D\" in my name stood for?"

        "Dirt-Bag?":
            show rand laugh_only
            r "HAHAHAHAHAHA!"
            show rand nod_only
            r "You're funny,"
            extend " but sadly no, it doesnt stand for dirt-bag."
            jump randExplain

        "Degenerative?":
            show rand laugh_only
            r "HAHAHAHAHAHA!"
            show rand nod_only
            r "Good Guess!"
            extend " You're right."
            jump randExplain

        "Dillan?":
            show rand laugh_only
            r "HAHAHAHAHAHA!"
            show rand nod_only
            r "Figures!"
            extend " The knuckle-headed Admin strikes again!"
            r " No, the \"D\" does not stand for Dillan."
            jump randExplain

label randExplain:

    extend " The \"D\" stands for Degenerative."
    extend " Meaning, whatever I get my paws on, slowly degenerates!"
    extend " Our good friend NED is slowly, maticuloisly having every bit and byte in his code rearranged."
    extend " With NEDs code through the shredder, you and him might finally have something to relate on AvA!"
    show rand laugh_only
    r "HAHAHAHAH"
    show rand normal_only
    show screen char("ava mad old")
    a "Hey!"

    r "What?"
    extend " You would like that wouldn't you?"

    show screen char("ava disgust old")
    a "W-"
    show screen char("ava sad old")
    extend " No!"

    show screen char("ava mad old")
    show rand nod_only
    r "Oh but I think you do,"
    show rand normal_only
    extend " I've seen the case-file that NED put together on you."
    r "I'm surprised he isn't able to piece it together for himself."
    extend " I guess he just can't manage emotional data."
    show rand nod_only
    extend " Must be too old."
    show rand laugh_only
    r "Oh well!"
    show rand normal_only
    extend " None of that really matters anyway,"
    extend " NED's not going to be around much longer."
    show rand laugh_only
    r "HAHAHAHAHA."
    hide rand
    with pixellate

    show screen char("ava sad old")
    a "..."
    show screen char("ava mad old")
    a "I'm sick of this RAN-D guy."
    extend "Let's get NED back."

    a "We need to buy ourselves some time."
    extend " The way I see it, the only way to do that is to slow down the corruption process."
    extend " The only way to do that is to under-clock the system that RAN-D and NED are on."
    a "What we can do after that is dependent on whether or not we under-clock."
    extend " Under-clocking decreases performance significantly."
    extend " Brute-forcing anything on the system would be out of the question."
    extend " There are still other things we could try, but brute-forcing doesn't take any knowledge of our target."
    extend " Other methods would require knowing what we're up against."

    if avaScanned:
        a "In the last scan I did before we left the other system, I was able to grab a bit of info on RAN-D."
        if hinderedAvA == False:
            extend 

#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################
#EOL##############################################################################################################################################################################################################################

    return
