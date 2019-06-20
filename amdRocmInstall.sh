sudo apt update
sudo apt dist-upgrade
sudo apt install libnuma-dev
sudo reboot

wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
echo 'deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main' | sudo tee /etc/apt/sources.list.d/rocm.list

sudo apt update
sudo apt install rocm-dkms

groups

sudo usermod -a -G video $LOGNAME

echo 'ADD_EXTRA_GROUPS=1' | sudo tee -a /etc/adduser.conf
echo 'EXTRA_GROUPS=video' | sudo tee -a /etc/adduser.conf

/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/x86_64/clinfo
