@echo off
sdemon -o kill -t all -s roc-a-a07 -i 5151
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters 1 true
exit