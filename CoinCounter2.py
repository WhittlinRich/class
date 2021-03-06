import ui
#import dialogs
import random
import threading

# main window ##########################

mainWindow = ui.View()
mainWindow.name = 'Coin Counter'
mainWindow.background_color = 'white'
mainWindow.width = 600 #ui.get_screen_size().width
mainWindow.height = 500 #ui.get_screen_size().height

fontName = "courier"
fontSize = 30

# ui components #########################

label1 = ui.Label()
label1.text = "Enter Amount:"
label1.x = 12
label1.y = 25
label1.height = 32
label1.width = 150

label_status = ui.Label()
label_status.text = "Correct!"
label_status.x = 270
label_status.y = 25
label_status.height = 32
label_status.width = 100
label_status.hidden = True

textBox1 = ui.TextField()
textBox1.x = 130
textBox1.y = 25
textBox1.height = 32
textBox1.width = 120

coinContainer = ui.View()
coinContainer.width = mainWindow.width - 60
coinContainer.height = mainWindow.height - 120
coinContainer.x = 30
coinContainer.y = 100

label_results = ui.Label()
label_results.x = 0
label_results.y = 0
label_results.width = mainWindow.width
label_results.height = mainWindow.height
label_results.background_color = "white"
label_results.font = (fontName, fontSize)
label_results.text_color = "#138b1e"
label_results.alignment = ui.ALIGN_CENTER
label_results.line_break_mode = ui.LB_WORD_WRAP
label_results.number_of_lines = 2
label_results.hidden = True

#ui actions ###########################

def timer1_tick():
	textBox1.begin_editing()
	label_status.hidden = True


def textBox1_action(sender):
	answer = sender.text
	if answer.isdigit() and int(answer) == coinAmount:
		label_status.text = "Correct!"
		label_status.text_color = (0.0, 0.7, 0.0)
		label_status.hidden = False
		clearCoins()
		if questionCounter == 0:
			end()
		else:
			displayCoins()
	else:
		label_status.text = "Nope."
		label_status.text_color = (0.8, 0.0, 0.0)
		label_status.hidden = False		
		
	sender.text = ""
	t = threading.Timer(1.0, timer1_tick)
	t.start()		


#init ################################

textBox1.action = textBox1_action

path = "../Images/"
quarter = ui.Image(path + "quarter.png")
dime = ui.Image(path + "dime.png")
nickel = ui.Image(path + "nickel.png")
penny = ui.Image(path + "penny.png")

coins = {1:penny, 5:nickel, 10:dime, 25:quarter}

coinAmount = 0
currentX = 0
currentRow = 0
rowHeight = 100
gap = 6

totalQuestions = 10
questionCounter = totalQuestions

#functions ###########################

def getCoinWidth(value):
	width = 100
	if value == 1:
		width = 76
	elif value == 5:
		width = 85
	elif value == 10:
		width = 72
	elif value == 25:
		width = 100
	return width


def clearCoins():
	global coinAmount
	global currentX
	global currentRow
	coinAmount = 0
	currentX = 0
	currentRow = 0

	for subview in coinContainer.subviews:
		coinContainer.remove_subview(subview)


def displayCoins():
	global coinAmount
	global currentX
	global currentRow
	global questionCounter
	
	questionCounter -= 1
	totalCoins = random.randint(3, 10)
	
	for i in range(totalCoins):
		
		picture1 = ui.ImageView()	
		value, coinImage = random.choice(list(coins.items()))
		
		coinAmount += value
		imageViewWidth = getCoinWidth(value)
		
		if currentX + imageViewWidth + gap > coinContainer.width:
			currentX = 0
			currentRow += 1
		
		coinY = currentRow * (rowHeight + gap)
		picture1.y = coinY
		picture1.x = currentX
		currentX += imageViewWidth + gap
		
		picture1.width = imageViewWidth
		picture1.height = imageViewWidth
		picture1.image = coinImage
			
		coinContainer.add_subview(picture1)
		

def end():
	msg = "You completed\n" + str(totalQuestions) + " questions!"
	#dialogs.alert("Done!", msg, "OK", hide_cancel_button = True)
	label_results.text = msg
	label_results.hidden = False


#display window ##########################

displayCoins()

mainWindow.add_subview(coinContainer)
mainWindow.add_subview(label1)
mainWindow.add_subview(label_status)
mainWindow.add_subview(textBox1)
mainWindow.add_subview(label_results)

#mainWindow.present('fullscreen')
mainWindow.present('sheet')

textBox1.begin_editing()

###########################################
