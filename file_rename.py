import os
import re

pattern = re.compile(r'\((.*?)\)')
dir_files = os.listdir()
dir_files = [filee for filee in dir_files if filee[0:2]=='da']
for filee in dir_files:
    old_name = filee
    topic = re.findall(pattern,old_name)[0]
    idx = old_name.index('(')
    day = old_name[3:idx]
    if len(day)==1:
        day = '0'+day
    new_name = 'day'+day+"_"+topic+"_"
    os.rename(old_name,new_name)
