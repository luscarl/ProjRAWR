# Scif project for Tourism Australia

## Description

This project automates processing and visualization of data directly from a database. It can adjust outputs subject to user inputs, and provides
data on trend and forecast.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation
This project requires some python libraries for it's functionality. Please make sure you have python3 properly installed on your machine, as well 
as the following libraries.
  - postgresql
  - sqlalchemy
  - pandas
  - matplotlib
  - reportlab
  - statsmodels
  - datetime (part of standard library, but please double check)
# Example installation commands
pip install postgresql
pip install sqlalchemy
pip install pandas
pip install matplotlib
pip install reportlab
pip install statsmodels
pip install datetime

common troubleshoots:
If pip did not work for you, replace pip with pip3. 
If your terminal shows that pip did not exist, do the following:
  for macOS:
    type in terminal:  sudo easy_install pip
  for ubuntu/linux:
    type in terminal:  apt-get install python3-pip
  for windows:
    Instead of pip install [package], try using python -m pip install [package]

## Usage
  Run qry_generation.py, the terminal will prompt you to enter IATA codes of desired airports of origin. The inputs are case insensitive. 
  To finish entering origins, press 'q' and press enter. Please note that there needs to be at least 1 airports of origin.

  Then the terminal will prompt you to type which continents airports of origin originated from. Currently this only intakes one of the following:
  asia, northamerica, europe, oceania. 

  After pressing enter, the inputs will prompt user to type in IATA codes of desired airports of destination and press Enter. 
  To stop typing, press 'q' and press enter.
  By default, the airports of destination is set to 
  international airports all over Australia. Also note that the the airports of destination should be within Australia.

  Finally, the program will run and produce the output pdf in output.pdf in the directory.

## Contributing
  Avinash Dansinghani
  Coco Wu
  Ella Foth
  Gavin Chan
  Lachlan Hammond
  Lucy Lu lucyluhk@gmail.com (enquiries about usage and problems)
  
  
