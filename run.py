import os 
import json
import sys
sys.path.append('src')
from etl import *
import subprocess

def main():
    
    args = sys.argv
    
    if (len(args) > 1):
        if (args[1] == "test"):
            
            # Test project
            dictionary = json.load(open("config/test_params.json"))
            create_folders()
            subset = get_subset(dictionary['read_1'],dictionary['read_2'],dictionary['subset_size'])
            fastqc(dictionary,subset)
            kallisto(dictionary,subset)
            return
        
        elif (args[1] == "clean"):
            print("cleaning...")
            clean()
            print("cleaned!")
            return
    else:
        dictionary = json.load(open("config/params.json"))
    
        #Full Project
        create_folders()
        subset = get_subset(dictionary['read_1'],dictionary['read_2'],dictionary['subset_size'])
        fastqc(dictionary,subset)
        kallisto(dictionary,subset)
        return
    
if __name__ == '__main__':
    main()