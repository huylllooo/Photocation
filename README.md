Multi User Blog
===============================

A multi user blog application using Google App Engine and Jinja. Users can post blog posts after signing in. Also they are able to leave 'Like' and 'Comment' on others' posts on the blog.

## Getting Started

Clone the repository on your computer to run it locally

## Instructions

Please ensure you have Python, Vagrant and VirtualBox installed. This project uses a pre-congfigured Vagrant virtual machine which has the Flask server installed.

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

### API Endpoints
* JSON endpoints can be accessed from the following routes
```bash
'/category/JSON'
'/category/<int:category_id>/menu/JSON'
'/category/<int:category_id>/menu/<int:menu_id>/JSON'
```


### CRUD
* Read: Reads category and item information from a database.
* Create: Includes a form allowing users to add new items and correctly processes submitted forms.
* Update: Include a form to edit/update a current record in the database table and correctly processes submitted forms.
* Delete: Include a function to delete a current record.

### Authentication & Authorization
* Page implements a third-party authentication & authorization service (Google Accounts)
* Create, delete and update operations do consider authorization status prior to execution.

### Permissions
* Post Edit or Delete are not visible to non-users. Also, users are redirected to the login page when attempting to create, post comment or like a blog post.
* Logged in users can create, edit, or delete blog posts they themselves have created.


