# Contributing to SLModes

SLModes became open-source after being closed-source for some years. The reason for this change is that it is no longer
practical for me to continue developing the software, while at the same time, there still existing lots of room for
improvement and new features. It is my belief that SLModes provides genuine value to musicians and that it would be a
pity to let the project stagnate.

In other words, I made the project open-source in order to give an opportunity for the community to continue its
development.

If you are interested in contributing, you are welcome to do so. Please take a moment to read the following guidelines:

## Getting Started

To get started, follow these steps:

1. Fork the SLModes repository to your own GitHub account.
2. Clone your fork to your local machine.
3. Create a new branch for your changes.
4. Make your changes and commit them.
5. Push your changes to your fork.
5. Submit a pull request to the SLModes repository.

## Guidelines for Contributions

When making contributions to SLModes, please follow these guidelines:

1. Test your changes thoroughly before submitting a pull request.
2. Make sure your changes do not break existing functionality.
3. If you are making a significant change, please open an issue to discuss it before submitting a pull request.
4. Providing a working frozen code is helpful to make the software available to users. This is specially true for macOS, since I can no longer guarantee I will be able to do it myself moving forward. Read the last section of this document to get familiarized with the challenges regarding freezing the code.
5. You are not expected to make changes to SLModes for macOS and Windows (unless you want to). From now on, those 2 versions will grow independent from each other.
6. You should keep in mind that I'm mostly an amateur self-taught programmer, and some things might not have been done according to the textbook. If you find such things and want to improve them, do it.

## Review Process

To conclude the process, I will review a pull request before it is merged into the main branch.

Thank you for your contributions to SLModes!

## Contact
To contact me directly, go to https://sinewavelab.com/contact/

# SLModes Report - Installation Tips, Freezing, etc.

The next part of this document contains some notes regarding steps and challenges I faced during the development of
SLModes.

# macOS version

## Installation

- SLModes for macOS was developed on Catalina and tried on a clean install of Big Sur. It is important to test the .app file on different systems, because many times it will give some error. Through trial and error, I found ways to avoid the errors. 
- SLModes hasn't been tested by me on Monterey or Ventura, hopefully someone else can pick up the development of the software into more recent systems.
- XCode was installed on macOS. IDE used to program was Pycharm.
- Best Python version found for this project: 3.7.9. More recent versions were creating problems during the Freeze part,
  e.g. completely black display of the window.
- Installing Python via Homebrew will not include the tKinter library, and for various reasons it is not possible to
  install it separately.

- Installing pip:

``` 
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

- SLModes for macOS has some very large differences in some aspects from the windows version. The main one is that it
  doesn't generate MIDI sounds, but instead plays audio files.

## Freezing

- Unlike version 1.5.0, using Pyinstaller / auto-py-to-exe creates issues with the app on Big Sur as it shows the error
  “The user does not have permissions to open this file”. ❌
- Creating the app with cx_freeze didn't work, as the terminal shows the error 'couldn't find file background01.png'
  even though the file was in the folder ❌
- py2app was used ✅
    - If py2app is not working, and you cannot see the error in the terminal, use cx_Freeze. It won't work (says it
      can't find the included files), but it will show the errors. Once fixed, go back to using Py2App. By the way, most
      likely the errors derive from libraries that are not found in Python3. To install, use this code, adapted to the
      library in question:

```
python3 -m pip install pynput –upgrade
```

### Install py2app:

```
$ python3 -m pip install -U py2app==0.27
```

### Missing Files

It is necessary to add the pygame_icon.tiff file (found on the project page) to a subfolder of the Python37 folder.

Biblioteca>Frameworks>Python.framework>Versions>3.7>lib>python3.7>site-packages>pygame>

### Create distribution:

```
python3 setup.py py2app -–packages=PIL
```

### Codesign

It is necessary to certify the Python file that is inside the newly created SLModes package:
output/SLModes.app/Contents/MacOS/Python. SLC is the name I gave to the certificate that I created.

```
codesign -f -s SLC Python
```

To see how to create (SLC) certificates on macOS, watch this video:
https://www.youtube.com/watch?v=VbbhhXEGH8o

How to open terminal in macOS specific folder:
https://www.youtube.com/watch?v=IAmsq1ULvSk

### Test the File

- After freezing, only the **SLModes.app** file is important.
- Use the same macOS to zip that file. Otherwise, it will probably give an error like *"You do not have the permission
  to run this file"* when you try to run it in a different macOS.
- Run the SLModes.app in a different macOS. If it run without errors, you can consider the freezing and zipping
  processes were successful ✅

# Windows

## Freezing

Use **CX_Freeze**

In the Windows project folder, right-click and choose Git Bash Here, then:

```
python setup.py bdist_msi
```

