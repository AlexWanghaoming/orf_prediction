#！
import subprocess
import os, sys
import re
import time
import commands
from Bio import SeqIO
import numpy

"""
For each file in getorf on collection 2792:I search the longest ORF in the MAF alignment and 
get each ORF alignment in Zea mays and arabidopsis.
Also,there are many sequences that do not have partner or have more than one partners. abandon them.
"""


def get_eachORF_alignment(fasta_file):
    seqs = SeqIO.parse("/home/malab19/Downloads/getorf on collection 2792/{0}".format(fasta_file), 'fasta')
    dic1 = {}
    for seq in seqs:
        num = "".join(seq.id.split('_')[0:3])
        if num in dic1.keys():
            dic1[num].append(len(seq))
        else:
            dic1[num] = [len(seq)]

    for i in dic1:
        dic1[i] = numpy.max(dic1[i])
    seqs2 = SeqIO.parse("/home/malab19/Downloads/getorf on collection 2792/{0}".format(fasta_file), 'fasta')
    seq_list = []
    id_list = []
    for index, seq in enumerate(seqs2):
        if len(seq) == dic1["".join(seq.id.split('_')[0:3])]:
            seq_list.append(seq)
            id_list.append(seq.id)
    waitingForDeletList = []

    ### extract the blocks which only contain two sequences
    for i in id_list:
        identifier = int(i.split("_")[2])
        count = 0
        for j in id_list:
            if int(j.split("_")[2]) == identifier:
                count = count + 1
            else:
                pass
        if count == 2:
            pass
        else:
            waitingForDeletList.append(id_list.index(i))

    ### list don't have method to del or pop() many elements, so I use <reverse> option to prevent losing subsequent elements.
    for Index in sorted(waitingForDeletList, reverse=True):
        del seq_list[Index]

    SeqIO.write(seq_list, '/home/malab19/whm/workflow/result1/{0}_result1'.format(fasta_file), 'fasta')



"""
muscle can only align sequences in a single file. So must divide each file in result1/ into a lot of files which contain only 2 sequences
"""


def separate_files(fasta_result1):
    seqs = SeqIO.parse(
        "/home/malab19/whm/workflow/result1/{0}".format(fasta_result1), 'fasta')
    alignment_block_list = []
    # subprocess.Popen("mkdir /home/malab19/whm/workflow/result2/{0}".format(fasta_result1), shell=True)
    os.mkdir("/home/malab19/whm/workflow/result2/{0}".format(fasta_result1), 0755)
    for index, seq in enumerate(seqs):
        print(seq.id)
        if (index % 2) == 1:
            alignment_block_list.append(seq)
            SeqIO.write(alignment_block_list,
                        "/home/malab19/whm/workflow/result2/{0}/{1}".format(fasta_result1, str(seq.id).split("_")[2]),
                        "fasta")
            alignment_block_list = []
        else:
            alignment_block_list.append(seq)

#########################################################################################################
# path1 = "/home/malab19/Downloads/getorf on collection 2792"
# files1 = os.listdir(path1)
# """files is a list,it only contains the each file name in path"""
# for file1 in files1:
#     get_eachORF_alignment(file1)
#
# path2 = "/home/malab19/whm/workflow/result1"
# files2 = os.listdir(path2)
# for file2 in files2:
#     separate_files(file2)
