

read -p "enter the username which you want to check:" username

if id "$username" &>/dev/null; then
    echo "$username" is exist
else
    echo " not exist"
fi