# pythonGuide

### python
Virtualenvs可帮助您将不同项目的依赖关系分开

### 各图标代表的含义
c代表Class:类
m代表Method:方法
F代表Function:函数
f代表Field:域
v代表Variable:变量
紫色p代表Property:python内置函数
黄色p代表Parameter：参数
<>代表Element:元素
Directory:目录
Package:包

### Python工程目录结构

关于如何组织一个较好的Python工程目录结构，已经有一些得到了共识的目录结构。在Stackoverflow的这个问题上，能看到大家对Python目录结构的讨论。
假设你的项目名为foo, 我比较建议的最方便快捷目录结构这样就足够了:

Foo/
|-- bin/
|   |-- foo
|
|-- foo/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- docs/
|   |-- conf.py
|   |-- abc.rst
|
|-- setup.py
|-- requirements.txt
|-- README
简要解释一下:

bin/: 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
foo/: 存放项目的所有源代码。
(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。
(2) 其子目录tests/存放单元测试代码； 
(3) 程序的入口最好命名为main.py。
docs/: 存放一些文档。
setup.py: 安装、部署、打包的脚本。
requirements.txt: 存放软件依赖的外部Python包列表。
README: 项目说明文件。
__init__.py文件的作用：
(1)在文件夹里加__init__.py文件时，Python会自动认为这是一个包，若不加会被认为是普通文件夹
(2)__init__.py文件还可以控制文件下面模块的使用，即当前__init__.py文件的内容
(3)可以批量导入----就是说如果你的每一个模块都需要Python标准的内库内容，不可能你每在一个模块写代码都重复写入所需的内库内容那么__init__.py文件则会帮助你解决这个问题
__init__.py文件的代码为：
导入的是Python里面系统内置的标准内库
import sys
import datetime
import io

### python模块和包,项目结构
包：文件夹（Python）    
模块：文件夹里的文件即.py文件（Python.test1.py）
模块的命名：包名.模块名.py（Python.test1.py）

一个完整的结构需要满足以下的条件：
拥有一个在版本管理之下的源码目录
程序信息在setup.py中定义
在一个virtualenv环境中运行
#### 模块
模块分为三种：
自定义模块
内置标准模块
开源模块（第三方）
导入模块四种方法

    import module1,module2
    from 模块名 import 函数名
    from  模块名 import 函数名 as 函数别名
    import 模块名 as 函数别名
    
#### 导入包的方法:
import 包名.模块名
from 包名 import 模块名
import 包名(注意__init__.py函数的内容)

### pip 是一个现代的，通用的 Python 包管理工具
#### pip 安装第三方模块
第三方模块 通常是指由 知名的第三方团队 开发的 并且被 程序员广泛使用 的 Python 包 / 模块
提供了对 Python 包的查找、下载、安装、卸载等功能

安装和卸载命令如下：
# 将模块安装到 Python 2.x 环境
$ sudo pip install pygame
$ sudo pip uninstall pygame

# 将模块安装到 Python 3.x 环境
$ sudo pip3 install pygame
$ sudo pip3 uninstall pygame
