echo "OpenCV installation by learnOpenCV.com"

#Specify OpenCV version
cvVersion="3.4.4"
echo "OpenCV version:"
echo $cvVersion

# Clean build directories
echo "Cleaning build directories..."
rm -rf opencv/build
rm -rf opencv_contrib/build

# Create directory for installation
echo "Creating directory for installation..."
mkdir installation
mkdir installation/OpenCV-"$cvVersion"

# Save current working directory
echo "Saving current working directory..."
cwd=$(pwd)

# Update packages
echo "Updating packages..."
sudo apt -y update
sudo apt -y upgrade

# Install OS libraries and dependencies
echo "Installing OS libraries and dependencies..."
sudo apt -y remove x264 libx264-dev
sudo apt -y install build-essential checkinstall cmake pkg-config yasm
sudo apt -y install git gfortran
sudo apt -y install libjpeg8-dev libjasper-dev libpng12-dev
sudo apt -y install libtiff5-dev
sudo apt -y install libtiff-dev
sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo apt -y install libxine2-dev libv4l-dev
cd /usr/include/linux
sudo ln -s -f ../libv4l1-videodev.h videodev.h
cd $cwd
sudo apt -y install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt -y install libgtk2.0-dev libtbb-dev qt5-default
sudo apt -y install libatlas-base-dev
sudo apt -y install libfaac-dev libmp3lame-dev libtheora-dev
sudo apt -y install libvorbis-dev libxvidcore-dev
sudo apt -y install libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt -y install libavresample-dev
sudo apt -y install x264 v4l-utils
 
# Install optional dependencies
echo "Installing optional dependencies..."
sudo apt -y install libprotobuf-dev protobuf-compiler
sudo apt -y install libgoogle-glog-dev libgflags-dev
sudo apt -y install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen

# Install python libraries
echo "Installing python libraries..."
sudo apt -y install python3-dev python3-pip python3-venv
sudo -H pip3 install -U pip numpy
sudo apt -y install python3-testresources

cd $cwd

############ For Python 3 ############

# create virtual environment
python3 -m venv OpenCV-"$cvVersion"-py3
echo "# Virtual Environment Wrapper" >> ~/.bashrc
echo "alias workoncv-$cvVersion=\"source $cwd/OpenCV-$cvVersion-py3/bin/activate\"" >> ~/.bashrc
source "$cwd"/OpenCV-"$cvVersion"-py3/bin/activate
 
# now install python libraries within this virtual environment
pip install wheel numpy scipy matplotlib scikit-image scikit-learn ipython dlib

# quit virtual environment
deactivate

######################################

# Download opencv and opencv_contrib
echo "Downloading opencv and opencv_contrib..."
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout $cvVersion
cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout $cvVersion
cd ..

# Compile and install OpenCV with contrib modules
echo "Compiling and install OpenCV with contrib modules..."
cd opencv
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
            -D CMAKE_INSTALL_PREFIX=$cwd/installation/OpenCV-"$cvVersion" \
            -D INSTALL_C_EXAMPLES=ON \
            -D INSTALL_PYTHON_EXAMPLES=ON \
            -D WITH_TBB=ON \
            -D WITH_V4L=ON \
            -D OPENCV_PYTHON3_INSTALL_PATH=$cwd/OpenCV-$cvVersion-py3/lib/python3.5/site-packages \
        -D WITH_QT=ON \
        -D WITH_OPENGL=ON \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
        -D BUILD_EXAMPLES=ON ..

make -j$(nproc)
make install

# Using OpenCV in C++ with CMakeLists.txt
# SET(OpenCV_DIR /home/soundar/installation/OpenCV-3.4.4/share/OpenCV/)
# mkdir build
# cd build
# cmake ..
# cmake --build . --config Release

# Compiling a file
# g++ `pkg-config --cflags --libs <OpenCV_Home_Dir>/installation/OpenCV-3.4.4/lib/pkgconfig/opencv.pc` my_sample_file.cpp -o my_sample_file
