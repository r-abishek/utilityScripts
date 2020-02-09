#!/bin/bash

sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates gnupg software-properties-common wget
wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | sudo apt-key add -

#sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ xenial main'

sudo apt-get update

#sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic-rc main'
sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ xenial-rc main'

sudo apt-get update

sudo apt-get install kitware-archive-keyring
sudo apt-key --keyring /etc/apt/trusted.gpg del C1F34CDD40CD72DA

