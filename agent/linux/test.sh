last > result.txt

last reboot

# grep -ri shutdown /var/log/messages

uptime -s

date +"%Y-%m-%d %I:%M:%S" --date=@$(expr `date +%s` - `cut -d "." -f 1 /proc/uptime`)

