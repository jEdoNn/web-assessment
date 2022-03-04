### design
The python based flask framework builds the server, connects to the collected data files and displays them on the server page.

### development
Use the flask framework to build the server, use the route method to connect to the html, use the python language to parse the csv file and store it in the db file, and use the sqlite3 language to connect to the server.

### implementation
pyenv local 3.6.9  #  this sets the local version of python to 3.6.9
python3 -m venv .venv  #  this creates the virtual environment for you
source .venv/bin/activate  #  this activates the virtual environment

export FLASK_APP=HC.py  #  After installing the required libraries start the configuration and launch. Export the master file.
export FLASK_ENV=development  #  Export environment.
python3 -m flask run --host=0.0.0.0 --port=2500  #  Start the flask framework server at local: 2500.
### installation
pyenv local 3.6.9  #  this sets the local version of python to 3.6.9
python3 -m venv .venv  #  this creates the virtual environment for you
source .venv/bin/activate  #  this activates the virtual environment
pip install --upgrade pip [ this is optional]  #  this installs pip, and upgrades it if required.

pip install flask  #  Type this command into the command line to download the flask library.

### GitHub log
GitHub url:https://github.com/jEdoNn/web-assessment

codio@jesterbuffalo-yesgeorge:~/workspace$ git log
commit 40fb621bd755ed798a5f761db18c8bf3ab880d0e (HEAD -> main, origin/main)
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 16:58:31 2022 +0000

    update

commit 4fbb91b14a179f48957cc06f718777350291b74f
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 16:57:09 2022 +0000

    update

commit 6af5d559455d31db2e9a39f608f0d4ee6c2141de
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 16:54:30 2022 +0000

    update

commit 5b30f572f6ec3b3e638a21d45250f452b5f911e8
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 16:46:08 2022 +0000

    update

commit 2579c3141dc1bf2e53eabb17b47c02aab9072e77
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 13:52:00 2022 +0000

    make it better

commit 86bf5eccecc87d6a305b6234b59043e97e845b59
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 13:35:39 2022 +0000

    fixed version

commit 0dd3dda88aaff6e4a956d232a1785253df28be90
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Fri Mar 4 13:05:55 2022 +0000

    Add Heroku deployment files

commit f1f73c9e01f84d924638d01996b11aee471e81dc
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Thu Mar 3 16:42:51 2022 +0000

    new version

commit 9bf8064371b4f72c8f96272cc1433f1e15bece54
Author: JIADONG GONG <j.gong1.21@abdn.ac.uk>
Date:   Mon Feb 28 20:09:45 2022 +0000

    first commit

###Heroku log
Heroku git URL https://git.heroku.com/webassessment.git

-----> Building on the Heroku-20 stack
-----> Determining which buildpack to use for this app
-----> Python app detected
-----> Using Python version specified in runtime.txt
 !     Requested runtime (python-3.6.9) is not available for this stack (heroku-20).
 !     Aborting.  More info: https://devcenter.heroku.com/articles/python-support
 !     Push rejected, failed to compile Python app.
 !     Push failed