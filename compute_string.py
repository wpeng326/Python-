#利用栈来写自动识别运算字符串来计算
# ('2 + ( 5 + 3 * 2 + 1) / 3')
# 2 + ( 5 - 94 * 28 + 1) / 3 
#首先删除空格
def del_blank(exp:list):
    return ''.join(c for c in exp if c != ' ')
#按数字，操作符分割字符串
def exp_update(exp:str):
    exp = del_blank(exp)
    s=''
    str_list=[]
    for c in exp:
        if c in '+-*/()':
            if s != '':               
                str_list.append(s)                
                s = ''
            str_list.append(c)
        else:
            s = s+c
    if s != '':  #这里只需要考虑，s是否为空，若为空就不用再加了
        str_list.append(s)
    return str_list
exp_update('222  2')
