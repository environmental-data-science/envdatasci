
# Environmental Data Science


## [Course Syllabus](https://bit.ly/syllabus-eds-217)


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

	* The class server is located at [https://taylor.bren.ucsb.edu/](https://taylor.bren.ucsb.edu/)

	* Our server is running RStudio, which includes an installation of [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/). JupyterLab is an interactive environment for executing python code. Here are a couple of tutorials that introduce JupyterLab:

		* [A Quick Intro](https://www.youtube.com/watch?v=K2Yb1nXTmYM) (3 minutes)
		* [A Full Tutorial](https://youtu.be/7wfPqAyYADY) (25 minutes)

1. Login to the class server using your Bren user ID. 

> Note: You will need to be on campus or connected to UCSB's VPN to access the server.

1. Once you have logged into RStudio, start a new session by clicking the `+New Session` button at the top of the browser window. 

1. In the dialog box that pops up, create a session name (recommended: `EDS 217`), and select `JupyterLab` as the `Editor`. The `Cluster` option should be left as `Local` (the default)

1. Wait a moment for the JupyterLab instance to get initialized.

1. Clone this repository to your server instance.

	* Open a `Terminal` in your JupyterLab instance. ([Instructions](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html))

	* Type `git clone` and the the url for this repository, which is `https://github.com/environmental-data-science/eds-217.git`.

	     The entire command will look like this:

		`$ git clone https://github.com/environmental-data-science/eds-217`

		**Note:** In the line above, the `$` is your terminal prompt. On other systems, the command prompt is something like `>`, or `[username]$`. To keep these directions more general, I will just use `$` to represent the command prompt throughout our docs. The key point is that you *don't* need to type this as part of the command.

	* Press **Enter**. A local clone of the class repository will be created in your JupyterLab instance.

		```
		$ git clone https://github.com/environmental-data-science/eds-217
		> Cloning into eds-217...
		> remote: Counting objects: 10, done.
		> remote: Compressing objects: 100% (8/8), done.
		> remove: Total 10 (delta 1), reused 10 (delta 1)
		> Unpacking objects: 100% (10/10), done.
		```

	     You will now have a new local directory in your instance called `eds-217/`, which contains all of the course materials. Before proceeding, we need to make sure that your instance has all the necessary python libraries that the course materials require. 
		 
1. Use the file browser in JupyterLab top open the `eds-217/` directory. 

1. Double-click the `test_environment.ipynb` file. This will open the file into a Jupyer Notebook.

1. Follow the instructions in the notebook to execute the cells and confirm that your installation is working correctly. If all goes well, you will get a message saying `You\'re all set!`, and some detailed information on the various packages installed on `taylor.bren.ucsb.edu`. Now you're ready to learn some python!

### Local Installation (for Instructors or non-students)

1. Install Conda & Git.

	* Mac OS: Use [homebrew](https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37)
		
		`$ brew install anaconda`

		`$ brew install git`

	* Windows: ??

	* Linux: Use homebrew??

1. Clone the repository to your local machine and `cd` into the class repo directory

	`$ git clone https://github.com/environmental-data-science/eds-217`

	`$ cd eds-217`

1. Create a `conda` environment using the `environment.yml` file included in the repository.

	`$ conda env create --file environment.yml`

	**Note:** We are using python version [3.10.5](https://www.python.org/downloads/release/python-3105/) in this class. That may change in the future, but for now it matches the python that `taylor.bren.ucsb.edu` is using in RStudio's version of JupyterHub. 

1. Activate the `conda` envrionment

	`$ conda activate eds-217`

1. Install `pip` into the local conda environment.

	`$ conda install pip`

1. Add additional libaries to your conda environment using `pip`.

	`$ pip install -r requirements.txt`

	**Note:** We are using `pip` to manage dependencies within this conda environment. The use of `pip` and the `requirements.txt` file ensures consistency with our insallations on the JupyterHub server. This allows us to make sure that the working environment on our local machines matches *exactly* the working environment on JupyterHub. 

	**Note:** If you add a package to your local environment that is used in any of the course materials, you must use `pip freeze > requirements.txt` and push the new commit to our repo. 

