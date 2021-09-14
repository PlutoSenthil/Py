import NotepadMain
import subprocess
import os
import pickle
from time import process_time
import PySimpleGUI
t1_start = process_time()
PySimpleGUI.ChangeLookAndFeel('Dark')
MLINE_KEY = '-MLINE-' + PySimpleGUI.WRITE_ONLY_KEY
class GUIClass:
    def __init__(self):
        CurrentDirectory =os.path.splitdrive(os.getcwd())[0]+'/'
        self.layout=[
            [PySimpleGUI.Text('Directory Search ', size=(14, 1)),
             PySimpleGUI.Input(size=(45, 4), focus=True, key='dirSEARCHTERM_key'),
             PySimpleGUI.Radio('Contains', group_id='choice', key='dirCONTAINS_Key', default=True),
             PySimpleGUI.Radio('StartsWith', group_id='choice', key='dirSTARTSWITH_Key'),
             PySimpleGUI.Radio('EndsWith', group_id='choice', key='dirENDSWITH_Key')
             ],
            [PySimpleGUI.Text('File Search ',size=(10,1)),
             PySimpleGUI.Input(size=(45,1),focus=True,key='SEARCHTERM_key'),
            PySimpleGUI.Radio('Contains',group_id='choice',key='CONTAINS_Key',default=True),
             PySimpleGUI.Radio('StartsWith',group_id='choice',key='STARTSWITH_Key'),
            PySimpleGUI.Radio('EndsWith',group_id='choice',key='ENDSWITH_Key'),
             PySimpleGUI.Radio('FileType',group_id='choice',key='FileType_Key')
             ],
            [PySimpleGUI.Text('Root Path'),
             PySimpleGUI.Input(CurrentDirectory,size=(45,1),key='path_key'),
             PySimpleGUI.FolderBrowse('Browse'),
             PySimpleGUI.Button('Search File',size=(10,1),bind_return_key=True,key='_SEARCH_Key'),
             PySimpleGUI.Button('Search Directory', size=(14, 1), bind_return_key=True, key='dir_SEARCH_Key'),
             PySimpleGUI.Button('Clear', size=(10, 1), key='_Clear_Key'),
             PySimpleGUI.Button('Save', size=(10, 1), key='_Save_Key'),
             PySimpleGUI.Button('Load', size=(10, 1), key='_Load_Key'),
             ],[PySimpleGUI.Text('Filter'),
                PySimpleGUI.Input(size=(10, 1), key='OutputRecord_key'),
                PySimpleGUI.Text('Read/Open (give Path)'),
                PySimpleGUI.Input(size=(45, 1), key='Searchpath_key'),
                PySimpleGUI.Button('Read', size=(10, 1), key='Read_SEARCH_Key'),
                PySimpleGUI.Button('Open', size=(10, 1), key='Open_SEARCH_Key'),
                PySimpleGUI.Button('Edit', size=(10, 1), key='Edit_Notepad_key')

              ],[
                PySimpleGUI.Button('Notepad', size=(10, 1), key='_Notepad_key')
                ],
            [PySimpleGUI.Output(size=(160,30), key='_Output_Key')
             # PySimpleGUI.Output(size=(60, 30), key='_Output_Key')
             ]
        ]
        self.window=PySimpleGUI.Window('File Search Engine ').Layout(self.layout)

class SearchEngineClass:
    def __init__(self):
        self.file_index=[]
        self.directory_index=[]
        self.results=[]
        self.matches=0
        self.records=0
    def SavingIndex(self):
        #save to a pickle file]
        with open('file_index.pkl','wb') as FileOpenObject:
            pickle.dump(self.results,FileOpenObject)

    def loadExistingIndex(self):
        '''load existing index'''
        self.results.clear()
        try:
            with open('file_index.pkl','rb') as FileOpenObject:
                self.results=pickle.load(FileOpenObject)
        except:
            self.results.clear()

    def SearchDirectoryFunction(self, GUIEventValues):
        '''search for term based on search type'''
        #reset variable
        self.results.clear()
        self.directory_index.clear()
        self.matches = 0
        self.records = 0
        searchTerm= GUIEventValues['dirSEARCHTERM_key']
        root_path = GUIEventValues['path_key']
        for rootPath, directorys, files in os.walk(root_path):
            if directorys and directorys not in self.directory_index:
                self.directory_index.append((rootPath, directorys))
            # perform search
        for Path, directorys in self.directory_index:
            for directory in directorys:
                self.records += 1
                if (GUIEventValues['dirCONTAINS_Key'] and searchTerm.lower() in directory.lower()
                        or GUIEventValues['dirSTARTSWITH_Key'] and directory.lower().startswith(searchTerm.lower())
                        or GUIEventValues['dirENDSWITH_Key'] and directory.lower().endswith(searchTerm.lower())
                ):
                    result = Path.replace('\\', '/') + '/' + directory
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue
    def SearchFunction(self, GUIEventValues):
        '''search for term based on search type'''
        #reset variable
        self.results.clear()
        self.file_index.clear()
        self.matches = 0
        self.records = 0
        searchTerm= GUIEventValues['SEARCHTERM_key']
        root_path = GUIEventValues['path_key']
        for rootPath, directory, files in os.walk(root_path):
            if files and files not in self.file_index:
                self.file_index.append((rootPath, files))
        #perform search
        for Path,FileNames in self.file_index:
            for file in FileNames:
                self.records+=1
                fileWithoutType,fileType= os.path.splitext(file)[0],os.path.splitext(file)[1]
                if(GUIEventValues['CONTAINS_Key'] and searchTerm.lower() in file.lower()
                   or GUIEventValues['STARTSWITH_Key'] and fileWithoutType.lower().startswith(searchTerm.lower())
                   or GUIEventValues['ENDSWITH_Key'] and fileWithoutType.lower().endswith(searchTerm.lower())
                   or GUIEventValues['FileType_Key'] and fileType.lower()== searchTerm.lower()
                ):
                    result=Path.replace('\\','/')+'/'+file
                    self.results.append(result)
                    self.matches+=1
                else:
                    continue

