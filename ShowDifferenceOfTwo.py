
def ReadFileBySet(FileName = "1.txt"):
    with open(FileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 去除每行末尾的换行符（如果存在）
        lines = [line.rstrip() for line in lines]
        lines = list(filter(lambda x : x != "",lines))
        return set(lines)
def PrintSet(Input = set()):
    for s in Input:
        print(s)
def ShowDiff(S1 = set(),S2 = set()):
    print("<<<<<<<<<<<<<<<<<<<<<S1 - S2>>>>>>>>>>>>>>>>>>>>")
    PrintSet(S1 - S2)
    print("<<<<<<<<<<<<<<<<<<<<<S2 - S1>>>>>>>>>>>>>>>>>>>>")
    PrintSet(S2 - S1)
    print("<<<<<<<<<<<<<<<<<<<<<S1 & S2>>>>>>>>>>>>>>>>>>>>")
    PrintSet(S1 & S2)
ShowDiff(ReadFileBySet("1.txt"),ReadFileBySet("2.txt"))