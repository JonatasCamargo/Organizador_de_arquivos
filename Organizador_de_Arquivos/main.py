import os

base_path = os.path.expanduser('~')

                                #directory of your choice
path = os.path.join(base_path, 'Downloads')

work_dir = os.chdir(path)

list_files = os.listdir(work_dir)


type_files = ['exe', 'csv', 'jpg', 'pdf', 'zip', 'txt', 'py', 'xlsx']
for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)


for file in list_files:
    for type in type_files:
        if '.' +type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)