def main():
    GUIClassObject = GUIClass()
    SearchEngineClassObject = SearchEngineClass()
    while True:
        Events, Values = GUIClassObject.window.Read()
        print(Events, Values)
        if Events == "Exit" or Events == PySimpleGUI.WIN_CLOSED:
            break
        if Events =='_Save_Key':
            SearchEngineClassObject.SavingIndex()
            print('>>Save Successfully')
        if Events =='_Load_Key':
            index = 0
            SearchEngineClassObject.loadExistingIndex()
            if SearchEngineClassObject.results:
                for match in SearchEngineClassObject.results:
                    print(">>"+str(index+1)+" "+ match + "\n")
                    index += 1
            else:
                print('No Result\n')
            print('>>>Loaded Successfully')
        if Events == '_Clear_Key':
            GUIClassObject.window['_Output_Key'].update(value='')
            GUIClassObject.window['OutputRecord_key'].update(value=-1)
            GUIClassObject.window['SEARCHTERM_key'].update(value='')
            GUIClassObject.window['Searchpath_key'].update(value='')

        if Events=='_SEARCH_Key':
            SearchEngineClassObject.SearchFunction(Values)
            print('Root Path '+Values['path_key'])
            print('\n>> {:,d} matchs out of {:,d} records'.format(SearchEngineClassObject.matches,
                                                                SearchEngineClassObject.records))
            print('File\'s You Searched: '+Values['SEARCHTERM_key'] +'\n')
            index=0
            Filter=Values['OutputRecord_key']
            Filter=-1 if Filter=='' else int(Filter)
            if SearchEngineClassObject.results:
                for match in SearchEngineClassObject.results:
                    if index==Filter:
                        break
                    print(">>"+str(index+1)+" "+ match + "\n")
                    index+=1

            else:
                print('>>Not Found\n')
        if Events == 'Read_SEARCH_Key':
            GUIClassObject.window['_Output_Key'].update(value='')
            if os.path.isfile(Values['Searchpath_key']):
                FileOpen = open(Values['Searchpath_key'], 'r')
                Fileresult=FileOpen.read()
                FileOpen.close()
                print(Fileresult)
            else:
                print('It is Directory Path ,give file Path')
        if Events == 'Open_SEARCH_Key':
            FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            path = os.path.normpath(Values['Searchpath_key'])
            if os.path.isdir(path):
                subprocess.run([FILEBROWSER_PATH, path])
            elif os.path.isfile(path):
                subprocess.run([FILEBROWSER_PATH,'/select,',path])
        if Events=='_Notepad_key':
            NotepadMain.main()
        if Events=='Edit_Notepad_key':
            NotepadMain.edit(file=Values['Searchpath_key'])
        if Events=='dir_SEARCH_Key':
            SearchEngineClassObject.SearchDirectoryFunction(Values)
            print('Root Path '+Values['path_key'])
            print('\n>> {:,d} matchs out of {:,d} records'.format(SearchEngineClassObject.matches,
                                                                SearchEngineClassObject.records))
            print('Directory\'s You Searched: '+Values['dirSEARCHTERM_key'] +'\n')
            index=0
            Filter=Values['OutputRecord_key']
            Filter=-1 if Filter=='' else int(Filter)
            if SearchEngineClassObject.results:
                for match in SearchEngineClassObject.results:
                    if index==Filter:
                        break
                    print(">>"+str(index+1)+" "+ match + "\n")
                    index+=1

            else:
                print('>>Not Found\n')


    GUIClassObject.window.close()

main()
