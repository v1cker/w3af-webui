=======================
w3af Web User Interface
=======================

Intro
=====

This project provides web interface for w3af (http://w3af.org/) and is mostly built on:

* Django (https://www.djangoproject.com/).
* Celery (http://celeryproject.org/)

The main repository for the `w3af project <https://github.com/andresriancho/w3af/>`_ can be found `w3af project <https://github.com/andresriancho/w3af/>`_.


Install
=======

Install required dependences:

* w3af-console
* MySQL                 apt-get install python-mysqldb mysql-server-5.1
* lxml                  apt-get install python-lxml
* django_extensions     easy_install django-extensions
* south                 easy_install south
* ghettoq               easy_install ghettoq
* celery                easy_install celery
* djcelery              easy_install django-celery
* djkombu               easy_install django-kombu
* django                Download version 1.4 from https://www.djangoproject.com/
* cronex                Download from https://github.com/jameseric/cronex

These commands should help you with the installation process, please run from the w3af_webui 
root directory (where setup.py lives): ::

    sudo easy_install django-kombu django-celery celery ghettoq south django-extensions
    sudo apt-get update
    sudo apt-get install python-mysqldb python-lxml mysql-server-5.1
    git clone git://github.com/jameseric/cronex.git
    cd cronex
    cp cronex.py `python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
    cd ..
    sudo python setup.py install

Make database init: ::

    mysql -u root -p
    CREATE DATABASE w3af_webui CHARACTER SET utf8; 
    CREATE user w3af_webui@localhost IDENTIFIED BY "w3af_webui"; 
    GRANT ALL ON w3af_webui.* TO w3af_webui@localhost;
    FLUSH PRIVILEGES;

Dont forget to edit /etc/mysql/my.cnf: ::

     [mysqld]
     ...
     transaction-isolation  = READ-COMMITTED

and restart mysql: ::

    /etc/init.d/mysql restart

To configure w3af_webui settings please edit file src/w3af_webui/settings.py.

Then create local_settings simlink: :: 

    cd src/w3af_webui
    ln -s local_settings.development.py local_settings.py

Create necessary directories: ::
    
    sudo mkdir /var/local/w3af_webui
    sudo chown USER: /var/local/w3af_webui
    sudo mkdir /var/log/w3af-webui/
    sudo chown USER: /var/log/w3af-webui

Database schema init: ::

    cd ../
    ./manage.py syncdb --noinput
    ./manage.py migrate

Run django via runserver: :: 
    
    ./manage.py runserver 0.0.0.0:8080

Run celery: ::

    ./manage.py celeryd -l INFO -B

Open in your browser http://0.0.0.0:8080/.
Default user is w3af_admin:w3af_admin

.. vim:ft=rst
