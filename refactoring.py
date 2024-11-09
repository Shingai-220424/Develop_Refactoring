import re

def sum():
    result = 0
    for i in range(1, 11):
        result += i
    return result

def test_sum():
    assert sum() == 55

def repeat_string(s, num1, num2):
    """文字列を行と列に繰り返し出力する

    Args:
        s (str): 入力する文字列
        num1 (int): 文字列を横に繰り返す回数
        num2 (int): 繰り返した文字列を盾に繰り返す回数

    Raises:
        ValueError: 文字列は5文字以上、10以下でなければなりません
        ValueError: 文字列はアルファベットのみでなければなりません

    Returns:
        _type_: 改行削除
    """
    # TODO:数値の範囲を定数化する
    if not (5 <= len(s) <= 10):
        raise ValueError("文字列は5文字以上、10以下でなければなりません")
    if not re.match("^[a-zA-z]+$", s):
        raise ValueError("文字列はアルファベットのみでなければなりません")
    horizontal = s * num1

    result =  (horizontal + "\n") * num2

    return result.rstrip("\n")

