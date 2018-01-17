#!/bin/bash

# This script is called directly from the Vagrantfile

## general config ##

#vagrant config?
export DEBIAN_FRONTEND=noninteractive
set -e # Exit script immediately on first error.
set -x # Print commands and their arguments as they are executed.

#update package manager resources
sudo apt-get update -y

#set time zone
area="America"
zone="New_York"
sudo echo "$area/$zone" > /tmp/timezone
sudo cp -f /tmp/timezone /etc/timezone
sudo cp -f /usr/share/zoneinfo/$area/$zone /etc/localtime

## end general config ##

## main server installs ##

#basics (bjd- needed?)
sudo apt-get install -y git-core mercurial vim screen wget curl raptor-utils unzip
sudo apt-get install -y tree
sudo apt-get install -y python-pip
#sudo pip install iPython

#apache
sudo apt-get install -y apache2

#System Python (2.7)
sudo apt-get install -y python python-dev python-mysqldb python-lxml python-virtualenv
sudo apt-get install -y libmysqlclient-dev

sudo apt-get install -y python-software-properties #required for add-apt-repository command below
sudo apt-get update -y

#MySQL
echo mysql-server mysql-server/root_password password vagrant | sudo debconf-set-selections
echo mysql-server mysql-server/root_password_again password vagrant | sudo debconf-set-selections
sudo apt-get install -y mysql-server
sudo apt-get install -y mysql-client

#lxml dependencies -- loaded later from requirements.txt
apt-get -y install libxml2-dev libxslt-dev

## end main server installs

#install necessary python packages for the EAFSD
sudo pip install -r /home/vagrant/ProjectQuincy/requirements.txt

#install testing packages COMMENT OUT IN PRODUCTION
sudo pip install -r /home/vagrant/ProjectQuincy/dev-requirements.txt


# ## set up and populate database ##

mysql -uroot -pvagrant -e "DROP DATABASE IF EXISTS eafsd;"
#create the database for the django project
#matches the settings_PROJECT.py file copied from the shared folder
mysql -uroot -pvagrant -e "CREATE DATABASE IF NOT EXISTS eafsd DEFAULT CHARACTER SET utf8;"

##clone ProjectQuincy code from github

cd /home/vagrant/ProjectQuincy
# git clone https://github.com/jabauer/projectquincy.git ProjectQuincy


## create database

mysql -uroot -pvagrant eafsd < /home/vagrant/ProjectQuincy/2017-05-26_eafsd_dump.sql

echo "---"
echo "---"
echo "Box provisioned! Now log into vagrant, start the dev server and you'll be able to see The Early American Foriegn Service Database!"
echo "---"
echo "---"

exit
