import readwrite
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")

window = sg.Window("My Todo App", layout=[[label, input_box]])
window.read()
window.close()
