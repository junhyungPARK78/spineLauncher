import pickle

list1 = {}

for i in range(1000):
    list1[i] = "asdfasdfasdfasdfasdf"

with open("./resources/testSave.txt", "wb") as f:
    pickle.dump(list1, f)

with open("./resources/testSave.txt", "rb") as f:
    data = pickle.load(f)

print(data)
print(data[2])

"""
- 덧이어서 쓰는 모드는 없었다. 읽어들여서 편집한 후에, 다시 싹 다 세이브 하는 방법이 되어야할 듯.
- 바이너리면 용량이 어떻게 되는거지?
    - 키 1000개 짜리 딕셔너리로 저장해보았다.
    - 바이너리 : 5KB
    - 텍스트 : 29KB
"""
