Photocation
===============================

This small website will show the popular photos that were taken in the city and where the photographers took them with a simple click of a button.

## Getting Started

Clone the repository on your computer to run it locally. This is the instructions to run the app via a virtual Linux machine on a Windows computer.

## Instructions

Please ensure you have Python, [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed. This project uses a pre-congfigured Vagrant virtual machine which has the Flask server installed.

### Run the virtual machine

Using the terminal in the repository folder, type the following commands to launch your virtual machine.

```bash
$ cd /vagrant
$ vagrant up
$ vagrant ssh
```

### Run the App

Type the following commands to initialize the database and get the app running

```bash
$ python db0.py
$ python init.py
$ python project.py
```
Open 'localhost:5000' on your favorite browser

## Functionality

Read input from user and then return related photos on 500px.com

### Authentication & Authorization
* Page implements a third-party authentication & authorization service (Google Accounts)

### Permissions
* Button '500px' is not usable to non-users. Also, users are redirected to the login page when attempting to click that button


