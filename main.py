import readwrite as rw
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=rw.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label], 
          [input_box, add_button], 
          [list_box, edit_button, complete_button], 
          [exit_button]]

window = sg.Window("My Todo App", 
                   layout= layout, 
                   font=("Helvetica", 11))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])
    match event:
        case "Add":
            todos = rw.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            rw.write_todos(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = rw.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            rw.write_todos(todos)
            window["todos"].update(values=todos)
        
        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
