import subprocess
import os

# Открываем Rutube в Chrome как отдельное окно (без адресной строки)
cmd = """
osascript -e 'tell application "Google Chrome"
    if it is running then
        tell window 1
            make new tab with properties {URL:"https://rutube.ru"}
        end tell
    else
        open location "https://rutube.ru"
    end if
    activate
end tell'
"""

subprocess.call(cmd, shell=True)