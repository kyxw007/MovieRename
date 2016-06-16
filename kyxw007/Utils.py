# coding=utf-8
import unicodedata


def hasChinese(str):
    for ch in str:
        if unicodedata.east_asian_width(ch) != 'Na':
            return True
    return False
