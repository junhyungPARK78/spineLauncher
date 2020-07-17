import os
import os.path
import sys
import platform
import pickle
import tkinter
import pandas

import resources.optionSetting as optionSetting
import resources.multiLanguage as multiLanguage
import resources.noFile as noFile

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

# 実行の関数
def StartSpine(spineVer):
    with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
        loadData = pickle.load(f)
    keyOfLoadData = loadData["spinePath" + thisPlatform]
    print(keyOfLoadData[:-3].replace("\"", ""))
    runningText = keyOfLoadData + " " + spineVer
    
    # ファイルの存在を確認
    try:
        with open(keyOfLoadData[:-3].replace("\"", ""), 'r'):
            pass
    except FileNotFoundError as e:
        print(languageData['text_noFile'])
        print(e)
        noFile.Main()
    except IOError as e:
        print(languageData['text_noFile'])
        print(e)
        noFile.Main()
    
    print(str(runningText))
    os.system(str(runningText))

# メインのGUIの始まり
window = tkinter.Tk()
window.title("Spine Launcher")
window.geometry("640x500+200+100")

textLabel = languageData['spineLauncher_textLabel']
textLine = "------------------------------------------------------------"
ver1 = "3.6.53"
ver2 = "3.7.94"

labelHeader = tkinter.Label(window, \
    text = textLabel, \
    pady = 3)
labelHeader.pack(side = "top")

buttonVer1 = tkinter.Button(window, \
    text = "spine "+ ver1, \
    command = lambda : StartSpine(ver1), \
    width = 30, height = 4)
buttonVer1.pack(side = "top", pady = 10)

buttonVer2 = tkinter.Button(window, \
    text = "spine "+ ver2, \
    command = lambda : StartSpine(ver2), \
    width = 30, height = 4)
buttonVer2.pack(side = "top", pady = 10)

labelLine1 = tkinter.Label(window, \
    text = textLine)
labelLine1.pack(side = "top")

buttonDefaultOption = tkinter.Button(window, \
    text = "Spine path setting", \
    command = optionSetting.Main, \
    width = 25, height = 3)
buttonDefaultOption.pack(side="top", pady = 10)

buttonLanguageOption = tkinter.Button(window, \
    text = "Select Language", \
    command = multiLanguage.Main, \
    width = 25, height = 3)
buttonLanguageOption.pack(side="top")

window.mainloop()
