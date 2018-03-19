#!/usr/bin/python
# -*- coding:UTF-8 -*-
import multiprocessing
import subprocess
print(multiprocessing.cpu_count())
for i in range(2,4):
    def worker_i():
        subprocess.Popen("./lastz --format=maf --ambiguous=iupac --notransition /home/malab19/1.9TB_Volume_mounted/whm_data/AGP4.35/shell_result/{0}_result\
         /home/malab19/1.9TB_Volume_mounted/whm_data/tair10/tair10.fa > /home/malab19/1.9TB_Volume_mounted/whm_data/lastz_result/lastz_result_{1}".format(i,i),shell=True)
         
    creatVar = locals()
    creatVar['p' + str(i)] = multiprocessing.Process(target=worker_i)
    s=locals()['p'+str(i)]
    s.start()
