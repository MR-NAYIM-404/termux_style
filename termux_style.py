# VIRUS TEAM-NSN
# -*- coding: utf-8 -*-

import os
import time
import sys
 
os.system('apt update')
os.system('apt upgrade -y')
os.system('pkg install figlet -y')
os.system('pkg install ncurses-utils -y') 
os.system('pkg install ruby -y')
os.system('gem install lolcat')
 
output = '/data/data/com.termux/files/usr/etc/'
 
print('')
name = raw_input(' \x1b[1;97m WHATS YOUR BANNER NAME :> \x1b[38;5;46m  ')
 
wlc = '''
import os,sys,time,random
print("")
print("")
color = ["\\033[1;31m","\\033[1;32m"]
m = random.choice(color)+"Welcome {} \\n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
print("")
        '''.format(name)
 
h1 = open(output+'wlc.py', 'w')
h1.write(wlc)
h1.close()
 
bashrc1 = '''
clear
echo
 
 echo "  < ━━━━━━━━━━━━ [★] 𖧷𖧷👿𝐇.𝐀.𝐂.𝐊.𝐄.𝐑.𝐒👿 𖧷𖧷[★] ━━━━━━━━━━━━ >  " |lolcat
    echo "
                 [★] 𖧷𖧷 𝐖𝐄 𝐃𝐎 𝐍𝐎𝐓 𝐇𝐀𝐂𝐊 𝐓𝐎 𝐈𝐌𝐏𝐑𝐄𝐒𝐒 𖧷𖧷[★] 
                 [★] 𖧷𖧷 𝐖𝐄 𝐇𝐀𝐂𝐊 𝐓𝐎 𝐄𝐗𝐏𝐑𝐄𝐒𝐒....𖧷𖧷[★] " |lolcat
'''
 
bashrc2 = '''
echo "
                 [★] 𖧷𖧷 𝐘𝐎𝐔 𝐖𝐈𝐋𝐋 𝐑𝐄𝐌𝐄𝐌𝐁𝐄𝐑 𖧷𖧷[★] 
                 [★] 𖧷𖧷 𝐂.𝐄.𝐎 𖧷𖧷𝐃𝐄𝐕𝐈𝐋 𝐍𝐀𝐉𝐌𝐔𝐋  𖧷𖧷[★] 

  < ━━━━━━━━━━━━ [★] 𖧷𖧷👿𝐇.𝐀.𝐂.𝐊.𝐄.𝐑.𝐒👿 𖧷𖧷[★] ━━━━━━━━━━━━ > " |lolcat
 
python /data/data/com.termux/files/usr/etc/wlc.py
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
 
#PS1="\\033[1;31m𝐕𝐈𝐑𝐔𝐒~#"
 
PS1="\[\e[1;34m┌──\\a─T─I─M─E─\\a──┐\\033[1;34m\\a┌──\\a─D─A─T─E─\\a───>\\033[1;34m
\\a┌─[\\033[1;93m \@\\033[1;34m ]──[\\033[1;93m \d\\033[1;34m ]\\033[1;34m
\\a├─[\\033[1;32m\w\\033[1;34m]\\033[1;34m
'''
 
h2 = open(output+'bash.bashrc', 'w')
h2.write(bashrc1)
h2.write("\nfiglet -f slant    '    "+name+"' |lolcat\n")
h2.write(bashrc2)
h2.write('\[\e[34m\]└─>\[\e[35m\]'+name+'\[\e[34m\][~]:#\[\e[1;32m\] "\n')
h2.write('echo -e "\e[6 q"')
h2.close()
print('DONE')
 
