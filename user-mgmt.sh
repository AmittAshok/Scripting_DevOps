

read -p "enter the username which you want to check:" username

if id "$username" &>/dev/null; then
    echo "$username" is exist
else
    echo "not exist"
fi

#Create New user

read -p "Enter the username which you want to Create:" username1
useradd -m "$username1"
if id "$username1" &>/dev/null; then
	echo "$username1" created successfully
else
	echo "Error in creating user"
fi	
