# Python Course WS 24/25

> [!NOTE]  
> This is an introductory python course for Biology Master students at the University of Würzburg. The material is based on books that are freely available or accessible to the University Library. The course material can be re-used under CC-BY and the source code is under MIT license. The original course material is hosted on [WueCampus](https://wuecampus.uni-wuerzburg.de/).

## General

### Announcements

TODO

### Pre-course survey

TODO

### Course Repository

https://github.com/BioMeDS/Python_Course_WS24

## Communication

### Zoom Room

All lectures happen in the same Zoom room (accessible through WueCampus)

### Questions

A question forum (hosted in WueCampus)

## Setup Instructions

This is a hands-on course, so you will practice programming in Python using your own computer. Therefore, you need to install some required software:

- [Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install)
- [Visual Studio Code](https://code.visualstudio.com/download) (with [python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and [jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) extensions)
- [Git](https://git-scm.com/downloads) (advanced group)

Please follow the instructions linked above, to first install Minforge (follow the instructions closely) and then VS Code. Then install the extensions from within VS Code. If you plan to attend the advanced group, install Git, as well.

To finalize and test the installation, create a folder for the python course and open this folder in VS Code. Create a new file called "test.ipynb" and create a new "Code" cell in the created notebook. Enter "1+1" and click the little play icon to run the code. You will be prompted to install required packages. After confirming and waiting a minute, the result "2" should show up under the cell (see screenshot). 🎉 Congratulations, you are all set 🎉

<img width="994" height="474" alt="image" src="https://github.com/user-attachments/assets/856d4022-87a6-43f0-ae45-3e7cf1d0255d" />

## (Tentative) Schedule

|       | Monday   | Tuesday  | Wednesday | Thursday | Friday               |
|-------|----------|----------|-----------|----------|----------------------|
| 09:00 | Welcome  | Beginner | Beginner  | Beginner | Exam Assignments     |
| 10:00 | Beginner |          |           |          |                      |
| 11:00 | Advanced |          |           |          |                      |
| 12:00 |          |          |           |          |                      |
| 13:00 |          | Advanced | Advanced  | Advanced | Final Question Round |
| 14:00 |          |          |           |          |                      |
| 15:00 | Beginner | Beginner | Beginner  | Beginner |                      |
| 16:00 |          |          |           |          |                      |

## Beginner Group

[Python for the Life Sciences - A Gentle Introduction to Python for Life Scientists](https://pythonforthelifesciences.com/) by Alexander Lancaster and Gordon Webster

[Free full text from the university network](https://link.springer.com/book/10.1007/978-1-4842-4523-1) | SpringerLink

### Monday

#### Tasks

- work through Chapter 2, "Python at the Lab Bench"
- follow along with the code examples by manually typing them into a jupyter notebook (in VS Code)
- execute the code examples and try some modifications
- write down any questions and problems that occur, and we'll discuss them in the afternoon session
- when you are done, try to solve the exercises

#### Exercises

1. Write a function `fahrenheit_to_celsius(temperature)` that can convert Fahrenheit to Celsius and a function `celsius_to_fahrenheit(temperature)` that does the reverse
2. Write a function `is_leap_year(year)` that tells whether any given year is a leap year or not

#### Important Concepts

- Writing and running code (with Jupyter Notebooks)
- Variables and Types (float, int, string, boolean (True/False))
- Comments
- Code blocks (indentation)
- Functions
- Conditionals (if/elif/else)

### Tuesday

#### Tasks

- work through Chapter 3, "Making Sense of Sequences"
- follow along with the code examples, execute them and try some modifications
- write down any questions and problems that occur, and we'll discuss them in the afternoon session
- try to implement the final `restrictionDigest` function (from the end of the chapter) without typing it 1-to-1
- when you are done, try to solve the exercises

#### Exercises

1. Write a function `subsequence_positions(sequence, subsequence)` that takes a sequence and a subsequence as a string and returns a list of all positions where the subsequence occurs within the sequence
2. Write a function `subsequences_positions(sequence, subsequences)` that takes a sequence as a string and a list of subsequences and returns a dictionary with each subsequence as keys and a list of all positions where that subsequence occurs within the sequence as values

#### Important Concepts

- Loops (for)
- lists
- dictionaries
- string searching
- methods
- Code blocks (indentation)
- Functions
- Conditionals (if/elif/else)

### Wednesday

#### Tasks

- work through Chapter 4, "A Statistical Interlude"
- follow along with the code examples, execute them, and try some modifications
- write down any questions and problems that occur, and we'll discuss them in the afternoon session
- when you are done, try to solve the exercises, you'll need the following additional tutorials:
- walk through the first two `pandas` tutorials: "[What kind of data does pandas handle](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)" and "[How do I read and write tabular data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)"
- walk through the [basic `matplotlib` tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

#### Exercises

1. Calculate the results of `biomarker(pDisease, 0.8, 0.04)` with `pDisease` taking all values from 0 to 1 in steps of 0.05. Store the results in a list.
2. Create a pandas `DataFrame` with two columns `pDisease` and `biomarker` with the values from the previous exercise and save it as `biomarker.csv`.
3. Plot the result from exercise 1 using `matplotlib`, with `pDisease` on the x-axis and `biomarker` on the y-axis.

#### Installation

```
mamba install pandas
```

in Miniforge Prompt (Windows), Terminal (mac OS, Linux)

#### Important Concepts

- function arguments
- string formatting
- tables with `pandas`
- plotting with `matplotlib`

### Thursday

#### Tasks

- work through Chapter 5, "Opening Doors to Your Data"
- follow along with the code examples, execute them, and try some modifications
- write down any questions and problems that occur, and we'll discuss them in the afternoon session
- when you are done, try to solve the exercises

#### Exercises

1. Re-write the fasta parser to a function `parse(file)` that takes a file name and returns the dictionary
2. Add an optional argument `save_stats=False` to the function that, if set to `True`, will save a file `stats.csv` with the three columns: sequence id, length, GC %

#### Important Concepts

- reading text files
- type conversion
- exception handling (try/except)

