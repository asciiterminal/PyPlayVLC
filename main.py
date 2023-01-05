import PySimpleGUI as sg
import webbrowser

layout = [[sg.Text('Enter the file path of the video:')],
          [sg.Input(key='filepath')],
          [sg.Button('Browse'), sg.Button('Play'), sg.Button('Pause'), sg.Button('Stop')],
          [sg.Text(size=(40,1), key='output')]]

window = sg.Window('Video Player', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Stop'):
        break
    if event == 'Browse':
        filepath = sg.popup_get_file('Choose a video file')
        if filepath:
            window['filepath'].update(filepath)
    if event == 'Play':
        webbrowser.open(values['filepath'])
        window['output'].update('Playing video...')
    if event == 'Pause':
        window['output'].update('Video paused.')

window.close()
