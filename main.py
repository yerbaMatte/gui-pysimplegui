import PySimpleGUI as pg

with open("/Users/milek/PycharmProjects/pipMindBlower/ny.txt", "r") as file:
    file_contents = file.read()

#
treedata = pg.TreeData()

rootnodes=[
   ["","MON", "Monday", 175, 150, 200],
   ["MON", "PS", "Polacy swiatu", 100, 100,100],
   ["MON", "KPP", "Kamperem po pld", 30, 20, 40],
   ["","TUE", "Tuesday", 120, 80, 125],
   ["TUE", "NN", "Nad Niemnem", 75, 55, 80],
   ["TUE", "SL", "Studio Lwow", 25, 15, 30],
   ["","WED", "Wednesday", 175, 150, 200],
   ["WED", "KZ", "Kierunek zachod", 100, 100,100],
   ["WED", "MZW", "Magazyn z wysp", 30, 20, 40],
   ["","THU", "Thursday", 120, 80, 125],
   ["THU", "SI", "Stacja innowacja", 75, 55, 80],
   ["THU", "WSCH", "Wschod", 25, 15, 30],
   ["THU", "WILN", "Wilnoteka", 25, 15, 30],
   ["","FRI", "Friday", 175, 150, 200],
   ["FRI", "PE", "Polonia express", 100, 100,100],
   ["FRI", "PA", "Przystanek ameryka", 30, 20, 40],
   ["FRI", "OP", "Ola Polonia", 30, 20, 40],
   ["","SAT", "Saturday", 120, 80, 125],
   ["SAT", "KPL", "KulturalniPL", 75, 55, 80],
   ["","SUN", "Sunday", 175, 150, 200],
   ["SUN", "POWR", "Powroty", 100, 100,100],
   ["SUN", "FP", "Fajna Polska", 30, 20, 40],
]

for row in rootnodes:
   treedata.Insert( row[0], row[1], row[2], row[3:])
tree=pg.Tree(data=treedata,
   headings=['SINGLE','MULTI'],
   auto_size_columns=True,
   select_mode=pg.TABLE_SELECT_MODE_BROWSE,
   num_rows=10,
   col0_width=5,
   key='-TREE-',
   show_expanded=False,
   enable_events=True,
   expand_x=True,
   expand_y=True,
)

week = {
    "mon" : {'kpl' : 'https://cms.tvp.pl/listing/20768432'},
    "tue": {'stw': 'https://cms.tvp.pl/listing/53261143', 'nn': 'https://cms.tvp.pl/listing/43219320'},
    "wed": {'mgzw': 'https://cms.tvp.pl/listing/29486855', 'kz': 'https://cms.tvp.pl/listing/25985428'},
    "thu": {'wilno': 'https://cms.tvp.pl/listing/19748036', 'wschod':'https://cms.tvp.pl/listing/45512868'},
    "fri": {'pe': 'https://cms.tvp.pl/listing/53451124', 'op': 'https://cms.tvp.pl/listing/53337182', 'ae': 'https://cms.tvp.pl/listing/54528538'},
    "sut": {'test': 'test', 'dwa': 'trzy'},
    "sun": {'test': 'test', 'dwa': 'trzy'}
}


#

pg.theme("Reddit")
times = 0
font = ('Helvetica', 18)
dropdown_options = [ "FULL CONTENT", "BLANK", "SINGLE"]

file_list_column = [
    [
        pg.Text("Mode", background_color='white', font=('Helvetica', 30), text_color='black'),
        pg.DropDown(dropdown_options, key="OPERATION", size=(20, 1), pad=(10,20), expand_x=True),
        pg.Button("SET", size=(15, 1))

    ],
    [
        pg.Checkbox("TITLE", key="title", default=True),
        pg.Input( expand_x=True)

    ],
    [
        pg.Checkbox("LEAD", key="lead", default=False),
        pg.Input(expand_x=True)

    ],
    [
        pg.Checkbox("PARAGRAPH", key="paragraph", default=True),
        pg.Input(expand_x=True)
    ],
    [
        pg.Checkbox("PHOTO", key="photo", default=True),
    ],
    [
        pg.Checkbox("NO EPISODE", key="noepisode", default=False),
        pg.Input(expand_x=True)
    ],
    [
        pg.Button("RUN", expand_x=True)
    ],
    [tree]
]

file_viewer_column = [
    [pg.Text("TXT", size=(50, 1))],
    [pg.Multiline(size=(70, 30), key="-TEXT-", default_text=file_contents)],
    [pg.Button("Save", expand_x=True), pg.Button("Undo", expand_x=True)],
]

console_viewer_column = [
    [pg.Text("CONSOLE", size=(50, 1))],
    [pg.Output(size=(70, 30))],
    [pg.Button("Save", expand_x=True), pg.Button("Undo", expand_x=True)],
]

tabs = [
    [pg.Tab("ny.txt", file_viewer_column)],
    [pg.Tab("console", console_viewer_column)],
]

layout = [
    [
        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.TabGroup(tabs)
    ]
]


def setMode(title, lead, paragraph, photo, noepisode):
    window['title'].update(title)
    window['lead'].update(lead)
    window['paragraph'].update(paragraph)
    window['photo'].update(photo)
    window['noepisode'].update(noepisode)


window = pg.Window("PipiMindBlower", layout, font=font)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Save":
        with open("/Users/milek/PycharmProjects/pipMindBlower/ny.txt", "w") as file:
            file.write(values["-TEXT-"])
        print(values["-TEXT-"])
    elif event == "Undo":
        window["-TEXT-"].update(file_contents)
    elif event == "SET":
        selected_value = values['OPERATION']
        if selected_value == 'FULL CONTENT':
            setMode(True,True,True,True,True)
        elif selected_value == 'BLANK':
            setMode(False,False,False,False,False)


window.close()
exit()