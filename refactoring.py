import re

def sum():
    result = 0
    for i in range(1, 11):
        result += i
    return result

def test_sum():
    assert sum() == 55

def repeat_string(s, num1, num2):
    if not (5 <= len(s) <= 10):
        raise ValueError("文字列は5文字以上、10以下でなければなりません")
    if not re.match("^[a-zA-z]+$", s):
        raise ValueError("文字列はアルファベットのみでなければなりません")
    horizontal = s * num1

    result =  (horizontal + "\n") * num2

    return result.rstrip("\n")

