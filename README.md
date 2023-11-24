# Scif project for Tourism Australia

## Description

This project automates processing and visualization of data directly from a database. It can adjust outputs subject to user inputs, and provides
data on trend and forecast.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation
This project requires some python libraries for its functionality. Please make sure you have python3 properly installed on your machine, as well 
as the following libraries.
  - postgresql
  - sqlalchemy
  - pandas
  - matplotlib
  - reportlab
  - statsmodels
  - datetime (part of standard library, but please double check)
# Example installation commands
pip install postgresql <br>
pip install sqlalchemy <br>
pip install pandas <br>
pip install matplotlib <br>
pip install reportlab <br>
pip install statsmodels <br>
pip install datetime <br>

common troubleshoots:
If pip did not work for you, replace pip with pip3. <br>
If your terminal shows that pip did not exist, do the following: <br>
  for macOS: <br>
    type in terminal:  sudo easy_install pip <br>
  for ubuntu/linux: <br>
    type in terminal:  apt-get install python3-pip <br>
  for windows: <br>
    Instead of pip install [package], try using python -m pip install [package] <br>

## Usage
  Run qry_generation.py, the terminal will prompt you to enter IATA codes of desired airports of origin. The inputs are case insensitive. 
  To finish entering origins, press 'q' and press enter. Please note that there needs to be at least 1 airports of origin.
  <br>
  Then the terminal will prompt you to type which continents airports of origin originated from. Currently this only intakes one of the following:
  asia, northamerica, europe, oceania. 

  After pressing enter, the inputs will prompt user to type in IATA codes of desired airports of destination and press Enter. 
  To stop typing, press 'q' and press enter.
  By default, the airports of destination is set to 
  international airports all over Australia. Also note that the the airports of destination should be within Australia.

  Finally, the program will run and produce the output pdf in output.pdf in the directory.
  <br>

  **note**: There will be graphs popping out after run. It is expected behavior, simply close all the graphs. The resulting pdf is named output.pdf and everytime this script is run, it will be automatically updated.

## Notes of usage:
  This code is based on pgSQL database provided by cirium. It may not work on databases with different column and table names. <br>
  To adjust the dtaabase this code is reading from, change the database URI by adjusting the db_uri variable.

## Contributing
  Avinash Dansinghani <br>
  Coco Wu <br>
  Lucy Lu lucyluhk@gmail.com (enquiries about usage and problems)


  
  
