# Carrier HVAC Monitoring Service

The intent of this project was to be able to collect data on the Carrier HVAC system managed by a Carrier Infinity Touch thermostat so that I could both better understand when and how the HVAC was being used in comparison to the atmospheric conditions, our solar production and house occupancy.   

Initially I had hoped to use the Carrier Open Access Alliance APIs to pull this data.  I submitted an application online but did not hear back for a week.  I followed up with an email and still haven't heard back.  Still hoping as they appear to have all the data I need.

After a little poking I found one reference online to someone that found that the thermostat responds to HTTP.  It returns several lines of code that are not simple ascii characters.   First, that didn't seem like a lot of information and second, I didn't feel like figuring out the character encoding.   I then decided to try my luck and checked to see how the thermostat was sending data to Carrier central.  Thankfully over HTTP, so I went about building my solution.  

I relied on the following to get going:

1. I had already set up a Raspbery Pi 3 as a bridge inline in my network between my switch and my Internet modem - here's a recipe for doing this:  https://techknight.eu/2015/01/02/setup-wired-network-bridge-raspberry-pi-debianlinux/
2. I found this Python package for capturing packets in XML format:  https://github.com/KimiNewt/pyshark
3. I wrote a script to parse the results and write the data to a sqlite3 database
4. Setup the script to run as a service following this https://gist.github.com/connorjan/01f995511cfd0fee1cfae2387024b54a

Next steps:

1. Build an API to my database so that I can match the various elements of our household to get some answers to my initial questions.

The code:

* hvac_data_collection.py - the full script - writes the data to my sqlite3 database
* hvac_monitor.py - a portion of the full script, simply outputs the data to screen
* processxml.py - learning how to parse an XML snippet

The code relies on the existence of a params.py file located in the running users home directory (/home/pi in my case).  The strucutre in this case is:

[HVAC]
\# Remote host IP - of course, carrier could change this any day - should maybe do source IP
bpf_filter = host 128.11.138.NN
\# Request display filter - in this case, the value between /systems/ and /status is the serial # of our thermostat.  Ours is 11 characters
display_filter = http.request.uri contains "/systems/08.......96/status"
\# Location of our sqlite3 DB
db_location = /mnt/usb1/hvac/hvac.db

Database structure is pretty self explanatory.  There's no real need to separate the date and time fields; i just do it out of convention.

> CREATE TABLE `hvac` (
> `tdate`TEXT,
> `ttime`TEXT,
> `param`TEXT,
> `val`TEXT
> );

