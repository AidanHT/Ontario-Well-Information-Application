from tkinter import *
from tkinter.font import Font
import random
 
##Clears and resets all widgets in the "Add Well" LabelFrame to its original values
def clearButton():
   locationAddWellVar.set("")
   typeAddWellSpin.config(bg=azureBlue)
   typeAddWellVar.set("Municipal")
   depthAddWellVar.set(0)
   depthAddWellScale.config(troughcolor=blue)
   GPMAddWellVar.set(0)
   GPMAddWellScale.config(troughcolor=blue)
   ClayVar.set("F")
   GravelVar.set("F")
   LoamVar.set("F")
   LimestoneVar.set("F")
   SandVar.set("F")
   ShaleVar.set("F")

##gets user input to create a new well with the location, type, depth and GPM names, location name will be displayed in the listbox 
def addButton():
   locationName = locationAddWellVar.get()
   typeName = typeAddWellVar.get()
   depthName = depthAddWellVar.get()
   GPMName = GPMAddWellVar.get()
 
   if locationName != "" and locationName not in location_list:
       location_list.append(locationName)
       locationVar.set(location_list)
 
       locationListbox.selection_clear(0, len(location_list))
       locationListbox.selection_set(len(location_list) - 1)
 
       type_list.append(typeName)
       depth_list.append(depthName)
       gpm_list.append(GPMName)
 
       soil = ClayVar.get() + GravelVar.get() + LoamVar.get() + LimestoneVar.get() + SandVar.get() + ShaleVar.get()
       soil_list.append(soil)
       
       todo_listbox.selection_set(len(location_list)-1)
       
   clearButton()
 
##retrieves details and data of selected well from the listbox
def retrieveButton():
   index = locationListbox.curselection()[0]
 
   locationDetailsVar.set(f'{location_list[index]}')
   typeDetailsVar.set(f'Type: {type_list[index]}')
   depthDetailsVar.set(f'Depth: {depth_list[index]} ft.')
   GPMDetailsVar.set(f'GPM: {gpm_list[index]}')
 
   soil = ""
 
   soils = soil_list[index]
 
   for i in range(0, len(soils)):
       if soils[i] == "T":
           soil += f' {soil_legend[i]}'
 
   soilDetailsVar.set(f'Soil: {soil}')

   detailsFrame.config(bg = lightBeige)
   typeDetailsLabel.config(bg = lightBeige)
   depthDetailsLabel.config(bg = lightBeige)
   GPMDetailsLabel.config(bg = lightBeige)
   locationDetailsLabel.config(bg = lightBeige)
   soilDetailsLabel.config(bg = lightBeige)
   locationDetailsLabel.config(fg=rgbColors[index])

 
##removes selected well from listbox and all information connected to the well 
def removeButton():
   index = locationListbox.curselection()[0]
 
   location_list.pop(index)
   locationVar.set(location_list)
   type_list.pop(index)
   gpm_list.pop(index)
   soil_list.pop(index)
   depth_list.pop(index)

##changes in spinbox based on type of well selected by user 
def typeSpinColor():
   type = typeAddWellVar.get()
 
   if type == "Domestic":
       typeAddWellSpin.config(bg = "#ff2f8e")
   elif type == "Agricultural":
       typeAddWellSpin.config(bg="#ff9e4c")
   elif type == "Industrial":
       typeAddWellSpin.config(bg="#ffd600")
   elif type == "Commercial":
       typeAddWellSpin.config(bg="#66df48")
   elif type == "Municipal":
       typeAddWellSpin.config(bg=azureBlue)
   else:
       typeAddWellSpin.config(bg="#9803ce")

##changes color of trough in the scale based on value
def depthColor(ignore):
   depth = depthAddWellVar.get()
 
   green = round(depth * 203 / 500) + 1
   blue = round(depth * 110/500) + 129
   red = round(depth * 83/500)
   rgb = (f'#{red:02x}{green:02x}{blue:02x}')
 
   depthAddWellScale.config(troughcolor=rgb)

##changes color of GPM in the scale based on value
def GPMColor(ignore):
   GPM = GPMAddWellVar.get()
 
   green = round(GPM * 203 / 600) + 1
   blue = round(GPM * 110 / 600) + 129
   red = round(GPM * 83 / 600)
   rgb = (f'#{red:02x}{green:02x}{blue:02x}')
 
   GPMAddWellScale.config(troughcolor=rgb)

##creates color for each listbox item and displays that color in the title
def listboxSelectBackgroundColor(event):
    for location in location_list:
        red = random.randint(0, 20)
        green = random.randint(0, 150)
        blue = random.randint(150, 255)

        rgb = (f'#{red:02x}{green:02x}{blue:02x}')

        rgbColors.append(rgb)
        
    index = locationListbox.curselection()[0]
    locationListbox.config(selectbackground=rgbColors[index])    
    
 
