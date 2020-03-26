
# Environmental Data Science

[Course Information]


## How to use this repository.


### If you are a student in G136:

1. Login to the G136 JupyterHub Server.

	* Our server is located at [https://g136.lsit.ucsb.edu/](https://g136.lsit.ucsb.edu/)

	* Our server is running [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), which is an interactive environment for executing python code. Here are a couple of tutorials that introduce JupyterLab:

		* [A Quick Intro](https://www.youtube.com/watch?v=K2Yb1nXTmYM) (3 minutes)
		* [A Full Tutorial](https://youtu.be/7wfPqAyYADY) (25 minutes)

1. Clone this repository to your server instance.

	* Open a `Terminal` in your JupyterLab instance. ([Instructions](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html))

	* Type `git clone` and the the url for this repository, which is `https://github.com/environmental-data-science/envdatasci`.

	     The entire command will look like this:

		`jovyan@jupyter-USERNAME:~$ git clone https://github.com/environmental-data-science/envdatasci`

		**Note:** In the line above, the `jovyan@jupyter-USERNAME:~$` is your terminal prompt, where USERNAME is your ucsb id. On other systems, the command prompt is something like `>`, or `$`. To keep these directions more general, I will just use `$` to represent the command prompt throughout our docs. The key point is that you *don't* need to type this as part of the command.

	* Press **Enter**. A local clone of the class repository will be created in your JupyterLab instance.

		```
		$ git clone https://github.com/environmental-data-science/envdatasci
		> Cloning into envdatasci...
		> remote: Counting objects: 10, done.
		> remote: Compressing objects: 100% (8/8), done.
		> remove: Total 10 (delta 1), reused 10 (delta 1)
		> Unpacking objects: 100% (10/10), done.
		```

	     You will now have a new local directory in your instance called `envdatasci/`, which contains all of the course materials. Before proceeding, we need to make sure that your instance has all the necessary python libraries that the course materials require. We will use a python installation utility called [pip](https://pip.pypa.io) to update your instance with the required libraries. 

1. Use `pip` to install required libraries.

	* In your open terminal, change directory into the newly-created `envdatasci` folder.

		`$ cd envdatasci`

	* There is a text file called `requirements.txt` in this folder. You page through this file using the `more` command.

		`$ more requirements.txt`

	* The file contains a list of python modules. We will be using these various modules in the course, and so we need to make sure they are installed in your JupyterLab instance. This is easy to do with the `pip` command:

		`$ pip install -r requirements.txt`

	* Type the above command and press **Enter**. You will see a ton of output as the `pip` command reads each line of the `requirements.txt` file, determines what library (and library version) is on each line, and then installs the specific version of that library if is needed. The command also tracks down any dependencies that each new library might require and installs those too. 

		**Note:** Most of the libraries in `requirements.txt` should already be installed, in which case `pip` will report back `Requirement already satisfied` for almost every line.

1. Launch the test notebook, `test_environment.ipynb`. 




### Local Installation (for Instructors or non-students)

1. Install Conda & Git.

	#TODO - Add instructions or link. Include Windows & Mac directions.

1. Clone this repository to your local machine.

	* Step 1
	* Step 2


1. Create a conda environment on your local computer.

	[directions]

3. 
