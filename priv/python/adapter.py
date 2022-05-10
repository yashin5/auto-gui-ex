import pyautogui
import json

def position():
    return json.dumps(pyautogui.position())

def moveTo(x, y, duration=0.0, tween=pyautogui.linear, logScreenshot=False, _pause=True):
    return pyautogui.moveTo(x, y, duration, tween, logScreenshot, _pause)

def click(
    x=None, y=None, clicks=1, interval=0.0, button="primary", duration=0.0, tween=pyautogui.linear, logScreenshot=None, _pause=True
):
    return pyautogui.click(x, y, clicks, interval, button.decode("utf-8"), duration, tween, logScreenshot, _pause)


def moveRel(xOffset=None, yOffset=None, duration=0.0, tween=pyautogui.linear, logScreenshot=False, _pause=True):
    return pyautogui.moveRel(xOffset, yOffset, duration, tween, logScreenshot, _pause)

def dragTo(
    x=None, y=None, duration=0.0, tween=pyautogui.linear, button="primary", logScreenshot=None, _pause=True, mouseDownUp=True
):
    return pyautogui.dragTo(x, y, duration, tween, button.decode("utf-8"), logScreenshot, _pause, mouseDownUp)

def dragRel(
    xOffset=0, yOffset=0, duration=0.0, tween=pyautogui.linear, button="primary", logScreenshot=None, _pause=True, mouseDownUp=True
):
    return pyautogui.dragRel(xOffset, yOffset, duration, tween, button.decode("utf-8"), logScreenshot, _pause, mouseDownUp)

def isValidKey(key):
    return pyautogui.isValidKey(key.decode("utf-8"))
    
def printInfo(dontPrint=False):
    return pyautogui.printInfo(dontPrint)

def getInfo():
    info = pyautogui.getInfo()
    size = info[4]

    return json.dumps({"width": size.width, "height":size.height, "version": info[2], "sys_version": info[1], "sys_executable": info[3], "platform": info[0]})

def run(commandStr, _ssCount=None):
    return pyautogui.run(commandStr.decode("utf-8"), _ssCount)

def countdown(seconds):
    return pyautogui.countdown(seconds)

def displayMousePosition(xOffset=0, yOffset=0):
    return pyautogui.displayMousePosition(xOffset, yOffset)

def failSafeCheck():
    return pyautogui.failSafeCheck()

def hotkey(*args, **kwargs):
    handled_args = tuple(map(lambda arg: arg.decode("utf-8"), args))
    return pyautogui.hotkey(*handled_args, **kwargs)

def typewrite(message, interval=0.0, logScreenshot=None, _pause=True):
    return pyautogui.typewrite(message.decode("utf-8"), interval, logScreenshot, _pause)

def hold(keys, logScreenshot=None, _pause=True):
    return pyautogui.hold(keys.decode("utf-8"), logScreenshot, _pause)

def press(keys, presses=1, interval=0.0, logScreenshot=None, _pause=True):
    return pyautogui.press(keys.decode("utf-8"), presses, interval, logScreenshot, _pause)

for func_name in ["scroll", "vscroll", "hscroll"]:
    exec(f"""def {func_name}(clicks, x=None, y=None, logScreenshot=None, _pause=True):
    return pyautogui.{func_name}(clicks, x, y, logScreenshot, _pause)""")

for func_name in ["keyUp", "keyDown"]:
    exec(f"""def {func_name}(key, logScreenshot=None, _pause=True):
    return pyautogui.{func_name}(key.decode("utf-8"), logScreenshot, _pause)""")

for func_name in ["leftClick", "rightClick", "middleClick"]:
    exec(f"""def {func_name}(x=None, y=None, interval=0.0, duration=0.0, tween=pyautogui.linear, logScreenshot=None, _pause=True):
    return pyautogui.{func_name}(x, y, interval, duration, tween, logScreenshot, _pause)""")