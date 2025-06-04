# PPL_Project
PPL Project with chatbox helps users can adjust their cart


This is the PPL project about chatbox help users to interact with shopping by command, can be triggered by automation, API connection.


(04/06/2025)
Project Starting Date: 04/06/2025 (4 days left to deadline)
Team members: ? myself only
Starting coding date: 10/05/2025

**Initialize the code and how to run**
Well... I have ever never done this before but I need to download the zip file then extract it or clone it to the folder. It must have at least 4 files: 
- chatbox.g4
- chatbox.py
- CartVisitor.py
- products.json
Open the terminal, cd to the extracted folder:
- ```python chatbox.py gen``` to generate the ANTLR
- ```python chatbox.py run``` to run the project
- I'm tired to write the tutorial in this so, let me ~~GPT~~ that, please

**Explaination**
- chatbox.py handles setup, print command to generate ANTLR(Lexers, Parsers and Visitors in the CompiledFiles), run the code and the loop to get the inputs from terminal to the Lexers, Parsers and Visitors to run.
- chatbox.g4 is the main core of this project that have all the grammars, languages, syntax, etc... that makes this project work
- CartVisitor.py have all the visit node from Program to command, conditionalCommand, etc...
- products.json is the list of products that can be used as an instance for calculating.

**Some Issues**
- From start, *we* submited the project with storage in database (MySQL), but I worked alone, and have no time to generate the database or something. So... my appologies for not completing the promised tasks. All the products added in carts now is stored in 1 session only. However, I may try to extract that to .txt as the bill.

**Future Work**
- I wrote this to have enough, I may write the report more careful and with academic words. But this can be used in Webs, Cashier or automation work.

**Lecturer**
[Le Thi Ngoc Hanh](https://lehanhcs.github.io/)

Do Tan Loc - ITCSIU21199
*noname4now*

