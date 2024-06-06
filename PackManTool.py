import os
import sys
import platform
INDEX = "https://pypi.org/simple"
PIP = "pip3"
MORE_ARGS = ""
VERSION = ""
PACK = ""
__version__ = '1.0.1-Pre1'

OS_MSG = """
    OS: {}
    Node (网络名称) : {}
    Release (内核版本号) : {}
    Version (详细版本信息) : {}
    Machine (机器类型) : {}
    Architecture (架构) : {}
    CPU Edition (CPU 类型) : {}
"""


class NotInAShell(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        pass


def getAllPackFormat(ppl = 5):
    packagesList = os.popen(PIP + " freeze").read().split("\n")
    lenMax = 0
    for i in packagesList:
        if len(i) > lenMax:
            lenMax = len(i)

    packs = ""
    idx = 0
    for i in packagesList:
        idx += 1
        addSpace = lenMax - len(i)
        pack = i + " " * addSpace
        packs += pack + ' '
        if idx % ppl == 0:
            packs += "\n"
    return packs


def index():
    CLS()
    global INDEX
    MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Index 索引

Now Index: {}
现在的索引: {}

1) Set TUNA Mirror 设置 清华源

2) Set BFSU Mirror设置 北京外国语源

3) Set PyPI Mirror 设置 官方源

4) Set Douban Mirror 设置 豆瓣源

5) Back 返回
====================================

Your choice 你的选择:
""".format(INDEX, INDEX)

    mirror_list = ["https://mirrors.tuna.edu.cn/pypi/web/simple", "https://mirrors.bfsu.edu.cn/pypi/web/simple",
                   "https://pypi.org/simple",
                   "https://pypi.douban.com/simple/"]
    choice = int(input(MSG))
    if choice == 5:
        return True
    elif 0 < choice < 5:
        INDEX = mirror_list[choice - 1]
        return True
    else:
        raise Exception


def help_msg():
    CLS()
    print("""
    用法：
        pip3＜命令＞〔选项〕

    命令：
        install       安装软件包。
        download      下载软件包。
        uninstall     卸载程序包。
        freeze        以需求格式输出已安装的程序包。
        inspect       检查python环境。
        list          列出已安装的程序包。
        show          显示有关已安装程序包的信息。
        check         验证已安装的程序包是否具有兼容的依赖项。
        config        管理本地和全局配置。
        search        搜索PyPI以查找包。
        cache         检查和管理pip的wheel缓存。
        index         检查包索引中的可用信息。
        wheel         根据您的要求制造wheel。
        hash          计算包存档的哈希。
        completion    用于命令完成的辅助命令。
        debug         显示对调试有用的信息。
        help          显示命令的帮助。

    常规选项：
        -h、 --help 显示帮助。
        --debug 让未处理的异常在主子程序之外传播，而不是记录将它们发送到stderr。
        --isolated 在隔离模式下运行pip，忽略环境变量和用户配置。
        --require-virtualenv 允许pip仅在虚拟环境中运行；否则将退出并返回错误。
        --python＜python＞ 使用指定的python解释器运行pip。
        -v、 --verbose 提供更多输出。选项是可添加的，最多可使用3次。
        -V、 --version 显示版本并退出。
        -q、 --quiet 输出更少。选项是可添加的，最多可使用3次（对应至“警告”、“错误”和“关键”日志记录级别）。
        --log＜path＞ 详细附加日志的路径。
        --no-input  禁用输入提示。
        --proxy＜proxy＞  以scheme://[user:passwd@]proxy.server:port的形式指定代理。
        --retries＜retries＞  每个连接应尝试的最大重试次数（默认为5次）。
        --timeout＜sec＞  设置套接字超时（默认为15秒）。
        --exists action＜action＞   当路径已经存在时的默认操作：(s)witch，(i)gnore，(w)ipe，(b)ackup (a)bort。
        --trusted-host＜hostname＞ 将此主机或host:port对标记为可信，即使它没有有效的或任何HTTPS。
        --cert<path> PEM编码的CA证书捆绑包的路径。如果提供，则覆盖默认值。看见有关详细信息，请参阅pip文档中的“SSL证书验证”。
        --client-cert＜path＞ SSL客户端证书的路径，一个包含私钥和PEM格式的证书。
        --cache-dir＜dir＞ 将缓存数据存储在＜dir＞中。
        --no-cache-dir 禁用缓存。
        --disable-pip-version-check  不要定期检查PyPI以确定新版本的pip是否可供下载。隐含--no-index。
        --no-color 抑制彩色输出。
        --no-python-version-warning 对即将推出的不受支持的Python发出无声的弃用警告。
        --use-feature＜feature＞启用可能向后不兼容的新功能。
        --use-deprecated <feature>启用弃用的功能，这些功能将来将被删除。 
    """)
    input()
    return


def install():
    CLS()
    global INDEX, MORE_ARGS, VERSION, PACK

    def install_packages():
        CLS()
        global VERSION, PACK, MORE_ARGS

        def Specify_version(pack):
            CLS()
            MSG_SV = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包 -> Specify Version 指定版本

{}

输入版本:
====================================
""".format(os.popen(PIP + " index versions " + pack).read())
            return input(MSG_SV)

        def Select_install():
            CLS()
            MSG_SP = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包 -> Select Package 选择包

