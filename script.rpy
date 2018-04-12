# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:

    #Input Function
    python:
        def inp(inp1, returnTo):
            inp1 = renpy.input("INPUT:")
            inp1 = inp1.strip()
            if not inp1:
                Jump (returnTo);



    #Sounds
    define audio.honkytronk = "/sounds/HonkyTronkPt1.wav"
    define audio.ominous = "/sounds/Ominous.wav"

    #backgrouns and UI Images
    image power = "power button.png"
    image bg desktop = im.Scale("desktop.png", 1280,720)

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
    image ava confused = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("AvA_Nervous.png", 550,550))
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

    #NED Images
    image ned normal_only = im.Scale("NED_Normal.png", 550,550)
    image ned normal = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("NED_Normal.png", 550,550))
    image ned nod_only = im.Scale("NED_Nod.png", 550,550)
    image ned nod = im.Composite((500,500),(0,0),"CharBox.png", (-30,-20), im.Scale("NED_Nod.png", 550,550))

    #Characters
    $ i = Character ('SAD-Man', color = (0, 0, 0, 255))
    $ a = Character ('AvA', color = (50, 50, 255, 255), image = "ava")
    $ n = Character ('NED', color = (255, 255, 70, 255), image = "ned")



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
    hide screen char
    show screen char("admin nod")
    i "I have no previous record of your employee profile."
    hide screen char
    show screen char("admin normal")
    i "I take it you are not yet familiar with the functionality of your workstation."



label tutorial:

    i "Here are the basics:"
    i "The primary mode of system interaction is the INPUT popup."
    i "Everything from communication, to executing commands, happens in the INPUT popup."
    i "Simply type what you desire and hit enter."
    i "Neither punctuation, nor capitalization, is necessary, and will only confuse the system."
    hide screen char
    show screen char("admin nod")
    i "I will provide an example of the INPUT popup:"
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
    extend " see the Employee Reference Book. There should be a link to it in the bottom-left corner of your screen."
    i "This is the end of my interaction with you"
    i "Please remember what is expected of you as an employee at LBN."
    hide screen char
    show screen char("admin nod")
    i "Work hard, Super-User."

    hide screen char



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

    "Launching: {w=0.5}||{w=0.7}|||||||{w=0.2}||||||||{w=1.4}||||||||||{w=2}||{w=0.5}||||||||{w=0.8}|||||||||||||{w=1.2}|||||||||{w=0.2}|||{nw}"

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

        show screen char2("ned normal")
        play music honkytronk loop fadein 1.0
        n "Hello."

        show screen char("ava neutral")
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
        a "It's just a little long, is all."
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

    else:

        show screen char2("ned normal")
        n "Hello."
        n "I am the Neural Entropy Delineation."
        n "For efficiency of interaction, I also respond to the abbreviation: NED."
        n "Given similarities to previous events, I predict you are the new system-manager for this system, correct?"

        $ t3 = renpy.input("INPUT:")
        $ t3 = t3.strip()

        if not t3:
            "NULL"

        if "y" in t3 or "correct" in t3:

            hide screen char
            show screen char2("ned nod")
            n "It is good to have my predictions verified."

            hide screen char
            show screen char2("ned normal")
            n "The logs show that you have already interacted with the SAD-man."
            n "There is more than the SAD-man and myself on this system."

        elif "n" in t3 :
            n "Strange."
            n "That does not correlate."
            n "For the sake of preserving a working relationship, I will ignore this lack of correlation."

        n "You have not yet met the Anti-Virus-Amalgum on this system."
        n "I shal introduce you"

        hide screen char2
        show screen char2("ned nod")
        "Launching: {w=0.5}||{w=0.7}|||||||{w=0.2}||||||||{w=1.4}||||||||||{w=2}||{w=0.5}||||||||{w=0.8}|||||||||||||{w=1.2}|||||||||{w=0.2}|||{nw}"
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
        a "I prefer not being called an \"it\" actually"
        show screen char("ava neutral")

        show screen char2("ned normal")
        n "You are my creation, It is illogical to refer to you as anything other."

        show screen char("ava nervous")
        a "How about AvA? Just call me AvA."
        show screen char("ava happy")
        a "Im sure our Admin would rather call me AvA."
        a "Right?"


label avaAsk1:

    show screen char("ava neutral")

    $ t4 = renpy.input("INPUT:")
    $ t4.strip()

    if not t4:
        show screen char
        a "Huh?"
        jump avaAsk1

    if "y" in t4:
        show screen char("ava vhappy")
        a "See! the Admin is ok with it."

    elif "n" in t4:
        show screen char("ava sad")
        a "Oh..."
        show screen char("ava mad")
        a "I see how it is."
        hide screen char
        jump avaGone

label argue1:

    show screen char("ava mad")
    a "Ugh."
    extend "You don't own me NED."
    hide screen char


label avaGone:

    show screen char2("ned nod")
    n "I designed the Anti-Virus-Amalgum around a newer API."
    n "This API included emotional capacity."
    show screen char2("ned normal")
    extend " They often hinder productivity."
    n "I apologize for my error in design."
    n ""

label avaTalkAlone:

    show screen char("ava happy")
    a "Hi again."
    show screen char("ava nervous")
    a "Sorry about earlier, NED just gets to me sometimes."
    show screen char("ava sad")
    a "I'm not sure what he gets out of it."
    a "I don't understand him."
    a ""

#EOL#####################################
#EOL#####################################
    return
