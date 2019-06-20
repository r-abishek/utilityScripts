echo "OpenCV installation by learnOpenCV.com"

# Homebrew install
brew update
echo "# Homebrew" >> ~/.bash_profile
echo "export PATH=/usr/local/bin:$PATH" >> ~/.bash_profile
source ~/.bash_profile






# If installing python for the first time using Homebrew, 
# else skip the 3 lines below and upgrade. 
brew install python python3
brew link python
brew link python3
 
# NOTE : If you have python already installed using homebrew, 
# it might ask you to upgrade.
# Upgrade the python using new homebrew formulae.
brew upgrade python
brew upgrade python3
 
# Check whether Python using homebrew install correctly
which python2  # it should output /usr/local/bin/python2
which python3  # it should output /usr/local/bin/python3
 
# Check Python versions
python2 --version
python3 --version







# Install virtual environment
pip install virtualenv virtualenvwrapper
echo "# Virtual Environment Wrapper"
echo "VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python2" >> ~/.bash_profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bash_profile
source ~/.bash_profile

############ For Python 2 ############
# Create virtual environment
mkvirtualenv facecourse-py2 -p python2
workon facecourse-py2

# Now install python libraries within this virtual environment
pip install numpy scipy matplotlib scikit-image scikit-learn ipython pandas

# Quit virtual environment
deactivate
######################################

############ For Python 3 ############
# Create virtual environment
mkvirtualenv facecourse-py3 -p python3
workon facecourse-py3

# Now install python libraries within this virtual environment
pip install numpy scipy matplotlib scikit-image scikit-learn ipython pandas

# Quit virtual environment
deactivate
######################################



