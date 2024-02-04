echo "Setup Docker"
sudo apt-get -y update
sudo apt-get -y install tree
sudo apt -y install docker.io

sudo systemctl start docker
sudo systemctl enable docker
