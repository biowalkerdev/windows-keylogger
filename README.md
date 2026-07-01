## Disclaimer
**THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL PURPOSES ONLY**  
THE AUTHOR DOES NOT CONDONE, ENDORSE, OR ENCOURAGE ANY ILLEGAL ACTIVITY  
THE USER IS SOLELY RESPONSIBLE FOR COMPLYING WITH ALL LOCAL LAWS AND REGULATIONS IN THEIR JURISDICTION  

## Usage
Go to the scripts folder, run ``cryptokey_generator.py`` on terminal with overwriting  
Once the cryptokey is received, it will be automatically written to the cryptokey.txt file  
Also, don't forget to download dependencies using req_linux.sh or req_windows.bat  
On Windows:  
Just double-click on ``req_windows.bat``  

On Linux:  
```bash
bash req_linux.sh
```
Also you can change something in ``config.yaml``

After change variable IP to yours and VALUE_NAME to which you want in ``keylogger.py``  
Then build the ``keylogger.py`` to .exe by using ``build.bat`` script in terminal.  
```batch
build.bat <Filename of .exe>
```
> ⚠️ Warning! You cant build into .exe on linux using PyInstaller  
> If you are on Linux, run the script through Wine

The dist folder will contain the finished .exe file  

Once you've built the .exe, create a new zip archive and copy this files into it:
- config.yaml
- cryptokey.txt
- Your builded .exe  
After that, run ``server.py``, send the archive to someone  
And after the victim opens your .exe, the keylogger will be installed in the startup and will transmit all keystrokes to you.

## Functional
- All inputs are saving to log.txt
- Autostart
- Traffic Encryption

## Requirements
- Python
- pynput
- pyyaml
- colorama
