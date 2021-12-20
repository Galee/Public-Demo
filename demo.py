# 字符串的拼接
# a=886
# b=886
# if a>b:
#     print (str(a)+"大")
# elif a<b:
#     print (str(b)+"大")
# else:
#     print (type(str(a)+"=="+str(b)))
#
# c=147258
# if c==0:
#     print ("请重新输入")
# else:
#     if c%2==0:
#         print (str(c)+"是一个偶数")
#     elif c%2!=0:
#         print (str(c)+"是一个奇数")


# 质数 素数
# num1=(int(input("请输入一个数字")))
# if num1%1==0 and num1%num1==0:
#     print (str(num1)+"是一个素数")

# head=35
# foot=94
# tu=int((foot/2)-head)
# ji=int(head-tu)
# print ("兔子有"+str(tu)+"只")
# print ("鸡有"+str(ji)+"只")

# 循环
# sum1=0
# cou=1
# while cou<100:
#     sum1+=cou
#     cou+=2
# print (sum1)

# for循环(遍历)
# 遍历的意思就是将一个数组中的元素依次挨个输出
# for j in range(1,35):
#     for k in range(1,35):
#         if (2*j+4*k==94 and j+k==35):
#             print ("兔子有"+str(k)+"只")
#             print ("鸡有"+str(j)+"只")

# 运用for循环打印一个九九乘法表
# for m in range(1,10):
#     for n in range(1,m+1):
#         print (str(n)+"*"+str(m)+"="+str(m*n))
# 制作简易计算器
# num1=(float(input("请输入第一个数")))
# num2=(float(input("请输入另外一个数")))
# flag=(str(input("请输入需要执行的操作")))
# if flag=="+":
#     print (num1+num2)
# if flag=="-":
#     print (num1-num2)
# if flag=="*":
#     print (num1*num2)
# if flag=="/":
#     print (num1/num2)
# int float str
# 列表
# 数组/列表 通过下标访问  下标的排列是从0开始的
# a=[47,14,58,14.25,58.72,14,14]
# insert delete select update
# print(a.copy())
# 函数
# def sum(num1,num2):
#     print(num1+num2)
# sum(14,25)
# 第一种方法没有返回值
# def sum1(num1,num2):
#     return num1+num2
# aa=sum1(14,25)
# print(aa)
# 第二种方法是有返回值，有返回值就需要有接收值
# def init():
#     num1 = float(input("请输入第一个数"))
#     num2 = float(input("请输入另外一个数"))
#     flag = str(input("请输入需要执行的操作"))
#     return num1,num2,flag
# str=init()
# def aa():
#     if str[2]=="+":
#         print (str[0]+str[1])
#     if str[2] == "-":
#         print (str[0] - str[1])
#     if str[2] == "*":
#         print (str[0] * str[1])
#     if str[2] == "/":
#         print (str[0] / str[1])
# aa()

# str=" hello world & 大傻逼 "
# find查找匹配的元素并且输出其下标志,只输出第一个
# if str.find("&")>=0:
#     print("含有非法字符")
# else:
#     print("没毛病老铁")

# print(str.count(" "))
# print(str.split("l"))
# str1="+"
# print(str1.join(str))
# join在字符串中表示串联，
# if str.find("大傻逼")>=0:
#     print(str.replace("大傻逼","***"))
# else:
#     print("没毛病老铁")
# print(str)
# print(str.rstrip())
# 正则 相当于是一个规则
# str1=input("请输入一句话")
# reg="\w\W\d\D"
# 定义了4个东西  单词字符+非单词字符集+数字+非数字
# print(str1(reg))
# 正则表达式是用来检测用户输入的合法合规性
# import re
# str1=input("请输入手机号")
# res=re.search("(1[3-9][0-9]\d{8})",str1)
# if res:
#     print ("账号正确")
# else:
#     print("你是不是傻，自己的电话都记不住")
# 验证邮箱合法性
# search 验证
# import re
# text = input("Please input your Email address：\n")
# if re.match(r'[a-zA-Z]{1}[0-9a-zA-Z_]{0,16}[0-9a-zA-Z]{1}@163\.[com,cn,net]{1,3}',text):
#     print('1')
# else:
#     print('2')
# match方法
# import re
# pattern=re.compile(r"hello world")
# match=pattern.match("hello world hello python")
# if match:
#     print (1)
# search=pattern.search("hello world hello python")
# if search:
#     print (2)
# num=re.findall(r"\w","one1two2three3")
# print (num)
# phone="123-456-7894 # telephone number"
# res=re.sub(r"#.*","a",phone)
# print ("number:",res)
# result=re.sub(r"\D","",res)
# print ("number:",result)
# num=tuple("12345")
# print (num)
# x=1,2,3,4
# print(x[:3])
# 字典
# 字典的遍历
# name_age={"name":"james","age":18,"sex":"男","address":"taiyuan"}
# print(dict(name_age)['sex'])
# for item in name_age.items():
#     print (tuple(item)[0])
# 键-->下标 直接添加   修改也是可以直接赋值
# name_age['age']=12500
# print (name_age)
# name_age.clear()
# print (name_age)
# name_age1=name_age.copy()
# print(name_age1)
# print(name_age.get('money'))
# 有效代码100000行 相当于工作经验5年以上
# a1={}
# res=a1.fromkeys(["name","age","sex","address"])
# print (res)
# name_age.pop("name")
# print (name_age)
# 面向对象
# class James:
#     def init(self):
#         print ("hello world")
#     def name(self):
#         print ("my name is jamon lee")
# james=James()
# print(isinstance(james,James))