输入包:
====================================
"""
            return input(MSG_SP)

        def execute():
            CLS()
            if VERSION == "":
                cmd = PIP + " install " + PACK + " -i " + INDEX + " " + MORE_ARGS
            else:
                cmd = PIP + " install " + PACK + "==" + VERSION + " -i " + INDEX + " " + MORE_ARGS
            MSG_E = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包 -> Execute 执行

Will Execute Command 欲执行命令: {}

====================================
Enter To Execute 回车执行:
""".format(cmd)
            input(MSG_E)
            os.system(cmd)
            input()
            return

        MSG_I = """        
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包

Now Index: {}
现在的索引: {}

1) Select Package 选择包 {}

2) Specify Version 指定版本 {}

3) Execute 执行

4) Back 返回
====================================

Your choice 你的选择:
        """.format(INDEX, INDEX, PACK, VERSION)
        choice_I = int(input(MSG_I))
        if choice_I == 2 and PACK != "":
            VERSION = Specify_version(PACK)
            return install_packages()
        if choice_I == 1:
            PACK = Select_install()
            return install_packages()
        if choice_I == 3:
            execute()
            return install_packages()
        if choice_I == 4:
            return

    def more_args():
        CLS()
        global MORE_ARGS
        MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包-> Add Arguments 额外参数

Arguments 参数:{}

输入参数:
====================================
""".format(MORE_ARGS)
        MORE_ARGS = input(MSG)
        return

    MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装

Now Index: {}
现在的索引: {}

1) Install Package 安装包

2) Add Arguments 额外参数 {}

3) Back 返回
====================================

Your choice 你的选择:
""".format(INDEX, INDEX, MORE_ARGS)

    choice = int(input(MSG))
    if choice == 1:
        install_packages()
        return install()
    if choice == 2:
        more_args()
        return install()
    if choice == 3:
        return


def os_msgF():
    OS = platform.system()
    if OS == "Darwin":
        OS = "MacOS " + platform.mac_ver()[0]
    elif OS == "win32":
        OS = "Windows " + platform.win32_edition() + " " + ".".join(platform.win32_ver())
    elif OS == "linux":
        OS = "Linux " + " ".join(platform.linux_distribution())
    NODE = platform.node()
    RELEASE = platform.release()
    VERSION = platform.version()
    MACHINE = platform.machine()
    ARCH = platform.architecture()[0]
    CPU = platform.processor()
    return OS_MSG.format(OS, NODE, RELEASE, VERSION, MACHINE, ARCH, CPU)


def info():
    CLS()
    MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Info 详细信息

输入包名:
====================================
"""
    cmd = PIP + " show " + input(MSG)
    print(os.popen(cmd).read())
    return input()


def download():
    CLS()
    global INDEX, MORE_ARGS, VERSION, PACK

    def download_packages():
        CLS()
        global VERSION, PACK, MORE_ARGS

        def Specify_version(pack):
            CLS()
            MSG_SV = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Download 下载 -> Download Packages 下载包 -> Specify Version 指定版本

{}

输入版本:
====================================
""".format(os.popen(PIP + " index versions " + pack).read())
            return input(MSG_SV)

        def Select_packages():
            CLS()
            MSG_SP = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Download 下载 -> Download Packages 下载包 -> Select Package 选择包

