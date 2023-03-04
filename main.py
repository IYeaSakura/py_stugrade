# 定义列表用于储存字典
stu = []

# 定义显示菜单界面的函数
def menu():
    """
    显示菜单界面的函数
    :return: 输出选项
    """
    # 选项
    print('-' * 15)
    print('1、添加学生信息')
    print('2、修改学生信息')
    print('3、删除学生信息')
    print('4、查找学生信息')
    print('5、查看学生排名')
    print('6、退出程序')
    print('-' * 15)
    # 输入输出
    k = int(input('输入选项:'))
    return k


# 定义选择学生信息标签的函数
def tag_stu(part):
    """
    选择学生信息标签的函数
    :param part: 输入调用的位置(1、revise_stu函数; 2、check_stu函数)
    :return: 学生信息标签
    """
    global stu
    # 显示选择界面
    print('-' * 15)
    print('1、姓名')
    print('2、学号')
    if part == 2:
        print('3、排名')
    else:
        pass
    # 输入并返回查找标签
    tmp_num = int(input('输入通过查找方式:'))
    if tmp_num == 1:
        tmp_name = input('输入姓名:')
        return 'name',tmp_name
    elif tmp_num == 2:
        tmp_id = int(input('输入学号:'))
        return 'id',tmp_id
    elif part == 2 and tmp_num == 3:
        tmp_rank = int(input('输入排名:'))
        return 'rank',tmp_rank
    else:
        print('错误的选项！')
        return

# 定义添加学生信息的函数
def add_stu():
    """
    添加学生信息的函数
    :return: None
    """
    global stu
    # 显示学生的序号
    print('-' * 15)
    print(f'开始录入第{len(stu) + 1}位学生的数据')
    # 输入学生基本信息
    new_name = input('输入学生姓名:')
    new_id = int(input('输入学生学号:'))
    new_gradeFirst = int(input('输入成绩一:'))
    new_gradeSecond = int(input('输入成绩二:'))
    new_gradeAll = new_gradeFirst + new_gradeSecond
    # 判断信息是否重复
    for i in stu:
        if new_name == i['name']:
            print('信息重复！')
            return
    # 将学生信息存入字典
    stu_dict = {}
    stu_dict['name'] = new_name
    stu_dict['id'] = new_id
    stu_dict['gradeFirst'] = new_gradeFirst
    stu_dict['gradeSecond'] = new_gradeSecond
    stu_dict['gradeAll'] = new_gradeAll
    # 将字典存入列表
    stu.append(stu_dict)
    print('-' * 15)

# 定义修改学生信息的函数
def revise_stu():
    """
    修改学生信息的函数
    :return: None
    """
    global stu
    # 查找输入的学生
    tag, info = tag_stu(1)
    for i in stu:
        if info == i[tag]:
            new_name = input('修改姓名:')
            new_id = int(input('修改学号:'))
            new_gradeFirst = int(input('修改成绩一:'))
            new_gradeSecond = int(input(('修改成绩二:')))
            new_gradeAll = new_gradeFirst + new_gradeSecond
            for j in stu:
                if new_name == j['name']:
                    print('信息重复！')
                    return
            i['name'] = new_name
            i['id'] = new_id
            i['gradeFirst'] = new_gradeFirst
            i['gradeSecond'] = new_gradeSecond
            i['gradeAll'] = new_gradeAll
            return
    print('查找的信息有误!')
    return

# 定义删除学生信息的函数
def del_stu():
    """
    删除学生信息的函数
    :return: None
    """
    global stu
    # 查找输入的学生
    tag, info = tag_stu(2)
    # 删除学生信息
    for i in range(len(stu)):
        if info == stu[i][tag]:
            del stu[i]
            return
    print('查找的信息有误！')
    return

# 定义排序学生总成绩的函数
def sort_stu():
    """
    排序学生总成绩的函数
    :return: None
    """
    global stu
    # 定义临时列表拷贝学生数据
    tmp_stu = list(stu)
    # 排序成绩
    tmp_stu.sort(key=lambda x: x['gradeAll'], reverse=True)
    # 将排名录入列表
    for i in range(len(tmp_stu)):
        for j in stu:
            if tmp_stu[i]['name'] == j['name']:
                j['rank'] = i + 1

# 定义查找学生信息的程序
def check_stu():
    """
    查找学生信息的函数
    :return: None
    """
    global stu
    # 查找输入的学生
    tag, info = tag_stu(2)
    # 输出学生信息
    for i in stu:
        if info == i[tag]:
            print(i)
            return
    print('查找的信息有误！')
    return

# 定义输出排序后的学生信息的函数
def rank_stu():
    """
    输出排序后的学生信息的函数
    :return: None
    """
    global stu
    # 拷贝原列表数据
    tmp_stu = list(stu)
    # 按照rank键值排序临时数据
    tmp_stu.sort(key=lambda x: x['rank'])
    # 输出排序结果
    for i in tmp_stu:
        print(i)

# 主函数部分
while True:
    key = menu()
    if key == 1:
        add_stu()
        sort_stu()
    elif key == 2:
        revise_stu()
        sort_stu()
    elif key == 3:
        del_stu()
        sort_stu()
    elif key == 4:
        check_stu()
    elif key == 5:
        rank_stu()
    elif key == 6:
        print('程序结束!')
        break
    else:
        print('错误的选项！')
