
# Environmental Data Science


## [Course Syllabus](resources/G136_Syllabus_Spring_2020.pdf)


Course Description
==================

This course teaches the fundamentals of programming in Python. 
Students will learn foundational skills and concepts including data structures, 
programming basics, and how to clean, subset, aggregate, transform and visualize data. 
Course materials demonstrate the application of these techniques for 
environmental data analysis and problem solving.

Course Goals
============

1.  To develop expertise in the Python programming language and the use
    of Python's data science stack to effectively store, manipulate, and
    gain insight into environmental data.

2.  To be able to apply this understanding to characterize data on
    environmental patterns and processes at varying spatial and temporal
    scales.

Course Format
=============

Students will learn the principles of Python programming and
environmental data science by working largely independently on daily
course materials conducted in Python. Supplemental readings will be 
assigned for both programming and disciplinary content related to weekly themes. 


How to use this repository.
=============

### If you are a student in EDS 217:

1. Login to the EDS 217 JupyterHub Server.

	* Our server is located at [https://g136.lsit.ucsb.edu/](https://g136.lsit.ucsb.edu/)

	* Our server is running [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), which is an interactive environment for executing python code. Here are a couple of tutorials that introduce JupyterLab:

		* [A Quick Intro](https://www.youtube.com/watch?v=K2Yb1nXTmYM) (3 minutes)
		* [A Full Tutorial](https://youtu.be/7wfPqAyYADY) (25 minutes)

1. Clone this repository to your server instance.

	* Open a `Terminal` in your JupyterLab instance. ([Instructions](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html))

	* Type `git clone` and the the url for this repository, which is `https://github.com/environmental-data-science/envdatasci.git`.

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

	     You will now have a new local directory in your instance called `eds-217/`, which contains all of the course materials. Before proceeding, we need to make sure that your instance has all the necessary python libraries that the course materials require. We will use a python installation utility called [pip](https://pip.pypa.io) to update your instance with the required libraries. 

1. Use `pip` to install required libraries.

	* In your open terminal, change directory into the newly-created `eds-217` folder.

		`$ cd eds-217`

	* There is a text file called `requirements.txt` in this folder. You page through this file using the `more` command.

		`$ more requirements.txt`

	* The file contains a list of python modules. We will be using these various modules in the course, and so we need to make sure they are installed in your JupyterLab instance. This is easy to do with the `pip` command:

		`$ pip install -r requirements.txt`

	* Type the above command and press **Enter**. You will see a ton of output as the `pip` command reads each line of the `requirements.txt` file, determines what library (and library version) is on each line, and then installs the specific version of that library if is needed. The command also tracks down any dependencies that each new library might require and installs those too. 

		**Note:** Most of the libraries in `requirements.txt` should already be installed, in which case `pip` will report back `Requirement already satisfied` for almost every line.


### Local Installation (for Instructors or non-students)

1. Install Conda & Git.

	* Mac OS: Use [homebrew](https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37)
		
		`$ brew install anaconda`

		`$ brew install git`

	* Windows: ??

	* Linux: Use homebrew??

1. Create a `conda` environment.

	`$ conda create -n eds-217 python=3.7.3`

	**Note:** We are using python version [3.7.3](https://www.python.org/downloads/release/python-373/) in this class. That may change in the future, but for now it matches the python that LSIT is using in their docker images that they use to build JupyterHub deployments. 

1. Activate the `conda` envrionment

	`$ conda activate envdatasci`

1. Install `pip` into the local conda environment.

	`$ conda install pip`

1. Clone the repository to your local machine and `cd` into the class repo directory

	`$ git clone https://github.com/environmental-data-science/eds-217`

	`$ cd eds-217`

1. Add additional libaries to your conda environment using `pip`.

	`$ pip install -r requirements.txt`

	**Note:** We are using `pip` to manage dependencies within this conda environment. The use of `pip` and the `requirements.txt` file ensures consistency with our insallations on the JupyterHub server. This allows us to make sure that the working environment on our local machines matches *exactly* the working environment on JupyterHub. 

	**Note:** If you add a package to your local environment that is used in any of the course materials, you must use `pip freeze > requirements.txt` and push the new commit to our repo. 

