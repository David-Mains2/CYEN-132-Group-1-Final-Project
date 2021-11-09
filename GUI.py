#GUI for out smoke detector

from tkinter import *
import tkinter.font as font
from time import sleep
import webbrowser

root = Tk()
root.geometry("750x440")
root["bg"] = "grey5"



#main function that brings up main menu
#it first tries to get rid of the messag menu if it is up
def MainFunction():
	root.title("SSM")
	try:
		destroy_message_menu()
	except:
		pass
	start_label("Smart Smoke Detector", "seashell4")
	main_menu()
	loop()

#THIS DELETS THE MAIN MENU
#THEN IT BRINGS UP THE MESSAGE MENU
#ITS PRETTY MUCH THE 2ND MAIN FUNCTION 
def messageFAQs():
	destroy_start()
	root.title("Message details")
	start_label("Explanation of our Message System", "deep sky blue" )
	message_menu()

#function to clear start menu
def destroy_start():
	things_to_destory = [smoke_frame, utilities_frame, title_label]
	for i in things_to_destory:
		i.destroy()

#function to clear message menu
def destroy_message_menu():
	things_to_destory = [MFAQ, title_label, maker_label_msg]
	for i in things_to_destory:
		i.destroy()

#used to open a url for our message documentation
def callback(url):
	webbrowser.open_new(url)


#puts the title label on both
#the main and message menu
def start_label(name, color):
	title = StringVar()
	global title_label
	title_label = Label(root, anchor = CENTER, width=750, height=2,\
		textvariable = title, bg=color, fg="black",font=("Gill Sans", 12))
	title_label.pack_propagate(0)
	title.set(name)
	title_label.pack(side=TOP, anchor=N)

def test(frame):
	temp = Label(frame, bg="grey10", fg="green2")
	temp.pack(side=LEFT)

def message_menu():
	#message FAQs frame
	global MFAQ 
	MFAQ = Frame(root, bg="grey5", height=420)
	
	#button to go back to main menu
	back_button_font = font.Font(size=12)
	back_button = Button(title_label, bg="red", fg="black", cursor="arrow", \
		command=lambda: MainFunction(), text="←", relief=SUNKEN)
	back_button['font']=back_button_font

	#text widget to display our documentation of our messaging system
	T = Text(MFAQ, height=7, bg="grey6", fg="white", wrap=WORD, spacing2=3, font=14)
	T.insert(INSERT, "For our project we incorperated Twilio Messaging service. Twilio\
	is a programable messaging service that allows you to pruchase phone numbers. From\
	there you can incorporate the phone numbers within you code to accomplish all your messaging needs.\
	To message a non-Twilio phone number you must first register your phone with your twilio account on\
	their website. We have provided a link to Twilios HomePage below.")

	#label for our names on the GUI
	global maker_label_msg
	maker_label_msg=Label(root, bg="black", fg="red", text="a DND product")

	#link to twilio for the user to go too
	link = Label(MFAQ, text="Twilio HomePage", bg="black", fg="purple", cursor="hand2")
	
	link.bind("<Button-1>", lambda e: callback("https://www.twilio.com/what-is-cloud-communications?\
		msclkid=ebaf789cccd416ca76a219166dc54502&utm_source=bing&utm_medium=\
		cpc&utm_campaign=B_S_NAMER_Brand_Twilio&utm_term=twilio&utm_content=Twilio%20-%20Phrase") )

	MFAQ.pack(fill="both")
	T.pack(side=TOP, anchor=N)
	maker_label_msg.pack(side=RIGHT, anchor=SE)
	back_button.pack(side=LEFT, anchor=NW)
	link.pack(side=BOTTOM, anchor=S)

		

#creates the Frames of our main menu
def main_menu():
	#smoke Frame
	global smoke_frame
	smoke_frame_title = StringVar()
	smoke_frame = Frame(root, width=375, bg="grey5")
	smoke_frame_title.set("Gas Readouts")
	smoke_frame_label=Label(smoke_frame, anchor=CENTER, bd=10, bg="green yellow",\
	fg="grey5", relief="raised", textvariable=smoke_frame_title)
	smoke_frame.pack_propagate(0)
	smoke_frame.pack(side=LEFT, fill="y", expand=False)
	smoke_frame_label.pack()

	#utilities Frame
	global utilities_frame
	utilities_title = StringVar()
	utilities_frame = Frame(root, width=375, bg="dark slate gray")

	#label for our names on the GUI
	maker_label=Label(utilities_frame, bg="dark slate gray", fg="red", text="a DND product")

	#utilities frame title
	utilities_frame_label = Label(utilities_frame, bd=5, anchor=CENTER,\
		textvariable=utilities_title, bg="black", fg="tomato",\
		relief="raised")
	utilities_title.set("Utilities Menu")
	utilities_frame.pack(side=RIGHT, fill="y")
	utilities_frame_label.pack()

	
	

	#Buttons for utility frame
	msg = Button(utilities_frame, relief=RAISED, height=2, width=50, bg="mint cream",\
		text="Messages On/Off",activebackground="black", bd=10, cursor="hand2")
	detection = Button(utilities_frame, relief=RAISED, height=2, width=50, bg="mint cream",\
	 	text="Reset Detector", activebackground="black", bd=10, cursor="hand2")
	msgInfo = Button(utilities_frame, relief=RAISED, height=2, width=50,bg="mint cream",\
		command=lambda : messageFAQs(), text="More Info on Messages",\
		activebackground="black", bd=10, cursor="hand2")
	power = Button(utilities_frame, relief=RAISED, height=2, width=50,\
	 	text="Power", bg="tomato", command=lambda : quit(), activebackground="black",\
	 	bd=10, cursor="hand2")

	buttons = [msg, detection, msgInfo, power]
	for i in buttons:
		i.pack(pady=15)
	maker_label.pack(side=RIGHT, anchor=SE)

	



def loop():
	root.mainloop()


MainFunction()
