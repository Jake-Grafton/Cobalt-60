# Cobalt-60 | Drop and Run
A framework that utilizes ZerBea's hcxdumptool and hcxtool for automating the attacking of networks.
## Installation
When ran, the installation script will provide the needed information.
```
git clone https://github.com/Jake-Graton/Cobalt-60 && cd ./Cobalt-60 && sudo bash ./install.sh
```
## Uninstallation
When ran, the uninstallation script will remove the /usr/local/bin/C60 symlink, and then delete all files in the Cobalt-60 directory.
```
sudo bash ./uninstall.sh
```
### Why did you make this?
This was a project that I started to improve the workflow of auditing wireless networks. I found that I liked hcxdumptool, but it took too long to figure out what options made the attacks more effective, so I designed this framework to help me accomplish that.
I also just wanted to make something cool. :)
