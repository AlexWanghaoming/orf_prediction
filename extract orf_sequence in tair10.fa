#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pandas
import numpy
import re
import time
genome=open('/home/malab19/1.9TB_Volume_mounted/whm_data/tair10/tair10.fa')
orf_stats=pandas.read_csv('/home/malab19/1.9TB_Volume_mounted/whm_data/tair10/orf_stats_new2.csv')
coords=orf_stats["orf_coords"]

chr=orf_stats.iloc[:,[1]]
list1=[]
for i in chr["orf_coords"]:
    chromsome=str(i).split(':')[0]
    list1.append(chromsome)
all_chr = set(list1)
# def get_position():
# position = {'chr1':[],'chr2':[],'chr3':[],'chr4':[],'chr5':[],'chrMt':[],'chrPt':[]}
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
sequence={'chr1':'','chr2':'','chr3':'','chr4':'','chr5':'','chrMt':'','chrPt':''}
title_list=[1514792]
count=0
genome_list=genome.readlines()
for index,item in enumerate(genome_list):
    for i in all_chr:
        if item.startswith('>'+i):
            count+=1
            title_list.append(index)
            title_list.sort()
            temp2=''.join(genome_list[index+1:title_list[count]]).replace('\n','')
            sequence[i]=sequence[i]+temp2
            temp2=[]
# print(sequence['chr1'][3759:5630])
def reverse_complement(chr,start,stop):
    ntComlement = {'A':'T','C':'G','T':'A','G':'C'}
    seq=''
    for base in sequence[chr][start-1:stop]:
        seq=seq+ntComlement[base]
    revSeq=list(reversed(seq))
    return ''.join(revSeq)

print(orf_stats.iloc[0,2].split(':')[0])
col_num = int(orf_stats.describe().iloc[0,0])
for line in range(col_num):
    if orf_stats.iloc[line,1].split(':')[2] == '+':
        outf.write('>{0}_{1}_{2}\n{3}\n'.format(orf_stats.iloc[line,1].split(':')[0],orf_stats.iloc[line,0].split(':')[1],orf_stats.iloc[line,4],\
        sequence[orf_stats.iloc[line,1].split(':')[0]][int(re.split(':|-',orf_stats.iloc[line,1])[1])-1:int(re.split(':|-',orf_stats.iloc[line,1])[2])]))
    else:
        outf.write('>{0}_{1}_{2}\n{3}\n'.format(orf_stats.iloc[line,1].split(':')[0],orf_stats.iloc[line,0].split(':')[1],orf_stats.iloc[line,4],\
        reverse_complement(orf_stats.iloc[line,1].split(':')[0],int(re.split(':|-',orf_stats.iloc[line,1])[1]),int(re.split(':|-',orf_stats.iloc[line,1])[2]))))