# class Students:
#     def __init__(self,id_number):
#         self.value=id_number
#     def show(self):
#         print (self.value)
# stu1=Students(888666)
# stu1.show()
# 在类的中间添加以两个下划线开头的是私有的
# class Aa:
#     def __init__(self,id,name):
#         self.id=id
#         self.__name=name
# res=Aa(6,"zhangsan")
# print (res._Aa__name)
# print (res.name)
#
# class A():
#      def init(self):
#          self.str=["111","666"]
#      def ft(self,buf):
#          return [n for n in buf if n not in self.str]
# class B(A):
#     def init(self):
#         self.str=["hello world"]
#     def aa(self):
#         print (1)
# result=B()
# result.init()
# print(result.ft(["hello world","111","666"]))

# 文件处理
# f=open(r"C:\Users\86153\Desktop\admin.txt","r")
# f.readline()
# import os
# os.rename(r"C:\Users\86153\Desktop\python.txt","aa.txt")
# os.remove(r"C:\Users\86153\Desktop\aa.txt")
# 操作目录
# os.mkdir("big data class 3")
# print(os.getcwd())
# with open(r"C:\Users\86153\Desktop\aa.txt","w",encoding="utf-8")as fp:
#     print(fp.write("hahaha"))
# with open(r"C:\Users\86153\Desktop\aa.txt","r",encoding="utf-8")as fp:
#     print(fp.read())
# import tkinter as tk
# def event():
#     global user,num
#     num+=1
#     l1 = tk.Label(user, text=str(num))
#     l1.pack()
# num=0
# user=tk.Tk()
# user.wm_title("我的第一个窗体")
# l2=tk.Button(user,text="我是按钮",command=event)
# l2["width"]=20
# l2["height"]=10
# l2["background"]="yellow"
# l2.pack()
# user.mainloop()
# import tkinter as tk
# def event(event):
#     global user,num
#     num+=1
#     l1 = tk.Label(user, text=str(num))
#     l1.pack()
# num=0
# user=tk.Tk()
# user.wm_title("我的第一个窗体")
# l2=tk.Button(user,text="我是按钮")
# l2["width"]=20
# l2["height"]=10
# l2["background"]="yellow"
# l2.bind("<Button-1>",event)
# l2.pack()
# user.mainloop()

# import tkinter as tk
# fl=tk.Tk()
# tk.Button(fl,text="按钮").pack(side="top",expand=1,fill="y")
# fl.mainloop()
# l1=tk.Label(fl,text="666")
# l1.grid(row=2,sticky="E")
# l2=tk.Label(fl,text="555")
# l2.grid(row=1,sticky="E")
# tk.mainloop()
# 定位
# l1=tk.Label(fl,text="666").place(x=100,y=200)
# fl.mainloop()

# import tkinter as tk
# user=tk.Tk()
# def event(event):
#      global user,num
#      num+=1
#      l1 = tk.Label(user, text=str("鼠标左击事件"))
#      l1.pack()
# num=0
# user.wm_title("我的第一个窗体")
# l2=tk.Button(user,text="我是按钮")
# l2["width"]=20
# l2["height"]=10
# l2["background"]="yellow"
# l2.bind("<Control-D>",event)
# 获取焦点
# l2.focus_set()
# l2.pack()
# user.mainloop()
# import tkinter as tk
# user=tk.Tk()
# l1=tk.Label(user,text="账号")
# l2=tk.Label(user,text="密码")
# l1.pack()
# l2.pack()
# user.mainloop()
# Label文字 Button按钮 entry输入框
# tkinter里边所有的模块都引进来
# from tkinter import *
# top = Tk()
# L1 = Label(top, text="账号")
# L1.pack(side="left")
# E1 = Entry(top, bd=5)
# E1.pack(side="right")
# top.mainloop()
# user=Tk()
# m1=Menu(user)
# for i in ["文件","编辑","格式","查看","帮助"]:
#     m1.add_command(label=i)
# user["menu"]=m1
# user.mainloop()

# user=Tk()
# m1=Menu(user)
# fm1=Menu(m1)
# for i in ["打开","保存","另存为"]:
#     fm1.add_radiobutton(label=i)
# fm1.add_separator()
# for i in ["关闭","重启"]:
#     fm1.add_checkbutton(label=i)
# m1.add_cascade(label="文件",menu=fm1)
# user["menu"]=m1
# user.mainloop()

# def event():
#     global user
#     Label(user,text="1").pack(side="left")
# user=Tk()
# m1=Menu(user)
# fm1=Menu(m1)
# for i in ["打开","保存","另存为"]:
#     fm1.add_command(label=i)
# fm1.add_command(label="共享",command=event)
# m1.add_cascade(label="文件",menu=fm1)
# user["menu"]=m1
# user.mainloop()

import numpy as np
# x=np.array([1,2,3,4])
# print(np.array((1,2,3,4,5)))
# arr1=np.array([1,2,3,4,5],dtype=np.float)
# print(arr1)
# arr1=np.linspace(2,4)
# print (arr1)
# y=np.arange(5,9)
# z=y*x
# print(z)

# arr1=np.arange(10)
# print(arr1)
# print(arr1.reshape(2,5)[0][2])
# print (arr1)

# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# arr3=np.array([5,6,7,8])
# print(np.hstack((arr1,arr2,arr3)))

# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr.T)

arr1=np.arange(10).reshape(5,2)
print(np.array_split(arr1,3,axis=1))

