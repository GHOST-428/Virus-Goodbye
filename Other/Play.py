import pyglet
import pyautogui

pyautogui.press('volumeup', presses=50)

sound = pyglet.resource.media("sound.mp3")
sound.play()

pyglet.app.run()