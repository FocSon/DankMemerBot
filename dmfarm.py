import keyboard
import pyperclip
import pyautogui

from time import sleep
from random import randint

c=0
post=['n','e','r','d']

while True:
	sleep(13)
	
	keyboard.write("pls fish")
	keyboard.press_and_release("enter")
	sleep(10)

	keyboard.write("pls beg")
	keyboard.press_and_release("enter")
	sleep(10)

	keyboard.write("pls search")
	keyboard.press_and_release("enter")
	sleep(1)

	pyautogui.moveTo=(564, 903)
	for e in range(3):
	    pyautogui.click(564, 903)

	keyboard.press_and_release("ctrl+c")
	sleep(0.5)
	clipboard=pyperclip.paste()
	choix=clipboard.split(', ')
	print(choix)
	try:
		choix[2]=choix[2][:len(choix[2])-2]
	except:
		pass

	print(choix)

	if("dresser" in choix):
		keyboard.write("dresser")
	elif("discord" in choix):
		keyboard.write("discord")
	elif("dog" in choix):
		keyboard.write("dog")
	elif("mailbox" in choix):
		keyboard.write("mailbox")
	elif("couch" in choix):
		keyboard.write("couch")
	elif("bed" in choix):
		keyboard.write("bed")
	elif("coat" in choix):
		keyboard.write("coat")
	else:
		keyboard.write("no")

	keyboard.press_and_release("enter")
	sleep(10)

	if(c%2==0):
		keyboard.write("pls postmeme")
		keyboard.press_and_release("enter")
		sleep(2)

		rand=randint(0,3)
		keyboard.write(post[rand])
		keyboard.press_and_release("enter")

	c+=1

	if(c%50==0):		
		keyboard.write("pls buy laptop")
		keyboard.press_and_release("enter")
		keyboard.write("pls deposit max")
		keyboard.press_and_release("enter")

	print(c)