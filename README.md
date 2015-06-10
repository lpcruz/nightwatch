# nightwatch.py
An attempt at making a UI Automated Testing Framework using Python and Selenium. Influenced by the node.js powered framework, [nightwatch.js](http://nightwatchjs.org/)

# Demo

![alt tag](https://github.com/lpcruz/nightwatch/blob/master/demo/google-demo.png)
![alt tag](https://github.com/lpcruz/nightwatch/blob/master/demo/terminal-output-google.png)


# Installation

```
$ git clone https://github.com/lpcruz/nightwatch.git
```

```
Using Pip for dependencies

$ sudo pip install -r requirements.txt

```

# Creating a Test

* Create a new folder/directory for your project within the Root Director ```nightwatch```

* Within your new Project Folder, you'll need the following files to begin ```commands.py``` and ```nightwatch_utils.py```

* For screenshots, create a folder/directory called, ```screens```. This is referenced within ```commands.py```. This is where your screenshots will be located.

* Create a new file for your test eg. ```mytest.py```

* For reference, please review the template for making a test [here](https://github.com/lpcruz/nightwatch/blob/master/templates/test_template.py)

* You will need to make changes to nightwatch_utils and you can refer [here](https://github.com/lpcruz/nightwatch/blob/master/templates/nightwatch_utils.py)

* When you're done making your test, make sure that your new project folder contains updated versions of ```commands.py``` and ```nightwatch_utils.py```, as well as a ```screens``` directory

# Running a Test

Ensure that you are in the directory where which your new test file is located. Once you're in that directory do the following in terminal:

```
$ python mytest.py

```
