# ISS_Projekt_2020
ISS Viertsemesterprojekt 2020: Projekt Maschinelles Lernen in der Kommunikationstechnik

## Structure

> main.py

The main script that loads images from disk, turns them into numpy arrays and 'transmits' them using the komm python library.
> Transmitters/

The folder for the different transmitters. Currently only a QPSK transmitter and its unittests is implemented.
> pictures/

Contains the input and output folders for the pictures. A few public domain images are provided with the code.
Please not that output pictures have a "reconstructed_" prefix in their filename which is automatically ignored by git.

## How to execute
Enter the virtual environment with
```. ./venv/bin/activate```, then run ```python main.py```
for the programm or ```python -m unittest``` to run the tests.
Leave the virtual environment with ```deactivate```.

## Installation
```
sudo apt install python3.6 python3-venv
git clone git@github.com:tyculus/ISS_Projekt_2020.git
cd ISS_Projekt_2020
python3.6 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
```
