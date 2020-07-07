import os
import os.path
import sys
import platform
import tkinter as tk
import resources.optionSetting

# 현재 운영체제 알아내기
thisPlatform = platform.system() # 「Darwin」은 맥이다.「Windows」는 윈도우즈.

# 세팅 파일이 있는지 확인하기
file = "./resources/settingForWindows.txt"
if os.path.exists(file):
    pass
else:
    print("개인 설정을 시작합니다.")
    resources.optionSetting.OptionSetting()







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