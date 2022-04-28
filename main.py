import re


def reverse_string(s):
    """
    :param s:
    :return:
    """
    if not s:
        raise ValueError("不接受非空字符串")
    chars = list(s)
    start = 0
    end = len(chars) - 1
    while start < end:
        if not re.match(r"[a-zA-Z]", chars[start]):
            start += 1
        elif not re.match(r"[a-zA-Z]", chars[end]):
            end -= 1
        else:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
    return "".join(chars)


def reverse_v2(s: str):
    """
    对中文不友好
    :param s:
    :return:
    """
    if not s:
        raise ValueError("不接受非空字符串")
    chars = s.encode(encoding="utf-8")
    r_string = list(s)
    start = 0
    end = len(r_string) - 1
    while start < end:
        if not 33 <= chars[start] <= 122:
            start += 1
        elif not 33 <= chars[end] <= 122:
            end -= 1
        else:
            r_string[start], r_string[end] = r_string[end], r_string[start]
            start += 1
            end -= 1
    return "".join(r_string)


if __name__ == '__main__':
    print("ab-cd 字符位置反转：", reverse_string("ab-cd"))
    print("a-bC-dEf-ghIj 字符位置反转：", reverse_string("a-bC-dEf-ghIj"))
    print("Test1ng-Leet=code-Q! 字符位置反转：", reverse_string("Test1ng-Leet=code-Q!"))

    s = input("请输入一个字符串：")  # "sdfwef@w地春，sdfw"
    print("字符位置反转：", reverse_string(s))

    # print("ab-cd 字符位置反转：", reverse_v2("ab-cd"))
    # print("a-bC-dEf-ghIj 字符位置反转：", reverse_string("a-bC-dEf-ghIj"))
    # print("Test1ng-Leet=code-Q! 字符位置反转：", reverse_string("Test1ng-Leet=code-Q!"))

