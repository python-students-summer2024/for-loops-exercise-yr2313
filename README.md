# For Loop Practice

The given code in this repository contains files, named `number_guessing.py`, `virus_transmissiion.py`, and `loopy_turtles.py`, that contain several functions that must be completed in order for the program in `main.py` to work.

Your job is to complete the function definitions in these files according to the documentation included in the code.

The code for each function, if written correctly, will include at least one for loop, and will pass the given unit tests.

## Clone this repository

First, clone this repository to your local computer, using Visual Studio Code's cloning feature.

Helpful video:

- [cloning a code repository from GitHub to your local machine](https://www.youtube.com/watch?v=axcny0o1NYo).

## Set up Visual Studio Code

Once cloned, set Visual Studio Code to be suitable for Python development using the "command palette":

- set the interpreter to a Python 3.x interpreter, such as that by [`Anaconda`](https://www.anaconda.com/).
- set the linter to by `pylint`.
- set the test framework to be `pytest`.

Helpful video:

- [Setting up Visual Studio Code for Python development](https://www.youtube.com/watch?v=xsXMzyK1M4I)

## Modify the code

The files named `number_guessing.py`, `virus_transmissiion.py`, and `loopy_turtles.py` contain several functions that must be completed in order for the program in `main.py` to work. Each function contains a description of what it should do.

The only modifications you must make in order to complete this assignment are to the incomplete functions in these files.

### Run the program

To run the program, run the file named `main.py`. The code in this file makes use those functions you have modified to produce the desired behavior.

### Verify the output is correct

Running the `main.py` program, as given, will produce meaningful output. Verify visually that the output appears correct, given the expected behavior of the functions.

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. If the functions have been completed correctly, all tests should pass. You should not edit any files in the `test` directory.

If the tests do not appear, or seem to never stop loading, open up a Terminal window and run the command, `pytest --collect-only`, to see whether there are any errors in the code that prevent the tests from being discovered.

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
