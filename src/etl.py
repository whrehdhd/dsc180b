import os
import json
import glob
import numpy as np 
import pandas as pd
import subprocess

def create_folders():
    if not os.path.isdir('data'):
        os.system('mkdir data')
    if not os.path.isdir('data/fastqc_results'):
        os.system('mkdir data/fastqc_results')
        os.system('mkdir data/fastqc_results/esbl')
        os.system('mkdir data/fastqc_results/ctrl')
    if not os.path.isdir('data/cutadapt'):
        os.system('mkdir data/cutadapt')
    if not os.path.isdir('data/kallisto'):
        os.system('mkdir data/kallisto')
    return 

def clean():
    if os.path.isdir('data'):
        os.system('rm -R data')
    return

def fastqc(dictionary):
    
    esbl = glob.glob(dictionary['esbl_1'])
    ctrl = glob.glob(dictionary['ctrl_1'])
    
    for sample in esbl:
        s1 = sample
        s2 = sample.replace("_1.","_2.")
        command1 = "/opt/FastQC/fastqc " + s1 + " --outdir=data/fastqc_results/esbl/"
        command2 = "/opt/FastQC/fastqc " + s2 + " --outdir=data/fastqc_results/esbl/"

        os.system(command1)
        os.system(command2)
        
    for sample in ctrl:
        s1 = sample
        s2 = sample.replace("_1.","_2.")
        command1 = "/opt/FastQC/fastqc " + s1 + " --outdir=data/fastqc_results/ctrl/"
        command2 = "/opt/FastQC/fastqc " + s2 + " --outdir=data/fastqc_results/ctrl/"

        os.system(command1)
        os.system(command2)

    zip_esbl = glob.glob("data/fastqc_results/esbl/"+"*.zip")
    zip_ctrl = glob.glob("data/fastqc_results/ctrl/"+"*.zip")

    for file in zip_esbl:
        os.system(f"unzip {file} -d data/fastqc_results/esbl/unzipped")
        
    for file in zip_ctrl:
        os.system(f"unzip {file} -d data/fastqc_results/ctrl/unzipped")
        
    return

def cutadapt(dictionary,subset):

    for sample in subset:
        s1 = sample.replace("_2.","_1.")
        f1 = s1.split('/')[-1]

        s2 = sample
        f2 = s2.split('/')[-1]

        command1 = f"cutadapt -j 4 -a {dictionary['adapter_sequence']} -o data/cutadapt/{f1} {s1}"
        command2 = f"cutadapt -j 4 -a {dictionary['adapter_sequence']} -o data/cutadapt/{f2} {s2}"

        os.system(command1)
        os.system(command2)
        
    return