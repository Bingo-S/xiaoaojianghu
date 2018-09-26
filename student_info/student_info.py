def get_chinese_char_count(s):
    count = 0 #先假设个数为０
    for x in s: 
        if ord(x) > 127:# 如果x为中文字符，加一
            count += 1
    return count


def input_student():
    L = [] #创建一个新的列表，用此列表准备保存学生信息
    while True:
        n = input('请输入姓名:')
        if not n: # ?
            break
        a = int(input('请输入年龄:'))
        s = int(input('请输入成绩:'))
    # 创建一个新的字典，把学生信息存入字典中
        d = {} #每次都重新创建一个新的字典
        d['name'] = n
        d['age'] = a
        d['score'] = s 
        L.append(d)
    return L


def output_student(L):
    s1='name'
    s2='age'
    s3='score'
    print('+' + '-'*15 + '+' + '-'*10 + 
        '+' + '-'*10 + '+')
    print('|'+ s1.center(15) + '|' + s2.center(10) + '|'
        + s3.center(10) + '|') 
    print('+' + '-'*15 + '+' + '-'*10 + 
        '+' + '-'*10 + '+')
    for d in L:
        n = d['name']
        a = str(d['age'])
        s = str(d['score'])
        cn = get_chinese_char_count(n)
        print('|%s|%s|%s|' % (n.center(15-cn),
            a.center(10),s.center(10)))
    print('+' + '-'*15 + '+' + '-'*10 + '+' + 
        '-'*10 + '+')


def delete_student(L):
    n = input('please input deleta student name:')
    for x in L:
        if n == x['name']:
            L.remove(x)
        print('已删除%s信息' % x['name'])
    return L


def modify_student_score(L):
    n = input('please input modify student name:')
    for x in L:
        if n in x['name']:
            s = int(input('请输入修改成绩:'))
            x['score'] = s
         
            # L.remove(x)
            # n = input('请输入修改姓名:')
            # a = int(input('请输入修改年龄:'))
            # s = int(input('请输入修改成绩:'))
            # d = {} 
            # d['name'] = n
            # d['age'] = a
            # d['score'] = s 
            # L.append(x)
        print('已修改') 
        return L

def score(d): # d 是字典
   return d['score']
def print_info_by_score_desc(L):
    l = sorted(L,key=score,reverse=True)
    output_student(l)
def print_info_by_score_asc(L):
    l = sorted(L,key=score)
    output_student(l)

def age(d):
    return d['age']
def print_info_by_age_desc(L):
    l = sorted(L,key=age,reverse=True)
    output_student(l)
def print_info_by_age_asc(L):
    l = sorted(L,key=lambda d:d['age'])
    output_student(l)
