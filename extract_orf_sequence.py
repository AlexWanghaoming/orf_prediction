#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pandas
import numpy
import re
import time
genome=open('/home/malab19/1.9TB_Volume_mounted/whm_data/tair10/tair10.fa')
orf_stats=pandas.read_csv('/home/malab19/1.9TB_Volume_mounted/whm_data/tair10/orf_stats_new2.csv')
# coords=orf_stats["orf_coords"]这里的coords对象是series对象

chr=orf_stats.iloc[:,[1]]#chr对象是dataframe对象，可以用for循环
list1=[]
for i in chr["orf_coords"]:
    chromsome=str(i).split(':')[0]
    list1.append(chromsome)
all_chr = set(list1)#去除重复
# def get_position():
# position = {'chr1':[],'chr2':[],'chr3':[],'chr4':[],'chr5':[],'chrMt':[],'chrPt':[]}#建立一个字典，每个染色体对应一个大列表 
                                                                               #列表中包括该染色体上所有orf的起始和终止位置[start,stop]
# for k in all_chr:
#     for j in coords:
#         split_coords=re.split(':|-',j)
#         chr_coords=split_coords[0]
#         if k == chr_coords:
#             start=split_coords[1]
#             stop=split_coords[2]
#             temp1=[start,stop]
#             position[k].append(temp1)
#             temp1=[]
outf=open('/home/malab19/1.9TB_Volume_mounted/whm_data/tair10/tair10_orf.fa','r+')
sequence={'chr1':'','chr2':'','chr3':'','chr4':'','chr5':'','chrMt':'','chrPt':''}#建一个字典，存入fasta文件中每条染色体下的所有序列
title_list=[1514792]#这是拟南芥基因组fasta文件的行数
count=0
genome_list=genome.readlines()
for index,item in enumerate(genome_list):
    for i in all_chr:
        if item.startswith('>'+i):
            count+=1
            title_list.append(index)
            title_list.sort()
            temp2=''.join(genome_list[index+1:title_list[count]]).replace('\n','')#从一个'>'到下一个‘>’之间的序列存入temp2
            sequence[i]=sequence[i]+temp2
            temp2=[]
# print(sequence['chr1'][3759:5630])
#对于反义链进行反向互补配对
def reverse_complement(chr,start,stop):
    ntComlement = {'A':'T','C':'G','T':'A','G':'C'}
    seq=''
    for base in sequence[chr][start-1:stop]:
        seq=seq+ntComlement[base]
    revSeq=list(reversed(seq))
    return ''.join(revSeq)

print(orf_stats.iloc[0,2].split(':')[0])
col_num = int(orf_stats.describe().iloc[0,0])#这个方法用来获得dataframe的行数
for line in range(col_num):
    if orf_stats.iloc[line,1].split(':')[2] == '+':#正义链
        outf.write('>{0}_{1}_{2}\n{3}\n'.format(orf_stats.iloc[line,1].split(':')[0],orf_stats.iloc[line,0].split(':')[1],orf_stats.iloc[line,4],\
        sequence[orf_stats.iloc[line,1].split(':')[0]][int(re.split(':|-',orf_stats.iloc[line,1])[1])-1:int(re.split(':|-',orf_stats.iloc[line,1])[2])]))
    else:#反义链
        outf.write('>{0}_{1}_{2}\n{3}\n'.format(orf_stats.iloc[line,1].split(':')[0],orf_stats.iloc[line,0].split(':')[1],orf_stats.iloc[line,4],\
        reverse_complement(orf_stats.iloc[line,1].split(':')[0],int(re.split(':|-',orf_stats.iloc[line,1])[1]),int(re.split(':|-',orf_stats.iloc[line,1])[2]))))



