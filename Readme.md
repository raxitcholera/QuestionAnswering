Question Answering
==================

Following the following step you would be able to setup my version of the Question Answering system using Python and Natural Language processing.

Required Installations 
----------------------

By following the following steps you would be able to get the system up and running.

* [Python](http://www.python.org/) -- `sudo apt-get install python2.6` (Required Version to be under python 3.0)
* [Pip](http://pypi.python.org/pypi/setuptools) -- `sudo easy_install pip`
* [Numpy] -- `sudo pip install -U numpy` (Optional)
* [PyYAML, NLTK](http://nltk.org/) -- `sudo pip install -U pyyaml nltk`
* [Apache]() -- `sudo apt-get install apache2`
* [Php5]() -- `sudo apt-get install php5`
* [Php Apache Liberary]() -- sudo apt-get install libapache2-mod-php5`
* [Apache]() -- `sudo /etc/init.d/apache2 restart`
* [Readability](http://pypi.python.org/pypi/readability-lxml) -- `python -m readability.readability -u http://pypi.python.org/pypi/readability-lxml`


Issues to take care
------------

1) Check the version of the default Python using: 
	
	python --version

2) Check if you have the required permission in the /var/www folder to make changes using:
	
	cd /var/www/
	ls -all

See if the name of the group of the owner and user access are the same which you have access to, if not please follow the following commands to change that:

	sudo su
	cd /var/www/
	chown -R username:username yourfoldername
	ls -all
	exit

After you have changed this the username you have mentioned would be able to make changes as per needed in the folder mentiond.

3) Check if apache has the same user previlages for this user or not using the following commands:

	sudo su
	cd /etc/apache2
	vi envvars

Locate the Term APACHE_RUN_USER and APACHE_RUN_GROUP and then change them to the names of the username that you have access to, only if that is the only user who is going to access this apache setup on this server. To save the changes and exit from the editor press the following:
	
	':wq'

4) Setup the Filezilla to access over SSH 22 port

Things you would need

* [Filezilla](http://filezilla-project.org/download.php) Download respective to your local system.
* [.pem]Certificate file given by the server even known as the Kep Pair file.
* [IP] The IP address of the server.
* [Username] The name of the user which would be used to access the Host server.

Now follow the follwing steps
	
	Edit->Settings
	Connection->SFTP
	Add Key File-> Locate the file on system and OK
	
	File->Site Manager (Ctrl+s)
	New Site-> General
	Host->IP address
	Port->22
	Protocol->SFTP
	Logon Type->Normal
	USer->Username
	(Connect)

You would be able to access and transfer the files on the server easyly now.
