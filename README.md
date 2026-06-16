# Assignment 6: Managing Collections

> [!IMPORTANT]
> This assignment is to be completed individually. It is not a team project.  You must document (using comments in your code) all resources (beyond our official textbook, Canvas, the class discussion forum, or the class website) that you used to help you complete this assignment. For example, if you referenced a code example from an online website such as Stackoverflow or github you could acknowledge it as follows: 
>
> ```
> # Next we print 'Hello, World' to the console.
> # Based on help from: https://stackoverflow.com/questions/826948/syntax-error-on-print-with-python-3
> print("Hello, world!")
> ```
>
> You must provide an attribution to any resource you consulted to complete this assignment except for our official textbook, Canvas, the class discussion forum, or the class website. Resources that require attribution include — but are not limited to — AI tools (even those built in to VS Code), websites, books, notes from other students, tutors, or help from other people (friends, classmates, etc.). Under no circumstances are you to look at or copy any material related to another person's solution for this assignment.
>
> To repeat, you must attribute any resource you consulted to complete this assignment other than our official textbook, Canvas, class discussion forum, or the class website. You must cite all AI technologies you used, if any, to complete this assignment. Failure to provide attribution is a violation of the honor code.

## Overview

For this assignment, you'll be creating a simple program to manage a collection of books and movies for a library. You will be provided with a basic program as a starting point which loads the contents of the collection from two data files (one for books; one for movies). You'll then need to add the program code required to allow users to perform a variety of operations (e.g., checking in and out books, or adding new items to the collection). The full list of operations your program must support and other specific requirements are outlined below.

**Starter Code.** Unlike past assignments, you will not need to start from scratch on this assignment. Instead, you should begin with the starter code provided in this repository.  To complete the assignment, add the required functionality to the starter code in main.py.

> [!NOTE]
> Your very first order of business, after reading through the assignment, should be to understand the starter code. First, make sure it runs successfully. Then, make sure you understand how it works. In particular, pay attention to how the data is represented once it is loaded into your program. You will need to understand the data structure very well in order to complete this assignment successfully.

**Input Data.** There are two input data files for this assignment, both in CSV (comma-separated values) format. The first line of each file contains a list of variables known for each item. The remaining lines contain the actual collection data, with one line per item. Each line contains multiple values, separated (as the term CSV suggests) by commas. While the starter code provided to you will parse this file, I suggest that you open these files in a text editor or Excel to see what the data looks like before you start coding. You should also look to see how the starter code works. Understanding the data files and the code that parses them will help you understand the data structures used by the starter code to represent the collections.

The first file, books.csv, contains the list of books in the collection. It contains 8 variables per book, and the variable names are defined on the first line. They include: Title, Author, Publisher, Pages, Year, Copies, Available, and ID. The "Copies" field represents the number of copies owned within the collection. The "Available" field represents the number of copies available for checkout at the current point in time. The ID field is a unique identifier for the item.

The second file, movies.csv, contains the list of movies in the collection. It contains 8 variables per movie, and the variables are defined on the first line. They include: Title, Director, Length, Genre, Year, Copies, Available, and ID. The "Copies" field represents the number of copies owned within the collection. The "Available" field represents the number of copies available for checkout at the current point in time. The ID field is a unique identifier for the item.

## Basic Requirements

> [!NOTE]
> Satisfying only the basic requirements perfectly, with no points deducted for any reason, would earn a maximum score of 8 out of 10 for this assignment.

Your program should perform the following:

