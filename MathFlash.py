import ui
import random
import threading

# main window ##########################

mainWindow = ui.View()
mainWindow.name = 'Math Flash'
mainWindow.background_color = 'white'
mainWindow.width = 400 #ui.get_screen_size().width
mainWindow.height = 300 #ui.get_screen_size().height

fontName = "courier"
fontSize = 30

# ui components #########################

label_top = ui.Label()
#label_top.text = "23"
label_top.alignment = ui.ALIGN_RIGHT
label_top.font = (fontName, fontSize)
label_top.x = mainWindow.width / 2 - 30
label_top.y = 80
label_top.height = 32
label_top.width = 70

label_bottom = ui.Label()
#label_bottom.text = "10"
label_bottom.alignment = ui.ALIGN_RIGHT
label_bottom.font = (fontName, fontSize)
label_bottom.x = label_top.x
label_bottom.y = label_top.y + label_top.height
label_bottom.height = 32
label_bottom.width = 70

label_operation = ui.Label()
#label_operation.text = "+"
label_operation.alignment = ui.ALIGN_RIGHT
label_operation.font = (fontName, fontSize)
label_operation.height = 32
label_operation.width = 32
label_operation.x = label_bottom.x - label_operation.width
label_operation.y = label_bottom.y

label_line = ui.Label()
label_line.text = "_____"
label_line.alignment = ui.ALIGN_CENTER
label_line.font = (fontName, fontSize)
label_line.x = label_operation.x
label_line.y = label_bottom.y + 4
label_line.height = 32
label_line.width = 120

textBox_answer = ui.TextField()
textBox_answer.alignment = ui.ALIGN_RIGHT
textBox_answer.font = (fontName, fontSize)
textBox_answer.x = label_top.x - 14
textBox_answer.y = label_line.x + label_line.height - 10
textBox_answer.height = 32
textBox_answer.width = 90

label_status = ui.Label()
label_status.text = "Correct!"
label_status.font = (fontName, fontSize)
label_status.alignment = ui.ALIGN_CENTER
label_status.height = 32
label_status.width = 160
label_status.center = (mainWindow.width / 2, label_top.y - label_status.height)
label_status.hidden = True

#ui actions ###########################

def timer1_tick():
	textBox_answer.begin_editing()
	label_status.hidden = True


def textBox_answer_action(sender):
	answer = sender.text
	if answer.isdigit() and int(answer) == result:
		label_status.text = "Correct!"
		label_status.text_color = (0.0, 0.7, 0.0)
		label_status.hidden = False
		displayQuestion()
	else:
		label_status.text = "Nope"
		label_status.text_color = (0.8, 0.0, 0.0)
		label_status.hidden = False		
	sender.text = ""
	t = threading.Timer(1.0, timer1_tick)
	t.start()	

#init ################################

textBox_answer.action = textBox_answer_action

minRangeTop = 1
maxRangeTop = 10
minRangeBot = 1
maxRangeBot = 10
operation = "+"
result = 0

#functions ###########################

def displayQuestion():
	global result
	global minRangeTop
	
	randomBottom = random.randint(minRangeBot, maxRangeBot)
	if operation == '-':
		minRangeTop = randomBottom
	randomTop = random.randint(minRangeTop, maxRangeTop)	
	
	result = eval(str(randomTop) + " " + operation + " " + str(randomBottom))

	label_operation.text = operation
	label_top.text = str(randomTop)
	label_bottom.text = str(randomBottom)

#display window ##########################

displayQuestion()

mainWindow.add_subview(label_top)
mainWindow.add_subview(label_bottom)
mainWindow.add_subview(label_operation)
mainWindow.add_subview(label_line)
mainWindow.add_subview(textBox_answer)
mainWindow.add_subview(label_status)

mainWindow.present('sheet')

textBox_answer.begin_editing()

###########################################
