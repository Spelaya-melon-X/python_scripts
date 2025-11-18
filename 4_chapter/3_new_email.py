import subprocess

url = "https://mail.google.com/mail/u/0/#inbox?compose=new"

subprocess.call(['open', '-a', 'Google Chrome', url])