输入包:
====================================
"""
            return input(MSG_SP)

        def execute():
            CLS()
            if VERSION == "":
                cmd = PIP + " download " + PACK + " -i " + INDEX + " " + MORE_ARGS
            else:
                cmd = PIP + " download " + PACK + "==" + VERSION + " -i " + INDEX + " " + MORE_ARGS
            MSG_E = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Download 下载 -> Download Packages 下载包 -> Execute 执行

Will Execute Command 欲执行命令: {}

====================================
Enter To Execute 回车执行:
""".format(cmd)
            input(MSG_E)
            os.system(cmd)
            input()
            return

        MSG_I = """        
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Download 下载 -> Download Packages 下载包

Now Index: {}
现在的索引: {}

1) Select Package 选择包 {}

2) Specify Version 指定版本 {}

3) Execute 执行

4) Back 返回
====================================

Your choice 你的选择:
""".format(INDEX, INDEX, PACK, VERSION)
        choice_I = int(input(MSG_I))
        if choice_I == 2 and PACK != "":
            VERSION = Specify_version(PACK)
            return download_packages()
        if choice_I == 1:
            PACK = Select_packages()
            return download_packages()
        if choice_I == 3:
            execute()
            return download_packages()
        if choice_I == 4:
            return

    def more_args():
        CLS()
        global MORE_ARGS
        MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包-> Add Arguments 额外参数

Arguments 参数:{}

输入参数:
====================================
""".format(MORE_ARGS)
        MORE_ARGS = input(MSG)
        return

    MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Download 下载

Now Index: {}
现在的索引: {}

1) Download Package 下载包

2) Add Arguments 额外参数 {}

3) Back 返回
====================================

Your choice 你的选择:
""".format(INDEX, INDEX, MORE_ARGS)

    choice = int(input(MSG))
    if choice == 1:
        download_packages()
        return download()
    if choice == 2:
        more_args()
        return download()
    if choice == 3:
        return


def wheel():
    CLS()

    global INDEX, MORE_ARGS, VERSION, PACK

    def wheel_packages():
        CLS()
        global VERSION, PACK, MORE_ARGS

        def Specify_version(pack):
            CLS()
            MSG_SV = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Wheel 生成Whl文件 -> Wheel Packages 生成Whl -> Specify Version 指定版本

{}

输入版本:
""".format(os.popen(PIP + " index versions " + pack).read())
            return input(MSG_SV)

        def Select_packages():
            CLS()
            MSG_SP = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Wheel 生成Whl文件 -> Wheel Packages 生成Whl -> Select Package 选择包

输入包:
====================================
"""
            return input(MSG_SP)

        def execute():
            CLS()
            if VERSION == "":
                cmd = PIP + " wheel " + PACK + " -i " + INDEX + " " + MORE_ARGS
            else:
                cmd = PIP + " wheel " + PACK + "==" + VERSION + " -i " + INDEX + " " + MORE_ARGS
            MSG_E = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Wheel 生成Whl文件 -> Wheel Packages 生成Whl -> Execute 执行

Will Execute Command 欲执行命令: {}

====================================
Enter To Execute 回车执行:
""".format(cmd)
            input(MSG_E)
            os.system(cmd)
            input()
            return

        MSG_I = """        
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Wheel 生成Whl文件 -> Wheel Packages 生成Whl

Now Index: {}
现在的索引: {}

1) Select Package 选择包 {}

2) Specify Version 指定版本 {}

3) Execute 执行

4) Back 返回
====================================

Your choice 你的选择:
""".format(INDEX, INDEX, PACK, VERSION)
        choice_I = int(input(MSG_I))
        if choice_I == 2 and PACK != "":
            VERSION = Specify_version(PACK)
            return wheel_packages()
        if choice_I == 1:
            PACK = Select_packages()
            return wheel_packages()
        if choice_I == 3:
            execute()
            return wheel_packages()
        if choice_I == 4:
            return

    def more_args():
        CLS()
        global MORE_ARGS
        MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Wheel 生成Whl文件 -> Wheel Packages 生成Whl-> Add Arguments 额外参数

Arguments 参数:{}

输入参数:
====================================
                        """.format(MORE_ARGS)
        MORE_ARGS = input(MSG)
        return

    MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Wheel 生成Whl文件

Now Index: {}
现在的索引: {}

1) Wheel Package 生成Whl文件

2) Add Arguments 额外参数 {}

3) Back 返回
====================================

Your choice 你的选择:
        """.format(INDEX, INDEX, MORE_ARGS)

    choice = int(input(MSG))
    if choice == 1:
        wheel_packages()
        return wheel()
    if choice == 2:
        more_args()
        return wheel()
    if choice == 3:
        return


def remove():
    CLS()
    global INDEX, MORE_ARGS, VERSION, PACK

    def remove_packages():
        CLS()
        global VERSION, PACK, MORE_ARGS

        def Select_packages():
            CLS()
            MSG_SP = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Remove 卸载 -> Remove Packages 卸载包 -> Select Package 选择包

输入包:
====================================
                            """
            return input(MSG_SP)

        def execute():
            CLS()
            cmd = PIP + " uninstall " + PACK + " " + MORE_ARGS
            MSG_E = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Remove 卸载 -> Remove Packages 卸载包 -> Execute 执行

