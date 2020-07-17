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

    def OptionOkClick(): # 【関数】設定のファイルを作る

        # セーブファイルを作る（Windows）
        if thisPlatform == "Windows":
            with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path オプションのセーブの文言を作る
                spinePathInput = entryOptionInput.get()
                if spinePathInput[0] == "\"":
                    spinePathInput = spinePathInput[1:]
                if spinePathInput[-1] == "\"":
                    spinePathInput = spinePathInput[:-1]
                if os.path.basename(spinePathInput) == "Spine.exe":
                    spinePathInput = os.path.dirname(spinePathInput)
                spinePathInput = "\"" + spinePathInput + "\\Spine.exe\" -u"
                spinePathDictionary["spinePathWindows"] = spinePathInput

                # セーブファイルを作る
                with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        # セーブファイルを作る（Mac）
        if thisPlatform == "Darwin":
            with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path オプションのセーブの文言を作る
                spinePathInput = entryOptionInput.get()
                if spinePathInput[-1] == "\\":
                    spinePathInput = spinePathInput[:-1]
                spinePathInput = spinePathInput + " -u"
                spinePathDictionary["spinePathDarwin"] = spinePathInput

                # セーブファイルを作る
                with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        window.destroy()

        return
    
    # 設定をデフォルトに戻す
    def SetDefault():
        defaultSettingDictionary = {}

        with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
            loadData = pickle.load(f)
            loadData['spinePathWindows'] = '“C:\\Program Files (x86)\\Spine\\Spine.exe” -u'
            loadData['spinePathDarwin'] = '/Applications/Spine/Spine.app/Contents/MacOS/Spine -u'
            defaultSettingDictionary = loadData

        with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
            pickle.dump(defaultSettingDictionary, f)
            print(defaultSettingDictionary)
        
        window.destroy()

    window = tk.Tk()
    window.title("Option")
    window.geometry("500x420+300+200")

    textHead = languageData['optionSetting_textHead']
    
    textLine = "------------------------------------------------------------"
    
    textDefault = languageData['optionSetting_textDefault']

    labelOptionComment1 = tk.Label(window, \
        text = textHead)
    labelOptionComment1.pack()
        
    entryOptionInput = tk.Entry(window, \
        justify = "right", \
        width = 40)
    entryOptionInput.pack()

    buttonOk = tk.Button(window, \
        text = "OK", \
        command = OptionOkClick, \
        width = 30, height = 3)
    buttonOk.pack()

    labelOptionComment2 = tk.Label(window, \
        text = textLine)
    labelOptionComment2.pack()

    labelOptionComment3 = tk.Label(window, \
        text = textDefault)
    labelOptionComment3.pack()

    buttonDefaultOption = tk.Button(window, \
        text = "Default", \
        command = SetDefault, \
        width = 20, height = 2)
    buttonDefaultOption.pack()

    labelOptionComment4 = tk.Label(window, \
        text = textLine)
    labelOptionComment4.pack()

    window.mainloop()

if __name__ == '__main__':
    Main()
