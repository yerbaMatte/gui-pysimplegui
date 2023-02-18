import PySimpleGUI as pg

with open("/Users/milek/PycharmProjects/pipMindBlower/ny.txt", "r") as file:
    file_contents = file.read()
# Step 1: Set theme
pg.theme("default1")

dropdown_options = [ "FULL CONTENT", "BLANK", "SINGLE"]

options = ["Option 1", "Option 2", "Option 3"]

file_list_column = [
    [
        pg.Text("Mode", background_color='white', font='black', text_color='black'),
        pg.DropDown(dropdown_options, key="OPERATION", size=(20, 1), pad=(10,20)),
        pg.Button("SET", size=(15, 1))

    ],
    [
        pg.Checkbox("TITLE", key="title", default=True),
    ],
    [
        pg.Checkbox("LEAD", key="lead", default=False),
    ],
    [
        pg.Checkbox("PARAGRAPH", key="paragraph", default=True),
    ],
    [
        pg.Checkbox("PHOTO", key="photo", default=True),
    ],
    [
        pg.Checkbox("NO EPISODE", key="noepisode", default=False),
    ],
    [
        pg.Button("RUN", expand_x=True)
    ],
]

file_viewer_column = [
    [pg.Text("TXT", size=(50, 1))],
    [pg.Multiline(size=(70, 30), key="-TEXT-", default_text=file_contents)],
    [pg.Button("Save", expand_x=True), pg.Button("Undo", expand_x=True), ],
]

layout = [
    [
        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.Column(file_viewer_column)
    ]
]
# Step 3: Create Window
window = pg.Window("PipiMindBlower", layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Save":
        with open("/Users/milek/PycharmProjects/pipMindBlower/ny.txt", "w") as file:
            file.write(values["-TEXT-"])
    elif event == "Undo":
        window["-TEXT-"].update(file_contents)
    elif event == "SET":
        selected_value = values['OPERATION']
        if selected_value == 'FULL CONTENT':
            window['lead'].update(True)
            window['noepisode'].update(False)
        elif selected_value == 'BLANK':
            window['noepisode'].update(False)
            window['title'].update(False)
            window['paragraph'].update(False)
            window['paragraph'].update(False)
            window['photo'].update(False)






window.close()
exit()