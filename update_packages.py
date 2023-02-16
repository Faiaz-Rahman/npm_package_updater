#!/usr/bin/env python3

print("The updater is RUNNNIG !!!")
print()

import subprocess
import os

curr_dir=os.getcwd()

print("Running the npm command for checking outdated packages ...")
print(f'Current Working Directory: <<< {curr_dir} >>>')
all_files_list=subprocess.run(args=['npm', 'outdated'], universal_newlines=True,stdout=subprocess.PIPE)

#lines=all_files_list.stdout.splitlines()

#all_files_list=str(all_files_list.stdout)

#Function that do the upgradation job ...
def upgrader(lst):
    txt=subprocess.run(args=lst,universal_newlines=True,stdout=subprocess.PIPE)
    print(txt.stdout)
    print()

#Function to trim the headers
def header(str_splitted):
    return str_splitted=='Wanted' or str_splitted=='Current'

files_list=all_files_list.stdout.splitlines()

command_as_str_list=[]

print()
print(f'(Upgradation can be manually done with following commands)')
print(f'==========================================================')

for lines in files_list:
    splitted_line=lines.split()
        
    if(header(splitted_line[1]) or header(splitted_line[2])):
        continue

    curr=splitted_line[1]
    wanted=splitted_line[2] 
    
    if(curr==wanted):
        continue
    else:
        version=wanted
        package_list=splitted_line[4]
        package_name=package_list[13:]
        
        command_str=f'npm install {package_name}@{version}'
        command_as_str_list.append(command_str)
        
        print(command_str)

print()
print(f'Executing the upgradation >>>')
print()

def main():
  for i in range(0, len(command_as_str_list)):
    #print(command_as_str_list[i])
    print(f'Running the command << {command_as_str_list[i]} >> ...')
    print(f'==============================================')
    print()
    lst=command_as_str_list[i].split()
    upgrader(lst)
    
main()