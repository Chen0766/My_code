temp=input('猜猜20位员工中哪几位员工能得到工资？输入6开始：')
abc = int(temp)
if abc==6:
 money = 10000
 for mem in range(1,21):
  import random
  jx = random.randint(1,10)
  if money>0:
      if jx>=5:
           print(f"员工{mem},领取工资1000元！")
           money = money-1000
      else:
           print(f'员工{mem}，绩效不足5，不发工资，下一位！')
  else:      
      print('公司没钱啦！发工资结束')  
      break
else:
     print('不听话！不给玩啦')
aaa = input()