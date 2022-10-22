from types import NoneType
import pyautogui
import pyscreeze
from utils import add_encounter, record_OBS, notify_user
from playback import playActions
from time import sleep


def warning():
    """
    Messages the user, captures Replay Buffer clip, and exits the script.
    """
    notify_user()  # Send a text/call
    record_OBS()  # Capture clip
    exit()


def run_away(button: pyscreeze.Point):
    """
    Receives Run Button Coordinates and clicks the coordinates.
    Moves the user's cursor to the run button coordinates for a split seconds and moves it back.
    """

    current_posiiton = pyautogui.position()

    pyautogui.click(button)  # Clicks run button, adds encounter
    add_encounter(1)

    # Move cursor back to original position
    sleep(0.1)
    pyautogui.moveTo(current_posiiton)


#### SINGLES ####
def singles(img_left: NoneType or pyscreeze.Point, img_right: NoneType or pyscreeze.Point):
    """
    Moves the player to the left or right depending on their position in game.
    """
    if img_left is not None:
        pyautogui.keyDown('d') # Start moving right if user has reached furthest left point

    if img_right is not None: 
        pyautogui.keyUp('d') # Start moving left if user has reached furthest right point
        pyautogui.keyDown('a')


#### HORDES ####
def teleport():
    pyautogui.press('z')
    sleep(2)


def sweet_scent():
    pyautogui.press('x')
    sleep(1)


def replenish_leppa():
    pyautogui.press('e')


def heal_unova():
    playActions('recordings\pokecenter_unova.json')
    pokecenter_unova = None
    # TODO: set a time limit before catches an error
    while pokecenter_unova == None:
        pokecenter_unova = pyautogui.locateCenterOnScreen('images/Events/pokecenter_unova.PNG', confidence=0.8)


def icirrus_city():
    teleport()
    heal_unova()
    playActions('recordings\DRAGONSPRIAL.json') # Get into position


# TODO: Add more Horde Replays


#### FISHING ####
def fishing():
    pyautogui.press('f')
    sleep(0.5)
    return


def skip_nibble():
    pyautogui.press('e')
    return


def skip_landed():
    pyautogui.press('e')
    sleep(3)
    return