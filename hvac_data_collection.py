import pyshark
from datetime import datetime as dt
import datetime
import sqlite3
import xml.etree.ElementTree as ET
import configparser, os
import sys

config = configparser.ConfigParser()
config.read(os.path.expanduser('~/params.py'))

def send_data(conn, event_time, **kwargs):
   cur = conn.cursor()
   statement = 'INSERT INTO hvac (tdate, ttime, param, val) VALUES (date(\'now\',\'localtime\'), ?, ?, ?)'
   for key, value in kwargs.items():
     cur.execute(statement, (event_time, key, value))
   conn.commit()

def parse_pdml(pdml):
    root = ET.fromstring(pdml)

    localTime = root.find("./localTime").text
    oat = root.find("./oat").text
    mode = root.find("./mode").text
    filtrlvl = root.find("./filtrlvl").text
    uvlvl = root.find("./uvlvl").text
    humlvl = root.find("./humlvl").text
    ventlvl = root.find("./ventlvl").text
    humid = root.find("./humid").text
    oprstsmsg = root.find("./oprstsmsg").text

    zone1 = root.find("./zones/zone[@id='1']")
    enabled = zone1.find("enabled").text
    currentActivity = zone1.find("currentActivity").text
    rt = zone1.find("rt").text
    rh = zone1.find("rh").text
    fan = zone1.find("fan").text
    htsp = zone1.find("htsp").text
    clsp = zone1.find("clsp").text
    zoneconditioning = zone1.find("zoneconditioning").text
    damperposition = zone1.find("damperposition").text

    tm = dt.today()

    event_time = localTime[11:]
    conn = sqlite3.connect(config['HVAC']['db_location'])

    try:
        send_data(conn, event_time, oat=oat, mode=mode, filtrlvl=filtrlvl, uvlvl=uvlvl, humlvl=humlvl,
              ventlvl=ventlvl, humid=humid, oprstsmsg=oprstsmsg, enabled=enabled,
              currentActivity=currentActivity, rt=rt, rh=rh, fan=fan, htsp=htsp, clsp=clsp, 
              zoneconditioning=zoneconditioning, damperposition=damperposition)
    except Exception as error_info:
        print("We have an error in submitting data {0}".format(error_info))

    conn.close()

def print_callback(pkt):

    try:
        urlencoded_layer = pkt["urlencoded-form"]
        urlencoded_value = urlencoded_layer.get_field_value("value")
        parse_pdml(urlencoded_value)
    except:
        print("Couldn't get layer")
      

def process_capture():
    capture = pyshark.LiveCapture(interface = 'br0', 
               bpf_filter = config['HVAC']['bpf_filter'],
               display_filter = config['HVAC']['display_filter'])


    capture.apply_on_packets(print_callback, timeout=50000)


if __name__ == "__main__":
    process_capture()
