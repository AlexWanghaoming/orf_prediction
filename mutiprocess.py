#!/usr/bin/python
# -*- coding:UTF-8 -*-
import multiprocessing#多进程
import subprocess  #调用系统命令
print(multiprocessing.cpu_count())
for i in range(2,4):#cpu是双核四个cpu最多可以用三个
    def worker_i():
        subprocess.Popen("./lastz --format=maf --ambiguous=iupac --notransition /home/malab19/1.9TB_Volume_mounted/whm_data/AGP4.35/shell_result/{0}_result\
         /home/malab19/1.9TB_Volume_mounted/whm_data/tair10/tair10.fa > /home/malab19/1.9TB_Volume_mounted/whm_data/lastz_result/lastz_result_{1}".format(i,i),shell=True)
         
    creatVar = locals()#获取所有局部变量，返回一个字典
    creatVar['p' + str(i)] = multiprocessing.Process(target=worker_i)#循环创建狠多变量（p1,p2,p3.....）
    s=locals()['p'+str(i)]
    s.start()
