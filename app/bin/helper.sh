#!/usr/bin/env bash

COR_BRANCO='\033[00;37m'
COR_VERMELHO='\033[00;31m'
COR_VERDE='\033[00;32m'
COR_AMARELO='\033[00;33m'
COR_AZUL='\033[00;34m'

COLOR_DEFAULT='\033[00;37;40m'
COLOR_SUCCESS='\033[00;30;42m'
COLOR_ERROR='\033[00;30;41m'


function success(){
	echo -e "$COLOR_SUCCESS"
	echo "$1 [OK]"
	echo -e "$COLOR_DEFAULT"
}

function error(){
	echo -e "$COLOR_ERROR"
	echo "$1 [Error]"
	echo -e "$COLOR_DEFAULT"

}
