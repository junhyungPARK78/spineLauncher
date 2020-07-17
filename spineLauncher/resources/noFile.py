import os
import platform
import pickle
import pandas
import tkinter as tk

import resources.optionSetting as optionSetting

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

def Main(): # 【関数】指定されたフォルダーにspineの実行ファイルがない場合の処理
    window = tk.Tk()
    window.title("ERROR")
    window.geometry("500x200+300+300")

    textError = languageData['noFile_textError']

    messageError = tk.Message(window, \
        anchor = "center", \
        text = textError, \
        width = 400, \
        padx = 20, \
        pady = 20)
    messageError.pack()

    buttonOK = tk.Button(window, \
        text = "OK", \
        command = lambda : ClickOK(), \
        width = 20, height = 2)
    buttonOK.pack(pady = 10)

    def ClickOK():
        window.destroy()

    window.mainloop()



if __name__ == '__main__':
    Main()
