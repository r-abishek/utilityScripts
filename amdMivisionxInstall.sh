git clone --recursive https://github.com/GPUOpen-ProfessionalCompute-Libraries/MIVisionX.git
cd MIVisionX

sudo python MIVisionX-setup.py

mkdir build
cd build
cmake ../
make -j$(nproc)
sudo make install