* Load the books and movies data files into the program, storing the data in a data structure using lists, dictionaries, and/or sets. **This functionality is provided to you already in the starter code. Do not re-implement it.**
* Display a menu that allows the user to perform a variety of actions, including:
    * Query for a book by pressing 'qb' then typing enter. The program should then allow a user to enter a query string which will be used to search against multiple fields in the collection: title, author, and publisher. The search should perform **partial string matching and be case insensitive.** For example, entering the query string "ion" should match both of the following strings: "Ions are Science" and "Frustration in Packaging". Details FOR ALL MATCHING BOOKS should be displayed.
    * Query for a movie by pressing 'qm' then typing enter. The program should then allow a user to enter a query string which will be used to search against multiple fields in the collection: title, director, and genre. The search, just as with books, should perform **partial string matching and be case insensitive.** Details FOR ALL MATCHING MOVIES should be displayed.
    * Request to check out an item by pressing 'co' and pressing enter. The program should then prompt the user to enter an ID number. The program should check to see if the requested item is available. If so, the availability number should be decreased by one and the user told that he/she has checked out the item. If the item is not available, or if the ID is not valid, the user should be shown an appropriate error message informing them about what went wrong.
    * Request to check in an item by pressing 'ci' and pressing enter. The program should them prompt the user to enter an ID number. The program should check to see that the requested item has indeed been checked out (that the available number is less than the copies number for the item). If so, the availability number should be increased by one and the user told that he/she has checked in the item. If the item is not checked out, or if the ID is not valid, the user should be shown an appropriate error message informing them about what went wrong.
    * Exit the program by pressing 'x' then typing enter.

The console output produced by your program should be nearly identical to the sample output provided below. While the specific books or movies displayed will vary because of differences in user input, the prompts and messages printed to the console when using your program should match those in the sample output to receive full credit.

## Advanced Requirements

> [!NOTE]
> Satisfying both the basic and advanced requirements perfectly, with no points deducted for any reason, will result in a full 10 out of 10 score for this assignment.

Expand on the basic requirements by extending your program as follows.

* Allow the user to request the display of the entire collection of either books (by typing "db") or movies (by typing "dm"), paging through the results 10 at a time. The user should be able to press <enter> to move on to the next group of ten items until the entire collection has been shown. The user should be able to press "m" (then <enter>) to quit the display process and return to the menu of options.
* Allow the user to add a new book (by typing "ab") or movie (by typing "am") to the collection.

Want an even greater challenge? You won't get extra credit, but test your skills by allowing the user to save the current collection to the input data files (by typing "s"). If done correctly, this will allow your checkin, checkout, and add commands to remain in place even when you restart your program!

## Sample Output

A brief example of the output produced by the correct solution is shown below. However, the output can get long. For this reason, rather than including the full sample output here in this README file, there is a separate file called sample_output.txt included in this repository.  See the sample_output.txt file for a far more extensive example of output produced by the solution to this assignment.

Here is the brief excerpt from the longer sample_output.txt file:

