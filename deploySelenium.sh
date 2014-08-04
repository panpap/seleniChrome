wget http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip
unzip chromedriver_linux*
rm chromedriver_linux*
sudo chmod a+x /usr/bin/chromedriver
apt-get -f install
sudo apt-get install python-pip
sudo pip install selenium
sudo pip install pyvirtualdisplay
sudo mv chromedriver /usr/bin/
sudo apt-get install libcurl3 libnspr4-0d libxss1
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#wget http://95.31.35.30/chrome/pool/main/g/google-chrome-stable/google-chrome-stable_33.0.1750.152-1_amd64.deb
sudo dpkg -i google-chrome*; rm google-chrome*
apt-get -f install
sudo apt-get install xvfb
Xvfb :1 -screen 5 1024x768x8 &
export DISPLAY=:1.5
