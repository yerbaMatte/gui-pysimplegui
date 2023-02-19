import PySimpleGUI as pg

with open("/Users/milek/PycharmProjects/pipMindBlower/ny.txt", "r") as file:
    file_contents = file.read()
# ////////////////


data = {
    'Monday': {
        'Polacy swiatu': {'Single': 'https://cms.tvp.pl/listing/55650523'},
        'Kamperem po pld': {'Single': 'https://cms.tvp.pl/listing/60328558'},
    },
    'Tuesday': {
        'Nad Niemnem': {'Multi': 'https://cms.tvp.pl/listing/43219320'},
        'Studio Lwow': {'Single': 'https://cms.tvp.pl/listing/49597795', 'Multi': 'https://cms.tvp.pl/listing/53261143'},
    },
    'Wednesday': {
        'Kierunek zachod': {'Single': 'https://cms.tvp.pl/listing/36741898', 'Multi': 'https://cms.tvp.pl/listing/25985428'},
        'Magazyn z wysp': {'Single': 'https://cms.tvp.pl/listing/29473547', 'Multi': 'https://cms.tvp.pl/listing/29486855'},
    },
    'Thursday': {
        'Stacja innowacja': {'Single': 'https://cms.tvp.pl/listing/49597789'},
        'Wschod': {'Single': 'https://cms.tvp.pl/listing/45512868'},
        'Wilnoteka': {'Multi': 'https://cms.tvp.pl/listing/19748036'}
    },
    'Friday': {
        'Polonia express': {'Single': 'https://cms.tvp.pl/listing/49597817', 'Multi': 'https://cms.tvp.pl/listing/53451124'},
        'Przystanek ameryka': {'Single': 'https://cms.tvp.pl/listing/45742428'},
        'Ola Polonia': {'Single': 'https://cms.tvp.pl/listing/50566544', 'Multi': 'https://cms.tvp.pl/listing/53337182'}
    },
    'Saturday': {
        'KulturalniPL': {'Multi': 'https://cms.tvp.pl/listing/20768432'},
    },
    'Sunday': {
        'Powroty': {'Single': 'https://cms.tvp.pl/listing/47439908'},
        'Fajna Polska': {'Single': 'https://cms.tvp.pl/listing/65539809'},
    },
}

data_choices = list(data.keys())


# ////////////////
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
    [pg.Text('Select a category:')],
    [pg.Listbox(data_choices, size=(15, 8), expand_x=True, key='-WEEK-', enable_events=True),
     pg.Listbox([], size=(15, 8), expand_x=True, key='-DAY-', enable_events=True),
     pg.Listbox([], size=(15, 8), expand_x=True, key='-PROGRAMME-', enable_events=True)],
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
    elif event == '-WEEK-':
        selected_day = values['-WEEK-'][0]
        window['-DAY-'].update(data[selected_day])
    elif event == '-DAY-':
        selected_option = values['-DAY-'][0]
        window['-PROGRAMME-'].update(data[selected_day][selected_option])
    elif event == '-PROGRAMME-':
        selected_kind = values['-PROGRAMME-'][0]
        print(f'{selected_option} | {selected_kind} | {data[selected_day][selected_option][selected_kind]}')
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