# MAIN
global location_list, type_list, depth_list, gpm_list, soil_list, rgbColors
location_list = ['GUELPH CITY', 'GUELPH DIV E01 005', 'SCUGOG 08 022', 'TORONTO 121 Industry', 'Halton NS01 005',
                'SOUTH DUMFRIES 02 017', 'BINBROOK BL303 004']
type_list = ['Municipal', 'Municipal', 'Domestic', 'Industrial', 'Domestic', 'Domestic', 'Domestic']
depth_list = [241, 265, 224, 11, 52, 152, 80]
gpm_list = [541, 151, 10, 0, 15, 20, 3]
# soil legend: Clay, Gravel, Loam, Limestone, Sand, Shale
soil_legend = ['Clay', 'Gravel', 'Loam', 'Limestone', 'Sand', 'Shale']
soil_list = ['FTTFTT', 'TTTTFF', 'TTTFTF', 'FFTFTF', 'TTFFFF', 'TFTFFF', 'TFFTFF']
rgbColors = []

# Create widgets
root = Tk()
mainframe = Frame(root)
 
GothamLightFont = Font(family='Gotham-book', size=9)
GothamBoldFont = Font(family='Gotham-bold', size=12)
GothamExtraBoldFont = Font(family='Gotham-bold', size=16)
 
beige = "#FFE6B6"
lightBeige = "#FFF7D9"
lightBlue = "#53CCEC"
azureBlue = "#1974D3"
blue = "#000181"
 
root.config(bg=beige)
mainframe.config(bg=beige)
 
# Title
root.title("Ontario Water Supply Well Information Application")
titleLabel = Label(mainframe, text="Ontario Water Supply Well Information Application", font = GothamExtraBoldFont,\
                   bg=beige, fg = blue)
 
##Well Location Label and Listbox
locationFrame = LabelFrame(mainframe, text="Well Locations", font=GothamBoldFont, bg=beige)
 
locationVar = StringVar()
locationVar.set(location_list)
locationListbox = Listbox(locationFrame, listvariable=locationVar, selectmode=SINGLE, font=GothamLightFont,
                         bg=lightBeige, relief = "flat", highlightcolor=azureBlue)
locationListbox.bind('<<ListboxSelect>>', listboxSelectBackgroundColor)
 
##Details labelframe, labels and checkbuttons
detailsFrame = LabelFrame(mainframe, text="Details", font=GothamBoldFont, bg=beige)
 
locationDetailsVar = StringVar()
locationDetailsVar.set("Location")
locationDetailsLabel = Label(detailsFrame, textvariable=locationDetailsVar, font=GothamLightFont, bg=beige)
 
typeDetailsVar = StringVar()
typeDetailsVar.set("Type:")
typeDetailsLabel = Label(detailsFrame, textvariable=typeDetailsVar, font=GothamLightFont, bg=beige)
 
depthDetailsVar = StringVar()
depthDetailsVar.set("Depth:")
depthDetailsLabel = Label(detailsFrame, textvariable=depthDetailsVar, font=GothamLightFont, bg=beige)
 
GPMDetailsVar = StringVar()
GPMDetailsVar.set("GPM:")
GPMDetailsLabel = Label(detailsFrame, textvariable=GPMDetailsVar, font=GothamLightFont, bg=beige)
 
soilDetailsVar = StringVar()
soilDetailsVar.set("Soil:")
soilDetailsLabel = Label(detailsFrame, textvariable=soilDetailsVar, font=GothamLightFont, bg=beige)
 
##Add Well labelframe, entry, scale, checkbuttons and button
 
addWellFrame = LabelFrame(mainframe, text="Add Well", font=GothamBoldFont, bg=beige)
 
locationAddWellLabel = Label(addWellFrame, text="Location Name:", bg=beige)
 
locationAddWellVar = StringVar()
locationAddWellEntry = Entry(addWellFrame, textvariable=locationAddWellVar, font=GothamLightFont, bg=lightBeige)
 
typeAddWellLabel = Label(addWellFrame, text="Type:", font=GothamLightFont, bg=beige)
 
typeList = ["Domestic", "Agricultural", "Industrial", "Commercial", "Municipal", "Dewatering"]
typeAddWellVar = StringVar()
typeAddWellSpin = Spinbox(addWellFrame, textvariable=typeAddWellVar, values=typeList, font=GothamLightFont,\
                         bg =azureBlue, command=typeSpinColor)
typeAddWellVar.set("Municipal")
 
depthAddWellVar = IntVar()
depthAddWellScale = Scale(addWellFrame, from_=0, to=500, variable=depthAddWellVar, orient=HORIZONTAL, label="Depth",\
                         font=GothamLightFont, bg=beige, troughcolor=blue,command=depthColor)
 
