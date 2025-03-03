
def ReadFile(FileName = "1.txt"):
    with open(FileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # 去除每行末尾的换行符（如果存在）
        lines = [line.rstrip() for line in lines]
        lines = list(filter(lambda x : x != "",lines))
        return lines
def WritFile(Content = []):
    with open('output.txt', 'w') as file:
        file.writelines(Content)
def Statistic(Lines = []):
    Dic,WritCintent = {},[]
    for line in Lines:
        if line in Dic.keys():
            Dic[line] = Dic[line] + 1
        else:
            Dic[line] = 1
    sorted_items = sorted(Dic.items(), key=lambda item: item[1],reverse=True)
    sorted_dict = dict(sorted_items)
    for (k,v) in sorted_dict.items():
        WritCintent.append("%s\t%d\n"%(k,v))
    WritFile(WritCintent)
Statistic(ReadFile())
