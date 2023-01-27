#This Script id created by DEVIL
#Don't copy or modify code Read License First
#follow me on fb page https://www.facebook.com/DEVIL.NAJMUL
clear
echo ""
echo -e"< ━━━━━━━━━━━━ [★] 𖧷𖧷👿𝐇.𝐀.𝐂.𝐊.𝐄.𝐑.𝐒👿 𖧷𖧷[★] ━━━━━━━━━━━━ >  "

echo "                [𝐀𝐃𝐌𝐈𝐍] 𝐌𝐑.𝐍𝐀𝐘𝐀𝐍 [𝐂𝐄𝐎] 𝐃𝐄𝐕𝐈𝐋 𝐍𝐀𝐉𝐌𝐔𝐋 "

echo -e "         \e[1;91m__\e[1;92m,-\e[1;93m////\e[1;92m, "
echo -e "        \e[1;91m/__\e[1;92m) (\e[1;93mo\e[1;92m) ) "
echo -e "          /.,--. \       "
echo -e "         /,-'/.\. \      "
echo -e "         \.  \.\ \ \     "
echo -e "          \.  \\\ \  /   "
echo -e "      \e[1;93m=====\e[1;91m((\e[1;93m=\e[1;91m((\e[1;92m\\e[1;93m=====.=== "
echo -e "           \e[1;92m    \ \ \.\   "
echo -e "                \ \ \'     "
echo -e "                 \ \'      "
echo -e "                  \ \     "
echo -e "                   '-'    \e[1;97m "

echo -e "
	                        Ethical Hacker
   < ━━━━━━━━━━━━━━━ [😈] 𝐃𝐄𝐕𝐈𝐋  𝐒𝐐𝐔𝐀𝐃  [😈] ━━━━━━━━━━━━━━━ > "
echo ""
echo -e "\e[1;91m [+] Fb page: \e[1;92mDevil Najmul"
echo -e "\e[1;91m [+] Github: \e[1;92mN41M01\e[1;97m"
echo ""
read -p " Does you want to Uninstall Parrot Shell?(Yes/No) : " input

if [[ $input == Yes || $input == yes || $input == y || $input == Y ]]; then
    clear
    cp default $HOME
    cd $HOME
    mv default bash.bashrc
    cd /data/data/com.termux/files/usr/etc
    rm -rf bash.bashrc
    cd $HOME
    mv bash.bashrc /data/data/com.termux/files/usr/etc
    cd $HOME
    echo -e "\e[1;91mSuccessfully Uninstalled"
    echo -e "Restart Termux"
    exit  3
elif [[ $input == No || $input == no || $input == n || $input == N ]]; then
exit 2
else
echo -e "\e[1;91mInvalid Option"
exit 1
fi
