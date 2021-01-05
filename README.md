# NFC-Reader
This feature was part of a project I did for my Software Engineering class. This project is called Easy Book a system we designed to help speed up Library's rent and return process. This project contains three parts: A mobile application for user to scan for renting books, A database which stores all relevant book informations and A return station.  

Raspberry Pi + NFC Board + Programmable NFC Tags
NFC Board can be found on https://www.amazon.com/Adafruit-Controller-Shield-Arduino-Extras/dp/B00IQY2P82/ref=sr_1_3?dchild=1&keywords=adafruit+pn532&qid=1609876216&sr=8-3

Assuming you have proper connection between Raspberry Pi and NFC board, then you can upload SerialReader to Raspberry Pi. The original readMifare.pde is owned by Adafruit industries, I only kept things I need for my project which became the SerialReader file.

The NFC Reader file needs access to a database in order to compare data with reading results. In NFC Reader, I fetch data from our own database repository "http://www.easybook2017.com/nfc" which is no longer available. I also passed some parameters to the url which is data coming from NFC tags. With that set up, if user returns a book successfully, he/she will hear a sound feedback otherwise the screen will return a error message.
