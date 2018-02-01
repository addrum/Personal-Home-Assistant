# with thanks to https://github.com/mf-social/Home-Assistant/blob/master/extras/bash_scripts/upgrade-hass.sh

#!/bin/bash

###########################################
## This script upgrades the OS on my pi, ##
## upgrades HA then reboots the device   ##
## having pulled any config changes from ##
## Github if needed.                     ##
###########################################

sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
source /srv/homeassistant/bin/activate
pip3 install --upgrade homeassistant
sudo reboot
