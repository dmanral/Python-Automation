import os
import send2trash

# os.unlink() will delete a file
# os.rmdir() will delete a folder (but the folder must be empty)
# shutil.rmtree() will delete a folder and all its contents
# send2trash.send2trash() will send  file or folder to the recycling bin

os.chdir('c:\\Users\\226250\\Desktop')

for filename in os.listdir():
    if filename.endswith('.PNG'):
        # os.unlink(filename)       # This will delete file(s). Also, this is permanent delete.
        print(filename)