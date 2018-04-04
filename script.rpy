# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    #backgrouns and UI Images
    image power = "power button.png"
    image bg desktop = im.Scale("desktop.png", 1280, 720)

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

    #NED Images



    $ i = Character ('SAD-Man', color = (0, 0, 0, 255))
    $ a = Character ('AvA', color=(0, 0, 0, 255), image = "ava")



label start:

    call screen power_button("power")

label firstScreen:

    show bg desktop

    show screen char("admin nod")
    hide screen char
    show screen char("admin normal")

    i "Hello."
    i "Congratiulations on your placement here at LBN."
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

label noTutorial:

    i "For information on what is possible with the INPUT popup, see the Employee Reference Book. There should be a link to it in the bottom-left corner of your screen."
    i "This is the end of my interaction with you"
    i "Please remember what is expected of you as an employee at LBN."
    hide screen char
    show screen char("admin nod")
    i "Work hard, Super-User."

    hide screen char


label secondTextInput:

    $ t2 = renpy.input("INPUT:")

    if not t2:

        "NULL"

        jump secondTextInput

    $ t2 = t2.strip()

    if "./AvA" in t2:
        jump startAvA


label startAvA:

    "Launching: {w=0.5}||{w=0.7}|||||||{w=0.2}||||||||{w=1.4}||||||||||{w=2}||{w=0.5}||||||||{w=0.8}|||||||||||||{w=1.2}|||||||||{w=0.2}|||{nw}"

    "AvA.sh Ready:"


    show screen char("ava sleep")
    a "..."
    a "SnZzZzZzZzZzZz."
    hide screen char
    show screen char("ava surprised")
    a "OH!"
    hide screen char
    show screen char("ava nervous")
    a "Sorry, I must've dosed off."
    hide screen char
    show screen char("ava neutral")
    a "Uhm..."
    hide screen char
    show screen char("ava happy")
    a "Im the Anti-Virus-Amalgam on this system."
    hide screen char
    show screen char("ava vhappy")
    a "You can just call me AvA though."
#EOL#####################################
#EOL#####################################
    return
