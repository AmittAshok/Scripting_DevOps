# While assign varibale in shell don't give any space inbetween


var1() {

    name="Mukta"
    age="6years"
    # when variable is used in statmemt it used with $ sign
    echo " My name is $name and I am $age old"
}


var_read_user(){
    read -p "Enter your name:" name1
    # while giving input value in variable, without $ sign
    read -p "Enter your age:" age1
    echo "My name is "$name1" and i am "$age1" year old.."
}

file_checker(){
    read -p "Enter the file location:" file_name
    # for file use -e for file format
    if [ -e "$file_name" ]; then
        echo " File is Present"
    else
        echo " File is not Present"
    fi
        
}

dir_checker(){
    read -p "Enter the Dir name:" dir_name
    if [ -d "$dir_name" ] ; then
        echo " Dir present "
    else
        echo "Dir not present"
    fi
}

loop_for() {
    fruits="apple,mango,bananan"
    for fruit in $fruits;
       do
        echo $fruit
    done 
}
calculate_sum() {

    read -p "Enter the last number:" num
    # number 10 
    # 1 2 3 4 5 6 7 8 9 
    sum=0
    # Result is set as zero
    # here for loop is in double (()) always
    for ((i=1;i<=$num;i++)); 
    do
    sum=$((sum+i))
    done
    echo "$sum"
}

word_search() {

    pattern="INFO"
    file_name="/home/amitt-ashok/shell_script/log.txt"
    # here -o search for exact word and -w search for word in between bigword
    result=$( grep -o -w "$pattern" "$file_name" | wc -l )
    echo "$result"
}

read_file() {

    file_name="/home/amitt-ashok/shell_script/log.tx"

    if [ -e $file_name ]; then
        while IFS= read -r line; do
    echo "Read Line :" $line
    done
    else
    echo "file is not present"
    fi
}

total_size(){
    read -p "Enter the name of Directory:" dir
    size=$(du -csh $dir| awk '{print $1}')
    echo "$size"
}
#var1
#var_read_user
#file_checker
#dir_checker
#loop_for
#calculate_sum
#word_search
#read_file
total_size