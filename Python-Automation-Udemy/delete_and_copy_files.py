import os, shutil

for folderName, subfolders, filenames in os.walk('C:\\Users\\226250\\Desktop\\Learn'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'to_delete' in subfolder:
            os.rmdir(subfolder)
            print('rmdir on ' + subfolder)
    
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))