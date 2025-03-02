
def ReadFile(FileName = "1.txt"):
    with open(FileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 去除每行末尾的换行符（如果存在）
        lines = [line.rstrip() for line in lines]
        lines = list(filter(lambda x : x != "",lines))
        return lines
def Statistic(Lines = []):
    Dic = {}
    for line in Lines:
        if line in Dic.keys():
            Dic[line] = Dic[line] + 1
        else:
            Dic[line] = 1
    for (k,v) in Dic.items():
        print("%s:%d"%(k,v))
Statistic(ReadFile())
