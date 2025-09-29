# Python file detection

import os

file_path='testos.txt'  ## relative file fath just need the name as in the same direcctory but  obselete file path needs the exact path

if os.path.exists(file_path): #### bolean by default true
    print(f'THis file {file_path} exists')

    #### to check if it is a file not a directory
    if os.path.isfile(file_path): ## by default True
        print('That is a file')

    elif  os.path.isdir(file_path):
        print('Dictory it is')

else:
    print("That location doesn't exists")


print('#################################################')

#########################################################

# Python writing files(.txt,.json,.csv)

txt_data='I like that stuff' ### content

file_path='outputs.txt' ## relative so it will be in the same directory

## to create file we will write the following
with open(file=file_path,mode='w') as file: ## mode == 'a' append new data
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")


## to write string from list

employees=['Spongebob','Squidward','Patrik','Eugene']
file_path='employee.txt'

with open(file_path,'w') as file:
    for employee in employees:
        file.write(employee+'\n') ### add new line
    print(f"txt file '{file_path}' was created")


### json file is made of key value pairs
import json
employees={
    'name':'Junayed',
    'age':'25',
    'profession':'cook'
}
file_path='output.json'

with open(file_path,'w') as file:
    ## to access json file use the dump method which converts the dictionary into json string
    json.dump(employees,file)
    print(f"json file '{file_path}' was created")




### writing CSv file

import csv

data=[['Name','Age','Profession'],
      ['junayed',45,'ML Engineer'],
      ['t.f',23,'Unemployed'],
      ['sandy',78,'Scientist']

      ]


file_path='data.csv'

with open(file_path,'w') as file:
    writer=csv.writer(file) ### create the csv file
    ## to iterate over every row to put the content
    for row in data:
        writer.writerow(row)
    print(f"txt file '{file_path}' was created")

print('##########################################################')

######################################################
## python reading files (.txt, .json , .csv)

file_path='C:\\Users\\ASUS\\PythonProject\\Beginner\\employee.txt'

with open(file_path ,'r') as file:
    content=file.read()
    print(content)

## read json

import json
file_path='output.json'

with open(file_path ,'r') as file:
    content=json.load(file)
    print(content)
    print(f" accessing value of key: {content['name']} ")

## csv read is content= csv.reader(file) then iterate it like for every line in content: print(line) ### row indexing by print(line[0])