GPMAddWellVar = IntVar()
GPMAddWellScale = Scale(addWellFrame, from_=0, to=600, variable=GPMAddWellVar, orient=HORIZONTAL, label="GPM",\
                       font=GothamLightFont, bg=beige, troughcolor=blue, command=GPMColor)
 
soilAddWellLabel = Label(addWellFrame, text="Soil", font=GothamLightFont, bg=beige)
 
ClayVar = StringVar()
ClayVar.set("F")
ClayCheck = Checkbutton(addWellFrame, text="Clay", variable=ClayVar, onvalue="T", offvalue="F", font=GothamLightFont,\
                       bg=beige, selectcolor=lightBlue)
 
GravelVar = StringVar()
GravelVar.set("F")
GravelCheck = Checkbutton(addWellFrame, text="Gravel", variable=GravelVar, onvalue="T", offvalue="F",\
                         font=GothamLightFont, bg=beige, selectcolor=lightBlue)
 
LoamVar = StringVar()
LoamVar.set("F")
LoamCheck = Checkbutton(addWellFrame, text="Loam", variable=LoamVar, onvalue="T", offvalue="F", font=GothamLightFont,\
                       bg=beige, selectcolor=lightBlue)
 
LimestoneVar = StringVar()
LimestoneVar.set("F")
LimestoneCheck = Checkbutton(addWellFrame, text="Limestone", variable=LimestoneVar, onvalue="T", offvalue="F",\
                            font=GothamLightFont, bg=beige, selectcolor=lightBlue)
 
SandVar = StringVar()
SandVar.set("F")
SandCheck = Checkbutton(addWellFrame, text="Sand", variable=SandVar, onvalue="T", offvalue="F", font=GothamLightFont,\
                       bg=beige, selectcolor=lightBlue)
 
ShaleVar = StringVar()
ShaleVar.set("F")
ShaleCheck = Checkbutton(addWellFrame, text="Shale", variable=ShaleVar, onvalue="T", offvalue="F", font=GothamLightFont,\
                        bg=beige, selectcolor=lightBlue)
 
addWellButton = Button(addWellFrame, text="ADD", width=30, command=addButton, font=GothamLightFont, bg=azureBlue)
 
ClearWellButton = Button(addWellFrame, text="Clear", width=30, command=clearButton, font=GothamLightFont, bg=azureBlue)
 
DeleteWellButton = Button(mainframe, text="Delete Selected Well", width=31, command=removeButton, font=GothamLightFont,\
                         bg=lightBlue)
 
RetrieveDetailsButton = Button(mainframe, text="Retrieve Well Details", width=31, command=retrieveButton,\
                              font=GothamLightFont, bg=lightBlue)
 
# Grid widgets
mainframe.grid(padx=100, pady=100)
 
titleLabel.grid(row=1, column=1, columnspan=2)
 
locationFrame.grid(row=2, column=1, sticky=W, padx=10, pady=10)
locationListbox.grid(row=1, column=1, ipady=58, padx=10, ipadx=25, pady=10)
 
detailsFrame.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky=W)
 
locationDetailsLabel.grid(row=1, column=1, columnspan=2, sticky=W)
typeDetailsLabel.grid(row=2, column=1, columnspan=2, sticky=W)
depthDetailsLabel.grid(row=3, column=1, sticky=W)
GPMDetailsLabel.grid(row=3, column=2, padx=10,sticky=W)
soilDetailsLabel.grid(row=4, column=1, columnspan=2, sticky=W)
 
addWellFrame.grid(row=2, column=2)
locationAddWellLabel.grid(row=1, column=1, columnspan=2, padx=10, sticky=W)
locationAddWellEntry.grid(row=2, column=1, columnspan=2, padx=10, sticky=W)
typeAddWellLabel.grid(row=3, column=1, columnspan=2, padx=10, sticky=W)
typeAddWellSpin.grid(row=4, column=1, columnspan=2, padx=10, sticky=W)
depthAddWellScale.grid(row=5, column=1, padx=7)
GPMAddWellScale.grid(row=5, column=2, padx=7)
soilAddWellLabel.grid(row=6, column=1, sticky=W, padx=10)
 
ClayCheck.grid(row=7, column=1, sticky=W, padx=10)
GravelCheck.grid(row=8, column=1, sticky=W, padx=10)
LoamCheck.grid(row=9, column=1, sticky=W, padx=10)
LimestoneCheck.grid(row=7, column=2, sticky=W, padx=5)
SandCheck.grid(row=8, column=2, sticky=W, padx=5)
ShaleCheck.grid(row=9, column=2, sticky=W, padx=5)
 
addWellButton.grid(row=10, column=1, columnspan=2)
ClearWellButton.grid(row=11, column=1, columnspan=2, pady=10)
DeleteWellButton.grid(row=3, column=1, padx=10, pady=10, sticky=W)
RetrieveDetailsButton.grid(row=3, column=2, pady=10)
# for some students
root.mainloop()
 
 
 


