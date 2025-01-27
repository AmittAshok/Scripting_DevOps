#!/bin/bash
#$---User management such create user, set random password and set policy where user need to change password on login

# Checking for root access or sudo access
if [ ${UID} -ne 0 ];
then
	echo "Please run command with root or with sudo access..."
	exit 1
fi
# User Should provide atlease one argument, else guide to add it
if [ $# -eq 0 ];
then
	echo "Provide atleast one argument such as User name...${0} USER_NAME [comment].."
	echo "Create user with name USER_NAME and comment field of COMMENT"
	exit 1
fi

# Store First argument as User_name
USER_NAME=${1}
echo "${USER_NAME}"

# Check for second argument and store in comment section
shift
comment=${@}
echo "$comment"
# Create Random password

PASSWORD=$(date +%s%N)
echo "$PASSWORD"

# Create User
useradd -c "$COMMENT" -m $USER_NAME

# check if user create successfully
if [[ $? -ne 0 ]];
then
	echo "User ${USER_NAME} could not be created..."
	exit 1
fi

# Set a password for user
echo "${USER_NAME}:${PASSWORD}" | sudo chpasswd
echo "Password for $USER_NAME has been set..."

# Force to reset password at first login for user
sudo passwd -e $USER_NAME

# Display all the details

echo "####### USER DETAILS ############"
echo "USERNAME : $USER_NAME "
echo "TEAM : $comment "
echo "PASSWORD : $PASSWORD "
echo 
echo "HOSTNAME : $(hostname) "


	
