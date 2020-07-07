import os
import os.path
import sys
import platform
import tkinter

import resources.optionSetting

# 현재 운영체제 알아내기
thisPlatform = platform.system() # 「Darwin」은 맥이다.「Windows」는 윈도우즈.

# 세팅 파일이 있는지 확인하기
file = "./resources/settingForWindows.txt"
if os.path.exists(file):
    pass
else:
    resources.optionSetting.OptionSetting()

window = tkinter.Tk()
window.title("Spine Launcher")
window.geometry("600x400+200+100")

labelText = """
------------------------------------------------------------
실행할 스파인 버전의 버튼을 눌러주세요.

스파인이 설치되어 있는 경로를 수정하고 싶은 경우에는
'Spine path setting' 버튼을 눌러주세요.
------------------------------------------------------------"""

label = tkinter.Label(window, text = labelText, pady = 3)
label.pack(side = "top")

btnVer1 = tkinter.Button(window, text = "spine 3.6.53", width = 25, height = 3)
btnVer1.pack(side = "top", pady = 10)

btnVer2 = tkinter.Button(window, text = "spine 3.7.94", width = 25, height = 3)
btnVer2.pack(side = "top", pady = 10)

btnOption = tkinter.Button(window, text = "Spine path setting", width = 20, height = 3)
btnOption.pack(side="bottom", padx = 100, pady = 20, anchor = "e")

window.mainloop()





# # 버전 선택하기
# spineVersionInput = input("spine의 버전을 입력해주세요. : ")
# print(spineVersionInput)

# # 이때까지 모인 정보로 spine 실행시키기
# start = "/Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53"
# # “C:\Program Files (x86)\Spine\Spine.exe” -u 3.6.53
# # /Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53
# os.system(start)

# UX 만들기
# # 옵션 GUI 업그레이드하기
# # 본체 GUI 업그레이드하기
# # 윈도우즈에서 spine이 실행이 되지 않을 때는 「resources/settingForWindows.txt」를 삭제하고 다시 실행시키십시오.