Will Execute Command 欲执行命令: {}

====================================
Enter To Execute 回车执行:
                            """.format(cmd)
            input(MSG_E)
            os.system(cmd)
            input()
            return

        PACKAGES = getAllPackFormat(3)
        MSG_I = """        
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Download 下载 -> Download Packages 下载包

Now Index: {}
现在的索引: {}

Packages 安装了的包 : 
{}

1) Select Package 选择包 {}

2) Execute 执行

3) Back 返回
====================================

Your choice 你的选择:
        """.format(INDEX, INDEX, PACKAGES, PACK, VERSION)
        choice_I = int(input(MSG_I))
        if choice_I == 1:
            PACK = Select_packages()
            return remove_packages()
        if choice_I == 2:
            execute()
            return remove_packages()
        if choice_I == 3:
            return

    def more_args():
        CLS()
        global MORE_ARGS
        MSG = """
====================================
Python pip for PyPI Tool

MainMenu 主界面 -> Install 安装 -> Install Packages 安装包-> Add Arguments 额外参数

Arguments 参数:{}

输入参数:
====================================
                        """.format(MORE_ARGS)
        MORE_ARGS = input(MSG)
        return

    MSG = """
====================================
Python pip for PyPI Tool

-> Remove 卸载

Now Index: {}
现在的索引: {}

1) Remove Package 卸载包

2) Add Arguments 额外参数 {}

3) Back 返回
====================================

Your choice 你的选择:
        """.format(INDEX, INDEX, MORE_ARGS)

    choice = int(input(MSG))
    if choice == 1:
        remove_packages()
        return remove()
    if choice == 2:
        more_args()
        return remove()
    if choice == 3:
        return


def settings():
    global PIP
    MSG_I = """        
    ====================================
    Python pip for PyPI Tool

    MainMenu 主界面 -> Settings 设置
    
    使用pip : {}
    ====================================
    
    输入更改的命令主体:
    """.format(PIP)
    PIP = input(MSG_I)


def mainMenu(main=False):
    CLS()
    if main:
        shell_()
    MSG = """
=============================================================================================
Python pip for PyPI Tool

Info: Run by Python {}

信息: 运行在Python {}

{}

Working dir 工作目录 : {}

1) Install 安装

2) Remove 卸载

3) Info 详细信息

4) Upgrade 升级

5) Index 索引 当前是:{}

6) Wheel 生成Whl文件

7) Download 下载

8) Help 帮助

9) Setting 设置

0) Exit 退出
=============================================================================================

Your choice 你的选择:
""".format(sys.version, sys.version, os_msgF(), os.getcwd(), INDEX)
    # TODO 4(update)\9(setting) MODE
    choice = int(input(MSG))
    if choice == 4:
        print("未开放 Not Supported")
        input()
        return mainMenu()
    if choice == 9:
        settings()
        return mainMenu()
    if choice == 5:
        print("\n\n\n")
        index()
        return mainMenu()
    if choice == 8:
        print("\n\n\n")
        help_msg()
        return mainMenu()
    if choice == 0:
        return
    if choice == 1:
        print("\n\n\n")
        install()
        return mainMenu()
    if choice == 3:
        print("\n\n\n")
        info()
        return mainMenu()
    if choice == 7:
        print("\n\n\n")
        download()
        return mainMenu()
    if choice == 2:
        print("\n\n\n")
        remove()
        return mainMenu()
    if choice == 6:
        print("\n\n\n")
        wheel()
        return mainMenu()


def shell_():
    CLS()
    if sys.stdout.isatty():
        return True
    else:
        MSG = """
================================================================
Shell Check Process

This Program  Isn't Run on Shell/TTY-like object (e.g. zsh bash cmd powershell)
================================================================

Still Execute(Y/n)?"""
        se = input(MSG)
        if se == 'y' or se == 'Y':
            return False
        else:
            raise NotInAShell("Not run in shell!")


def CLS():
    if sys.stdout.isatty():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


CLS()
def mstart():
    try:
        mainMenu(True)
    except:
        print("A error ocurred")
        mstart()

mstart()
