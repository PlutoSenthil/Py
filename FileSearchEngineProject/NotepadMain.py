
import PySimpleGUI as sg
import pathlib
sg.ChangeLookAndFeel('BrownBlue') # change style

class NotePadGUIClass:
    def __init__(self):
        sg.ChangeLookAndFeel('BrownBlue')
        self.WIN_W = 90
        self.WIN_H = 25
        self.file = None
        self.menu_layout = [['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', 'Save As',
                             'Maximize','---', 'Exit']],
                   ['Tools', ['Word Count']],
                   ['Help', ['About']]]
        self.layout = [[sg.Menu(self.menu_layout)],
              [sg.Text('> New file <', font=('Consolas', 10), size=(self.WIN_W, 1), key='_INFO_')],
              [sg.Multiline(font=('Consolas', 12), size=(self.WIN_W,self.WIN_H), key='_BODY_')]]

        self.window = sg.Window('Notepad', layout=self.layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)

    def open_file(self,filename):
        if filename:
            file = pathlib.Path(filename)
            self.window['_BODY_'].update(value=file.read_text())
            self.window['_INFO_'].update(value=file.absolute())
            return file
        else:
            sg.popup_no_wait('File Not Found (None)')
    def save_file(self,file,values):
        '''Save file instantly if already open; otherwise use `save-as` popup'''
        if file:
            file = pathlib.Path(file)
            file.write_text(values.get('_BODY_'))
            return file
        else:
            self.save_file_as(values=values)
    def save_file_as(self,values):
        '''Save new file or save existing file with another name'''
        filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
        if filename:
            file = pathlib.Path(filename)
            file.write_text(values.get('_BODY_'))
            self.window['_INFO_'].update(value=file.absolute())
            return file
    def new_file(self):
        '''Reset body and info bar, and clear filename variable'''
        self.window['_BODY_'].update(value='')
        self.window['_INFO_'].update(value='> New File <')
        self.file = None
        return self.file

    def word_count(self,values=None):
        '''Display estimated word count'''
        words = []
        if values == None:
            for w in values['_BODY_'].split(' '):
                if w!='\n' and w not in words:
                    words.append(w)
            word_count = len(words)
            sg.popup_no_wait('Word Count: {:,d}'.format(word_count))

    def about_me(self):
        '''A short, pithy quote'''
        sg.popup_no_wait('"All great things have small beginnings" - Peter Senge')

    def NotepadMainFunction(self,file=None):
        while True:
            event, values = self.window.read()
            if event in('Exit', None):
                break
            if event in ('New (Ctrl+N)', 'n:78'):
                file = self.new_file()
            if event in ('Open (Ctrl+O)', 'o:79'):
                filename = sg.popup_get_file('Open File')
                file = self.open_file(filename=filename)
            if event in ('Save (Ctrl+S)', 's:83'):
                file=self.save_file(file=file,values=values)
            if event in ('Save As',):
                file = self.save_file_as(values=values)
            if event in ('Maximize',):
                self.window.maximize()
                self.window['_BODY_'].expand(expand_x=True, expand_y=True)
            if event in ('Word Count',):
                self.word_count(values=values)
            if event in ('About',):
                self.about_me()
        self.window.close()

def main():
    NotePadGUIClassObject =NotePadGUIClass()
    NotePadGUIClassObject.NotepadMainFunction()
def edit(file):
    NotePadGUIClassObject1 = NotePadGUIClass()
    file=NotePadGUIClassObject1.open_file(filename=file)
    NotePadGUIClassObject1.NotepadMainFunction(file=file)



