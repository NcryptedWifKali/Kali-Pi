#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
## Global display settings ##

#++++++++++++++++++++++++++++#
#+   Select color scheme    +#

# Tron theme orange
##tron_regular = tron_ora
##tron_light = tron_yel
##tron_inverse = tron_whi

# Tron theme blue
tron_regular = tron_blu
tron_light = tron_whi
tron_inverse = tron_yel

#+           End            +#
#++++++++++++++++++++++++++++#

# Outer Border
pygame.draw.rect(screen, tron_light, (0,0,screen_x,screen_y),10)

## Global display settings ##
#############################

#############################
##    Local Functions      ##

def local_on_touch():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # button 1 event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and newOriginY <= touch_pos[1] <= (newOriginY + newButtonHeight):
            return 1
    # button 2 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY <= touch_pos[1] <= (newOriginY + newButtonHeight):
            return 2
    # button 3 event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY <= touch_pos[1] <= (newOriginY + newButtonHeight):
            return 3
    # button 4 event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and (newOriginY + newButtonHeight + newSpacing) <= touch_pos[1] <= newOriginY + (newButtonHeight * 2) + newSpacing:
            return 4
    # button 5 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY + newButtonHeight + newSpacing <= touch_pos[1] <= newOriginY + (newButtonHeight * 2) + newSpacing:
            return 5
    # button 6 event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY + newButtonHeight + newSpacing <= touch_pos[1] <= newOriginY + (newButtonHeight * 2) + newSpacing:
            return 6
    # button 7 event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 3) + (newSpacing * 2):
            return 7
    # button 8 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 3) + (newSpacing * 2):
            return 8
        # button 9 event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 3) + (newSpacing * 2):
            return 9
    # button c event
    if newOriginX <= touch_pos[0] <= (newOriginX + newButtonWidth) and newOriginY + (newButtonHeight * 3) + (newSpacing * 3) <= touch_pos[1] <= newOriginY + (newButtonHeight * 4) + (newSpacing * 3):
            return "c"
    # button 0 event
    if newOriginX + newButtonWidth + newSpacing <= touch_pos[0] <= newOriginX + (newButtonWidth * 2) + newSpacing and newOriginY + (newButtonHeight * 3) + (newSpacing * 3) <= touch_pos[1] <= newOriginY + (newButtonHeight * 4) + (newSpacing * 3):
            return 0
    # button e event
    if newOriginX + (newButtonWidth * 2) + (newSpacing * 2) <= touch_pos[0] <= newOriginX + (newButtonWidth * 3) + (newSpacing * 2) and newOriginY + (newButtonHeight * 2) + (newSpacing * 2) <= touch_pos[1] <= newOriginY + (newButtonHeight * 4) + (newSpacing * 3):
            return "e"

pin = ""


##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# Overwrite dimensions

###########################
##  Screen layouts       ##

newOriginX = originX
newOriginY = originY
newSpacing = spacing
newButtonWidth = buttonWidth
newButtonHeight = buttonHeight / 4 * 3
newLabelFont = labelFont / 3 * 2
newLabelPadding = labelPadding
newTitleFont = titleFont / 3 * 2


##  Screen layouts       ##
###########################


