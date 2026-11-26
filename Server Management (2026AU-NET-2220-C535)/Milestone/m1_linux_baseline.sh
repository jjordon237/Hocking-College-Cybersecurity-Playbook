#!/bin/bash
# NET2220 Milestone 1 Linux baseline
# Setup commands collated from the recorded lab work.
# Initial build on a fresh course server, using ec2-user with sudo.
# Accounts and groups already exist on the current course server.
# This file is not a rollback script and has not been run as a complete script.

# Create the local role groups and test accounts.
sudo groupadd m1readers
sudo groupadd m1operators
sudo useradd -m -G m1readers m1reader
sudo useradd -m -G m1readers,m1operators m1operator
sudo useradd -m m1retired

# Create the course folders and the published notice.
sudo mkdir -p /srv/courselab/published /srv/courselab/working
echo 'Team Notice' | sudo tee /srv/courselab/published/notice.txt

# Set ownership and permissions for Published.
sudo chown -R root:m1readers /srv/courselab/published
sudo chmod 2750 /srv/courselab/published
sudo chmod 640 /srv/courselab/published/notice.txt

# Set ownership and permissions for Working.
sudo chown root:m1operators /srv/courselab/working
sudo chmod 2770 /srv/courselab/working

# Disable the retired account by locking, expiring, and setting nologin.
sudo usermod -L -e 1 -s /sbin/nologin m1retired

# Recorded read-only verification commands.
id; hostname; date
ls -ld /srv/courselab/published /srv/courselab/working
id m1reader
id m1operator
getent passwd m1retired
sudo passwd -S m1retired
sudo chage -l m1retired
