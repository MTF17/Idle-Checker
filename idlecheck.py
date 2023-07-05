from dhooks import Webhook
import time
import pyfiglet
import pyautogui

webhook_url = 'your discord webhook here'

print("idle checker for sleepy users")

def idle_or_not():
	for i in range(10000000000000000000):
		mouse_location = pyautogui.position()
		time.sleep(10)
		mouse_location2 = pyautogui.position()
		if mouse_location2 == mouse_location:
			hook = Webhook((webhook_url))
			hook.send('hmhmhm yourname is sleeping')
		else:
			hook = Webhook((webhook_url))
			hook.send('hmhmhm yourname is not sleeeping')