```
The collections have loaded successfully with 48 items.


********** Welcome to the Collection Manager. **********
COMMAND    FUNCTION
  ci         Check in an item
  co         Check out an item
  ab         Add a new book
  am         Add a new movie
  db         Display books
  dm         Display movies
  qb         Query for books
  qm         Query for movies
  x          Exit
Please enter a command to proceed: db
ID: 17001
Title: My Best Book Ever
Author: Joseph Caldwell
Publisher: FPG Publishing
Pages: 317
Year: 2014
Copies: 3
Available: 3

ID: 17002
Title: Robert's Rules
Author: Robert Hett Chapman
Publisher: Manning Hall Press
Pages: 199
Year: 2011
Copies: 1
Available: 1

ID: 17003
Title: View from the Top
Author: Joseph Caldwell
Publisher: FPG Publishing
Pages: 545
Year: 2014
Copies: 1
Available: 1

ID: 17004
Title: A River
Author: Elisha Mitchell
Publisher: FPG Publishing
Pages: 345
Year: 2014
Copies: 2
Available: 2

ID: 17005
Title: Winding Trails
Author: David Lowry Swain
Publisher: FPG Publishing
Pages: 1234
Year: 2014
Copies: 1
Available: 1

ID: 17006
Title: The Fork and the Spoon
Author: Charles Phillips
Publisher: FPG Publishing
Pages: 346
Year: 2011
Copies: 1
Available: 1

ID: 17007
Title: Purple Iron Frog
Author: Kemp Plummer Battle
Publisher: FPG Publishing
Pages: 456
Year: 2012
Copies: 3
Available: 3

ID: 17008
Title: Titanium Boxer
Author: George Tayloe Winston
Publisher: FPG Publishing
Pages: 345
Year: 2010
Copies: 1
Available: 1

ID: 17009
Title: Yellow Zinc
Author: George Tayloe Winston
Publisher: FPG Publishing
Pages: 873
Year: 2014
Copies: 5
Available: 5

ID: 17010
Title: Blue Snake
Author: Edwin Anderson Alderman
Publisher: FPG Publishing
Pages: 434
Year: 2013
Copies: 1
Available: 1

Press enter to show more items, or type 'm' to return to the menu: m


********** Welcome to the Collection Manager. **********
COMMAND    FUNCTION
  ci         Check in an item
  co         Check out an item
  ab         Add a new book
  am         Add a new movie
  db         Display books
  dm         Display movies
  qb         Query for books
  qm         Query for movies
  x          Exit
Please enter a command to proceed: qb
Enter a query string to use for the search: ill
ID: 17006
Title: The Fork and the Spoon
Author: Charles Phillips
Publisher: FPG Publishing
Pages: 346
Year: 2011
Copies: 1
Available: 1

ID: 17013
Title: Moonshot
Author: Charles Phillips
Publisher: Dean Smith Imprints
Pages: 262
Year: 2011
Copies: 2
Available: 2



********** Welcome to the Collection Manager. **********
COMMAND    FUNCTION
  ci         Check in an item
  co         Check out an item
  ab         Add a new book
  am         Add a new movie
  db         Display books
  dm         Display movies
  qb         Query for books
  qm         Query for movies
  x          Exit
Please enter a command to proceed: ci
Enter the ID for the item you wish to check in: 17013
All copies are already available, so this item can not be checked in.


********** Welcome to the Collection Manager. **********
COMMAND    FUNCTION
  ci         Check in an item
  co         Check out an item
  ab         Add a new book
  am         Add a new movie
  db         Display books
  dm         Display movies
  qb         Query for books
  qm         Query for movies
  x          Exit
Please enter a command to proceed: x

```

## Grading Criteria

This assignment will be graded on a 10 point scale. Your grade for this assignment will be based on a combination of factors, including:

* Correct functionality (e.g., Does your Python code do what it is supposed to do as outlined in the basic and/or advanced requirements?)
* Clarity of your solution (e.g., Did you solve the problem directly and efficiently? Or is your answer excessively complex and/or inefficient?)
* Coding style (e.g., Is your code readable with comments, meaningful variable names, and good whitespace/indentation?)
* Meets submission requirements (see below)

## Seeking Help

For general questions about Python, please use the class forum on Piazza to seek assistance. For questions that are personal in nature or that would reveal a solution to the assignment, you ask for help by email or during office hours. However, please note that emailed questions will not receive an immediate response. It is likely that it will take 24-48 hours for me to respond.

## Submitting Your Solution

When you have completed your work on the assignment, it is time to submit your solution via Canvas.  You can submit your assignment by taking the following steps:
1. Be sure that all of your changes have been pushed to your GitHub repository for the assignment.
2. Go to the web page for your repository on github.com
3. Click the green button labeled "< > Code &#9660;" which should open a popup menu.
4. From the popup menu, click on "Download ZIP" which will download a zip file containing your entire project to your computer. 
5. Submit the zip file you just downloaded via Canvas as your solution for this assignment.


> [!WARNING]
> NOTE FOR MAC USERS: Mac users who use the Safari browser will notice that the browser will, by default, automatically unzip and delete zip files you download from the internet. To change this behavior, press and hold the Option key when clicking the "Download ZIP" menu item.  This will prevent Safari from automatically unzipping and deleting the Zip file. Instead, it will just download the Zip file as it is just as you would get on any other browser.  Only Safari users need to take this extra step.


## Due Date

The due date for this assignment can be found in the official class schedule and on Canvas.

