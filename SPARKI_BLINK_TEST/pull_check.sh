#!/bin/bash
zero=0
result=$(git remote show origin | grep -c 'up to date')
if [ $result != $zero ]
then
python ~/SPARKI-Reborn/Python/TURN_ON_LED.py	
fi
