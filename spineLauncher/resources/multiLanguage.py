import os
import platform
import pickle
import pandas
import tkinter as tk

# 現在のオペレーティングシステム調べる
thisPlatform = platform.system() # 「Darwin」：Mac、「Windows」：windows。

resourcesFolder = os.path.abspath("resources") # resources フォルダーの経路
settingSaveFile = "settingSave.bin" # 設定のセーブのファイル
multiLanguageCsvFile = "multiLanguageCsvFile.csv" # 言語別のデータが入っているcsvファイル

csvData = pandas.read_csv(os.path.join(resourcesFolder, multiLanguageCsvFile), header = None)
languageData = {}
selectLanguage = ''

with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
    loadData = pickle.load(f)
    selectLanguage = loadData['language']

for i in range(len(csvData)):
    languageData[csvData[0][i]] = csvData[int(selectLanguage)][i]

print(languageData)

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
            print(defaultSettingDictionary)
        
        window.destroy()

    def SelectKorean():
        defaultSettingDictionary = {}

        with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
            loadData = pickle.load(f)
            loadData['language'] = '2'
            defaultSettingDictionary = loadData

        with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
            pickle.dump(defaultSettingDictionary, f)
            print(defaultSettingDictionary)
        
        window.destroy()

    window = tk.Tk()
    window.title("Option")
    window.geometry("480x480+300+200")
    window.resizable(False, False)

    textLabel = languageData['multiLanguage_textLabel']

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





    # window.title("Option")
    # window.geometry("500x420+300+200")

    # textHead = """
    # ----------------------------------------------------------------------
    # オプションを修正します。
    # ----------------------------------------------------------------------

    # ------------------------------------------------------------
    # spineの設置のフォルダーをお入力してください。："""
    
    # textLine = "------------------------------------------------------------"
    
    # textDefault = """
    # ------------------------------------------------------------
    # オプションをデフォルトに戻します。"""

    # labelOptionComment1 = tk.Label(window, \
    #     text = textHead)
    # labelOptionComment1.pack()
        
    # entryOptionInput = tk.Entry(window, \
    #     justify = "right", \
    #     width = 40)
    # entryOptionInput.pack()

    # buttonOk = tk.Button(window, \
    #     text = "OK", \
    #     command = OptionOkClick, \
    #     width = 30, height = 3)
    # buttonOk.pack()

    # labelOptionComment2 = tk.Label(window, \
    #     text = textLine)
    # labelOptionComment2.pack()

    # labelOptionComment3 = tk.Label(window, \
    #     text = textDefault)
    # labelOptionComment3.pack()

    # buttonDefaultOption = tk.Button(window, \
    #     text = "Default", \
    #     command = SetDefault, \
    #     width = 20, height = 2)
    # buttonDefaultOption.pack()

    # labelOptionComment4 = tk.Label(window, \
    #     text = textLine)
    # labelOptionComment4.pack()

    # window.mainloop()

if __name__ == '__main__':
    Main()
