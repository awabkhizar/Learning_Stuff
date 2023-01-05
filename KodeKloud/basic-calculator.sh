#!/bin/bash
while true
do
        echo "1: Add"
        echo "2: Subtract"
        echo "3: Multiply"
        echo "4: Divide"
        echo "5: Quit"
        read -p "Enter your option " option
		
		if [ -z $option ]
        then
                echo "Select valid option, no option was selected"
                continue
        fi
		if [[ $option -lt 1 || $option -gt 5 ]]
        then
                echo "Select valid option, by selecting valid numbers"
                continue
        fi
		
		read -p "Enter Number1: " number1
		read -p "Enter Number2: " number2
        
        if [[ -z $number1 || -z $number2 ]]
        then
                echo "Enter valid numbers for calculation"
                continue
        fi

        if [ $option -eq 1 ]
        then
				echo "Answer=$(expr $number1 + $number2)"
                continue
        fi
        if [ $option -eq 2 ]
        then
                echo "Answer=$(expr $number1 - $number2)"
                continue
        fi
        if [ $option -eq 3 ]
        then
                echo "Answer=$(expr $number1 \* $number2)"
                continue
        fi
        if [ $option -eq 4 ]
        then
                echo "Answer=$(expr $number1 / $number2)"
                continue
        fi
        if [ $option -eq 5 ]
        then
                break
        fi
done