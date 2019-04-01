#! python3
import autopy
import keyboard

gameURL = "http://www.aimbooster.com/"


def findDOT(startArea):
    screen = autopy.bitmap.capture_screen()
    pos = screen.find_color((3, 133, 3), 0.03,
                            ((startArea[0], startArea[1]), (1600, 900)))
    if pos:
        # print("Found DOT at: %s" % str(pos))
        autopy.mouse.move(pos[0]+1, pos[1])
        autopy.mouse.click()


def findGameArea():
    for i in range(10):
        screen = autopy.bitmap.capture_screen()
        pos = screen.find_color((114, 114, 114), 0.03)
        if pos:
            # print("Game Area: " + str(pos))
            return pos
    exit()


def exitGame():
    if keyboard.is_pressed('q'):
        # print('Exit DOT AIM BOT !!')
        return True
    return False


startArea = findGameArea()
for i in range(1000):
    findDOT(startArea)
    if exitGame() == True:
        break