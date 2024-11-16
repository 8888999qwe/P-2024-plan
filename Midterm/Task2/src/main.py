# 学生管理系统
import json
from importlib.resources import files
from pyecharts.render.snapshot import save_as

# PS: 可以仅以 “姓名” / “学号” 来代指学生信息

STU_LIST = {}
global dir_size
def stu_init():
    """此函数用于, 从文件中, 初始化学生信息"""
    f = open(r"\Midterm\Task2\stu_infor.json", "r",
             encoding="UTF-8")
    json.load(f)
    global dir_size
    global STU_LIST
    dir_size = len(STU_LIST)
    pass

def get_choice() -> int:
    """此函数用于, 在命令行里, 获取用户输入的选项"""
    func= int(input("请输入功能代码："))
    return func
    pass

def menu():
    print("----------学生信息查询菜单----------")
    print("-------添加学生信息\t[代号1]--------")
    print("-------删除学生信息\t[代号2]--------")
    print("-------修改学生信息\t[代号3]--------")
    print("-------保存学生信息\t[代号4]--------")
    print("-------查询学生信息\t[代号5]--------")
    print("-------退出程序\t\t[代号0]--------")
    return

def exec(func):
    """此函数用于, 根据用户输入的选项, 执行相应的功能"""
    if func==1:
        stu_add()
    elif func==2:
        stu_del()
    elif func==3:
        stu_mod()
    elif func==4:
        stu_save()
    elif func==5:
        stu_sel()
    else:
        print("请输入正确代码: ")
    pass


def stu_add():
    """此函数用于, 添加学生信息"""

    name = input("姓名: ")
    student_id = int(input("学号: "))
    dir={}
    dir["name"] = name
    dir["student_id"] = student_id
    STU_LIST[name] = dir
    pass

def stu_del():
    """此函数用于, 删除学生信息"""
    name = str(input("删除学生信息对应姓名: "))
    name_1 = STU_LIST.pop(name)
    print(f"您删除的信息是：{name_1}")
    pass


def stu_mod():
    """此函数用于, 修改学生信息"""
    change_name = str(input("请输入需要修改的学生的姓名："))
    change_id = input("请输入修改后的学号：")
    STU_LIST[change_name]["student_id"] = change_id
    print(f"学号从{STU_LIST[change_name]["student_id"]}变成了{change_id}")
    pass


def stu_sel():
    """此函数用于, 查询学生信息"""
    for key in STU_LIST:
        print(f"姓名: {STU_LIST[key]["name"]},学号: {STU_LIST[key]["student_id"]}\n")
    pass


def stu_save():
    """此函数用于, 将学生信息保存到文件中"""
    with open("/stu_infor.json", "w", encoding="UTF-8") as f:
        json.dump(STU_LIST,f)
    print("保存成功")
    pass


def main():
    """尽量不要修改此函数的代码, 此函数用于全局调用"""
    stu_init()
    menu()
    user_choice = get_choice()
    while user_choice != 0:
        exec(user_choice)
        user_choice = get_choice()


if __name__ == '__main__':
    main()
