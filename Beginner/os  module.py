import os
if (not os.path.exists('data')):
    os.mkdir('data') ## make directory in the current folder path

''' for i in range(0,5):
    os.mkdir(f'data/day{i+1}') '''

''' for i in range(0,5):
    os.rename(f"data/day{i+1}",f"data/Tuitorial{i+1}")'''

#### lisiting all the folder present

folders=os.listdir('data')
print(folders)

###### show current directory
print(os.getcwd())