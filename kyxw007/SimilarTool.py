# coding=utf-8


def similar(title, origin_title, file_name):
    same_sub_title_chiness = getMaxSubString(title, file_name)  # 中文最大相同子串
    same_sub_title_orgin = getMaxSubString(origin_title, file_name)  # 原名最大相同子串
    return (len(same_sub_title_chiness) + len(same_sub_title_orgin)) / len(file_name)


def getMaxSubString(title, file_name):
    title1 = title
    file_name1 = file_name
    maxStr = [title, file_name][len(title1) < len(file_name1)]
    minStr = [title, file_name][len(title1) > len(file_name1)]
    length = len(minStr)
    substring = u""
    for i in range(0, length):
        x = 0
        y = length - i
        while y <= length:
            str = minStr[x:y]
            if str in maxStr:
                if len(str) > len(substring):
                    substring = str
            x += 1
            y += 1
    return substring
