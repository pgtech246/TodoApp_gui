import readwrite
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My Todo App", 
                   layout=[[label], [input_box, add_button]], 
                   font=("Helvetica", 11))
window.read()
window.close()
