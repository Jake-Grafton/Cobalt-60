#!/bin/bash
if ! command -v apt &> /dev/null
then
	echo "This installer is designed for apt usage. Please install hcxdumptool, hcxtools, and python3 via package manager or source, then rerun this script."
	exit
elif ! command -v hcxdumptool &> /dev/null
then
	exec apt -y install hcxdumptool
elif ! command -v hcxpcapngtool &> /dev/null
then
	exec apt -y install hcxtools
elif ! command -v python3 &> /dev/null
then
	exec apt -y install python3
fi
ln -s ./cobalt-60.py /usr/local/bin/C60
echo "Installation complete! Execute via the command python3 C60"
