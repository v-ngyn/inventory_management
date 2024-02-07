<h1>Inventory Management Interface</h1>
<p>Utilizes Django, Bootstrap, Python, HTML, and SQL</p>
<p>Tools used: VScode & WSL</p>

<h2>How to set up environment and run this project</h2>
<h3>1. Set up WSL environment and link with VScode</h3>
<p>Refer to this <a href="https://code.visualstudio.com/docs/remote/wsl">link</a> from the VScode documentation.</p>
<p>This should help you how to install WSL, manage VScode plugins, and establish a link between the two platforms.</p>
<p>Make sure the project files are in the WSL subdirectory. You will have to transfer the files from Windows to WSL.</p>

<h3>2. Setting up Django and Python3</h3>
<p>Run this command in the WSL console to install Python3:</p>

``$ sudo pip install python3``

<p>Run this command in the WSL console to install Django:</p>

``$ sudo pip install django``

<h3>3. Running server to localhost</h3>
<p>Navigate to the project working directory to where you see the file manage.py</p>
<p>Run this command in the WSL console:</p>

``$ python3 manage.py runserver``

<p>The server should be running on localhost:8000</p>
<p>Type that link into your browser and you should be able to access the inventory manager.</p>

**Dev Logs**
--
2/6/24
- completed base functionality of inventory manager. no bugs have been detected so far.
- i plan to add more visual information to dashboard; such as graphs, admin messages, etc.

2/5/24
- set up items table
- added functionality for users to add items
- added functionality to display items on a table
  - categorized by item ID, name, quanity, and category

1/29/24
- fixed log out function
- added navbar functionality

1/25/24
- ran into problem with logged out page, https error 405
- implemented log in and log out pages
- implemented cripsy forms and bootstrap5

1/22/24
- started project
  - coding environment: VScode and WSL: Ubuntu
- set up django and working local host
- set up blank navbar and webpage
