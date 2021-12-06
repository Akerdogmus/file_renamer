"""
# File Renamer
This script can be used for renaming files in folder. Before using, this script must be
inside the folder of will be renaming files.

### Created by AKE
"""

import os
import sys
import random
from os import listdir
from os.path import isfile, join

def main():
    """ Main function"""
    get_file_names()

def get_file_names():
    """
    This function using for getting file names in folder.
    """
    mypath = os.path.dirname(os.path.realpath(__file__))

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    func_num = input("Enter your rename option:\n1.Rename All with sequential "+\
        "numbers\n2.Rename All with random numbers\n3.Rename spesific files\nChoose one: ")

    if func_num == "1":
        rename_all_with_numbers(onlyfiles, mypath)
    elif func_num == "2":
        rename_all_with_random(onlyfiles, mypath)
    elif func_num == "3":
        # Spesific file name entrance
        rename_spesific_files()
    else:
        print("Please enter available mods number.")
        sys.exit()

def rename_all_with_numbers(files,mypath):
    """
    This function using for changing all file names with sequential numbers in the folder.
    """
    for i, fname in enumerate(files):
        if fname != str(os.path.basename(__file__)):
            old_name = str(mypath)+"/"+fname
            temp_new_name = str(i+1)+"."+str(fname.split(".",2)[1])
            if temp_new_name in os.listdir(mypath):
                print("Same name file in folder.")
                temp_new_name = "_"+str(temp_new_name)
            new_name = str(mypath)+"/"+str(temp_new_name)
            print(str(i)+". Old name ->"+old_name+"\nNew name ->"+ new_name)
            os.rename(old_name, new_name)

def rename_all_with_random(files, mypath):
    """
    This function using for changing all file names with random numbers in the folder.
    """
    for i, fname in enumerate(files):
        if fname != str(os.path.basename(__file__)):
            old_name = str(mypath)+"/"+fname
            temp_new_name = str(random.randrange(100000))+"."+str(fname.split(".",2)[1])
            if temp_new_name in os.listdir(mypath):
                print("Same name file in folder.")
                temp_new_name = "_"+str(temp_new_name)
            new_name = str(mypath)+"/"+str(temp_new_name)
            print(str(i)+". Old name ->"+old_name+"\nNew name ->"+ new_name)
            os.rename(old_name, new_name)

def rename_spesific_files():
    """Under-development"""

main()
