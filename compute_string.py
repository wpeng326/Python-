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
    if s != '':  #这里只需要考虑，s是否为空，若为空就不用再加了,考虑了一个数字传入的情形，以及防止）后再传入一个空的s=''
        str_list.append(s)
    return str_list  #list
# 这里定义一个比较元素优先级的函数
# 完美的答案，改进版还支持了多位数的运算
def priority_level(a,b):
    # 用a和b去比较，若（末端）b比新插入的a大或者相等则返回Ture，否则返回Flase
    if (a in '/\*') and b in ('/\*'):
        return True
    elif (a in '+-') and b in ('+-\*/'):
        return True
    else:
        return False
def cen_to_back(exp:str):
    exp_list = exp_update(exp)
    sta = []
    out = []
    for c in exp_list:
        if c.isdigit():
            out.append(c)
        elif c in '+-*/':
            # or语句的判断，和and的语句的判断逻辑，and中前面的为flase，则自动返回不会计算后面的
            while sta != [] and  priority_level(c,sta[-1]):
                out.append(sta.pop())
            sta.append(c)
        elif c == '(':
            sta.append(c)
        elif c == ')':
            while sta[-1] != '(':
                out.append(sta.pop())
            sta.pop()
    while sta != []:
        out.append(sta.pop())
    return out 

def compute(cha,a1,a2):             #有bug这里只考虑了整数间的运算，而没有考虑小数，后期再改
    if cha =='+':
        return int(a1) + int(a2)
    elif cha =='-':
        return int(a1) - int(a2)      
    elif cha =='*':
        return int(a1) * int(a2)      
    else:
        return int(a1) / int(a2)
    
    
def com_result(exp:str):     # 这里是实际的运算函数
    out = cen_to_back(exp)
    
    result = []
    for c in out:
        if c in '+-/*':
            a2 = result.pop()
            a1 = result.pop()
            result.append(compute(c,a1,a2))
        elif c.isdigit():
            result.append(c)
    return result
