# python_auto_email
Just a simple script to automate emails in python.

Few things you need to do before starting/using this script:

You need to create an apppassword for your google account so this app can bypass the 2-factor authentication <b>you should</b> have on for your gmail account.

You can create an apppassword for you google account by doing the following:
  - STEP 1: Go to https://myaccount.google.com/apppasswords and then loggin to the google account you are using.
  - STEP 2: On Select App dropdown menu select <b>mail</b> and on the Select Device dropdown menu select select <b>other</b> and give it a 
            name such as Python Email App. 
  - STEP 3: Copy/screen shot the created password and use it for below.


I am using environment variables because you don't want random people to see important information if you were to share this code.

This is how you add environment variables in MACOS. (I am sure you can find a Windows version somewhere.)
  - STEP 1: Open terminal. (Make sure you are on the home directory by typing "cd" without the quotes and hitting <b>enter</b>.)
  - STEP 2: Open file to set environment variables. You have to be able to edit it so open it using a terminal editor such as nano. 
            Type in "nano .bash_profile" without the quotes and hit <b>enter</b>.
  - STEP 3: Just on the top of the file add the following:
  
              - export EMAIL_USER="youremail@gmail.com"
              
              - export EMAIL_PASS="your apppassword from gmail apppasswords"
              
  - STEP 4: Hit <b>control x</b> and then <b>y</b> to save and then <b>enter</b> to keep the same name

You now have two environment variables called EMAIL_USER and EMAIL_PASS.

<b>Now you can use the script as provided.</b>

Source:
  - Corey Schafer's youtube videos. He is amazing.
