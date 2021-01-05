# NFC-Reader
Raspberry Pi + NFC Board + Programmable NFC Tags
NFC Board can be found on https://www.amazon.com/Adafruit-Controller-Shield-Arduino-Extras/dp/B00IQY2P82/ref=sr_1_3?dchild=1&keywords=adafruit+pn532&qid=1609876216&sr=8-3


You will need upload SerialReader into Raspberry Pi, then run the Python code.

Assuming you have proper connection between Raspberry Pi and NFC board, then you can upload SerialReader to Raspberry Pi. The original readMifare.pde is owned by Adafruit industries, I only kept things I need for my project which became the SerialReader file.

The NFC Reader file needs access to a database in order to compare data with reading results.
