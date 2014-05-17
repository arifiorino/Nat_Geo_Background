@echo off
sdemon -o kill -t all -s roc-a-a07 -i 5151
reg add "hkcu\control panel\desktop" /v wallpaper /t REG_SZ /d "C:\final.png" /f 
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters 1 true
exit