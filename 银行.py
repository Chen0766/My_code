#函数练习案例1


#定义查询余额函数
def cxye():
    print(f'您当前的余额剩余{money}')    
    zcd()
    
#定义存款函数
def ck():
    ckzd=input('请输入你要存款的余额:')
    ckz=int(ckzd)
    global money
    money=ckz+money
    print(f'您当前的余额剩余{money}')
    zcd()

#定义取款函数
def qk():
    qkzd=input('请输入你要取款的余额:')
    qkz=int(qkzd)
    global money
    money=money-qkz
    print(f'您当前的余额剩余{money}')
    zcd()

#定义主菜单函数()
def zcd():
    print('1:存款')
    print('2.取款')
    print('3.查询余额')
    zcdfwd=input('请选择服务:')
    zcdfw=int(zcdfwd)
    if zcdfw==1:
        ck()
    elif zcdfw==2:
        qk()
    elif zcdfw==3:
        cxye()
    else:
        print('请输入正确的数字')

#出错部分如下
money=5000000
name=input('请输入您的姓名:')
named=int(name)
if named==5:
    zcd()
else:
    print('请输入正确的姓名')