# define all of the buttons
titleButton = Button("       Environmental Survey - Humidity Sensor    ", newOriginX, newOriginX, newButtonHeight, buttonWidth * 3  + spacing * 2, tron_inverse, newTitleFont)
button1 = Button(newLabelPadding * " " + " " * 15 + "1", newOriginX, newOriginY, newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button2 = Button(newLabelPadding * " " + " " * 15 + "2", newOriginX + newButtonWidth + newSpacing, newOriginY, newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button3 = Button(newLabelPadding * " " + " " * 15 + "3", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY, newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button4 = Button(newLabelPadding * " " + " " * 15 + "4", newOriginX, newOriginY + newButtonHeight + newSpacing, newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button5 = Button(newLabelPadding * " " + " " * 15 + "5", newOriginX + newButtonWidth + newSpacing, newOriginY + newButtonHeight + newSpacing, newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button6 = Button(newLabelPadding * " " + " " * 15 + "6", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY + newButtonHeight + newSpacing, newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button7 = Button(newLabelPadding * " " + " " * 15 + "7", newOriginX, newOriginY + (newButtonHeight * 2) + (newSpacing * 2), newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button8 = Button(newLabelPadding * " " + " " * 15 + "8", newOriginX + newButtonWidth + newSpacing, newOriginY + (newButtonHeight * 2) + (newSpacing * 2), newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button9 = Button(newLabelPadding * " " + " " * 15 + "9", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY + (newButtonHeight * 2) + (newSpacing * 2), newButtonHeight, newButtonWidth, tron_light, newLabelFont)
buttonc = Button(newLabelPadding * " " + " " * 15 + "c", newOriginX, newOriginY + (newButtonHeight * 3) + (newSpacing * 3), newButtonHeight, newButtonWidth, tron_light, newLabelFont)
button0 = Button(newLabelPadding * " " + " " * 15 + "0", newOriginX + newButtonWidth + newSpacing, newOriginY + (newButtonHeight * 3) + (newSpacing * 3), newButtonHeight, newButtonWidth, tron_light, newLabelFont)
buttone = Button(newLabelPadding * " " + " " * 15 + "e", newOriginX + (newButtonWidth * 2) + (newSpacing * 2), newOriginY + (newButtonHeight * 3) + (newSpacing * 3), newButtonHeight, newButtonWidth, tron_light, newLabelFont)


def make_button(button):
    if button.disable == 1:
        button.color = grey

    pygame.draw.rect(screen, tron_regular, (button.xpo-10,button.ypo-10,button.width,button.height),3)
    pygame.draw.rect(screen, tron_light, (button.xpo-9,button.ypo-9,button.width-1,button.height-1),1)
    pygame.draw.rect(screen, tron_regular, (button.xpo-8,button.ypo-8,button.width-2,button.height-2),1)
    font=pygame.font.Font(None,button.fntSize)
    label=font.render(str(button.text), 1, (button.color))
    screen.blit(label,(button.xpo,button.ypo+7))

# Define each button press action
def button(number):
    global pin

    if number == 1:
        if button1.disable == 1:
            return

        # 1
        pin=pin+"1"
        return

    if number == 2:
        if button2.disable == 1:
            return

	# 2
        pin=pin+"2"
        return

    if number == 3:
        if button3.disable == 1:
            return

        # 3
        pin=pin+"3"

    if number == 4:
        if button4.disable == 1:
            return

        # 4
        pin=pin+"4"
        return

    if number == 5:
        if button5.disable == 1:
            return

	# 5
        pin=pin+"5"
	return

    if number == 6:
        if button6.disable == 1:
            return

	# 6
        pin=pin+"6"
        return

    if number == 7:
        if button7.disable == 1:
            return

        # 7
        pin=pin+"7"
        return

    if number == 8:
        if button8.disable == 1:
            return

        # 8
        pin=pin+"8"
        return

    if number == 9:
        if button9.disable == 1:
            return

        # 9
        pin=pin+"9"
        return

    if number == "c":
        if buttonc.disable == 1:
            return

        # Clear
#        pin = ""
#        return
        process = subprocess.call("setterm -term linux -back default -fore white -clear all", shell=True)
        pygame.quit()
        sys.exit()

    if number == 0:
        if button9.disable == 1:
            return

        # 0
        pin=pin+"0"

    if number == "e":
        if buttone.disable == 1:
            return

        # Enter
        if pin != "1337":
            pin=""
            return
        else:
            pygame.quit()
            page=os.environ["MENUDIR"] + "menu-1.py"
            os.execvp("python", ["python", page])
            sys.exit()


# Buttons and labels
# See variables at the top of the document to adjust the menu

# Title
make_button(titleButton)

# First Row
# Button 1
button1.disable = 0  # "1" disables button

if button1.disable == 1:
    make_button(button1)
else:
    # Add button launch code here
    make_button(button1)

# Button 2
# Button 2
button2.disable = 0  # "1" disables button

if button2.disable == 1:
    make_button(button2)
else:
    # Add button launch code here
    make_button(button2)

# Button 3
button3.disable = 0  # "1" disables button

if button3.disable == 1:
    make_button(button3)
else:
    # Add button launch code here
    make_button(button3)


# Second Row
# Button 4
button4.disable = 0  # "1" disables button

if button4.disable == 1:
    make_button(button4)
else:
    # Add button launch code here
    make_button(button4)

# Button 5
button5.disable = 0  # "1" disables button

if button5.disable == 1:
    make_button(button5)
else:
    # Add button launch code here
    make_button(button5)


# Button 6
button6.disable = 0  # "1" disables button

if button6.disable == 1:
    make_button(button6)
else:
    # Add button launch code here
    make_button(button6)


# Third Row
# Button 7
button7.disable = 0  # "1" disables button

if button7.disable == 1:
    make_button(button7)
else:
    # Add button launch code here
    make_button(button7)

# Button 8
button8.disable = 0  # "1" disables button

if button8.disable == 1:
    make_button(button8)
else:
    # Add button launch code here
    make_button(button8)

# Button 9
button9.disable = 0  # "1" disables button

if button9.disable == 1:
    make_button(button9)
else:
    # Add button launch code here
    make_button(button9)

# Button c
buttonc.disable = 0  # "1" disables button

if buttonc.disable == 1:
    make_button(buttonc)
else:
    # Add button launch code here
    make_button(buttonc)

# Button 0
button0.disable = 0  # "1" disables button

if button0.disable == 1:
    make_button(button0)
else:
    # Add button launch code here
    make_button(button0)

# Button e
buttone.disable = 0  # "1" disables button

if buttone.disable == 1:
    make_button(buttone)
else:
    # Add button launch code here
    make_button(buttone)

##        Buttons          ##
#############################


#############################
##        Input loop       ##

#While loop to manage touch screen inputs
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            num = local_on_touch()
            button(num)

        #ensure there is always a safe way to end the program if the touch screen fails
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
    ## Reduce CPU utilisation
    time.sleep(0.1)

##        Input loop       ##
#############################
