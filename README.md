# KiuAssessment

## Creating the dev environment
This project uses pyenv+pipenv to create the dev virtual environment.

The setenv.sh script will
* Download pyenv if not installed
* Download python version if not installed using pyenv
* Creates the virtual environment using pipenv
* Activates the environment
* Download/Sync all the project dependencies

```
$ ./setenv.sh
```

NOTE: Before running setenv script, make sure core.symlinks are not disabled in the .gitconfig file 

## Running UT
This project uses pytest for unit testing
```
$ pytest tests
```

## Report sample script
A sample python script "report_sample.py" was added to simulate a report generation

```
$ python report_sample.py
```
