# Chat GPT clone using Python
This is a CLI app.

## Requirements

* git
* pip
* openai
* virtualenv (optional)

>Note: You can isolate the libraries by using a virtualenv

## Install the requirements on Windows

### git
You can install git from [this](https://git-scm.com/download/win) page, just download the installer and run it.

### pip
You can install pip from the python installer
### openai
To install openai open a command prompt and type the following

~~~
pip install openai
~~~

### virtualenv (optional)
~~~
pip install virtualenv
~~~

## Install the requirements on Linux (Ubuntu/Debian)
After installing git you can run the setup.sh file to install the rest of the requirements

### git
~~~
sudo apt install git
~~~

### pip
~~~
sudo apt install python3-pip
~~~
### openai
~~~
pip install openai
~~~

### virtualenv (optional)
~~~
pip install virtualenv
~~~

## Usage

> Note: If you are on Linux and you want to use virtualenv, you can run the setup.sh file.

You need an openAI API key, to get one open [this]() link.

### Windows
Open a command prompt and type the name of the program followed by your openAI API key.
Let's suppose your key is 28a0b696-993a-493e-a12d-4b93c3ded10a, so you need to run the
program like this:

~~~
python main.py 28a0b696-993a-493e-a12d-4b93c3ded10a
~~~

### Linux

~~~
python3 main.py 28a0b696-993a-493e-a12d-4b93c3ded10a
~~~
