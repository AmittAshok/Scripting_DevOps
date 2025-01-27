read -p "enter the numbers separted by comma:" -a numbers

max=${numbers[0]}

for num in "${numbers[@]}"; do
    if (( num > max )); then
        max=$num
    fi
done

echo "Maximum number is : $max"
