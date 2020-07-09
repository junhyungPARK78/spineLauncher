import os
import os.path
import sys
import platform
import tkinter

import resources.optionSetting as optionSetting

# 현재 운영체제 알아내기
thisPlatform = platform.system() # 「Darwin」은 맥이다.「Windows」는 윈도우즈.

# 실행 함수 TEST
def TEST(spineVer):
    print(f"asdf {spineVer}")

# 메인 GUI 시작
window = tkinter.Tk()
window.title("Spine Launcher")
window.geometry("640x420+200+100")

textLabel = """
------------------------------------------------------------
실행할 스파인 버전의 버튼을 눌러주세요.

스파인이 설치되어 있는 경로를 수정하고 싶은 경우에는
'Spine path setting' 버튼을 눌러주세요.
------------------------------------------------------------"""
textLine = "------------------------------------------------------------"
ver1 = "3.6.53"
ver2 = "3.7.94"

labelHeader = tkinter.Label(window, \
    text = textLabel, \
    pady = 3)
labelHeader.pack(side = "top")

buttonVer1 = tkinter.Button(window, \
    text = "spine "+ ver1, \
    width = 30, height = 4)
buttonVer1.pack(side = "top", pady = 10)

buttonVer2 = tkinter.Button(window, \
    text = "spine "+ ver2, \
    width = 30, height = 4)
buttonVer2.pack(side = "top", pady = 10)

labelLine1 = tkinter.Label(window, \
    text = textLine)
labelLine1.pack(side = "top")

buttonDefaultOption = tkinter.Button(window, \
    text = "Spine path setting", \
    command = optionSetting.Main, \
    width = 25, height = 3)
buttonDefaultOption.pack(side="top", pady = 30)

window.mainloop()




# # 이때까지 모인 정보로 spine 실행시키기
# start = "/Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53"
# # “C:\Program Files (x86)\Spine\Spine.exe” -u 3.6.53
# # /Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53
# os.system(start)
