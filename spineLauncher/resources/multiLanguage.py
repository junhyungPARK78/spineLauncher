import os
import sys
import platform
import pickle
import pandas
import tkinter as tk

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import spineLauncher

def Main(): # 【関数】設定ファイル用のGUI
    resourcesFolder = os.path.abspath("resources") # resources フォルダーの経路
    settingSaveFile = "settingSave.bin" # 設定のセーブのファイル

    def SelectJapanese():
        defaultSettingDictionary = {}

        with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
            loadData = pickle.load(f)
            loadData['language'] = '1'
            defaultSettingDictionary = loadData

        with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
            pickle.dump(defaultSettingDictionary, f)            
        
        window.destroy()

    def SelectKorean():
        defaultSettingDictionary = {}

        with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
            loadData = pickle.load(f)
            loadData['language'] = '2'
            defaultSettingDictionary = loadData

        with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
            pickle.dump(defaultSettingDictionary, f)
        
        window.destroy()

    window = tk.Tk()
    window.title("Option")
    window.geometry("480x480+300+200")
    window.resizable(False, False)

    textLabel = spineLauncher.languageData['multiLanguage_textLabel']

    labelOptionComment1 = tk.Label(window, \
        text = textLabel)
    labelOptionComment1.pack()

    buttonSelectJapanese = tk.Button(window, \
        text = "日本語", \
        command = SelectJapanese, \
        width = 20, height = 2, pady = 10)
    buttonSelectJapanese.pack(pady = 10)

    buttonSelectKorean = tk.Button(window, \
        text = "한국어", \
        command = SelectKorean, \
        width = 20, height = 2, pady = 10)
    buttonSelectKorean.pack(pady = 10)

    window.mainloop()

if __name__ == '__main__':
    Main()
