import pyshark
import xml.etree.ElementTree as ET

f = open('/usr/lib/solar-home/hvac/log-traffic.log', 'a')

def parse_pdml(pdml):
    pdml_tree = ET.parse(pdml)
    

def print_callback(pkt):
    print('Just arrived: type {0}'.format(type(pkt)))
    print('Just arrived: {0}'.format(pkt))
    try:
        print('Just arrived: {0}'.format(pkt.urlencoded-form))
    except:
        print("Can't find urlencoded - 1")

    try:
        print('Just arrived: {0}'.format(pkt.http.urlencoded-form.value))
    except:
        print("Can't find urlencoded - 2")

    try:
        urlencoded_layer = pkt["urlencoded-form"]
        print("We got the encoded layer {0}".format(type(urlencoded_layer)))
        for field in urlencoded_layer.field_names:
            print("    Field name: {0}".format(field))
        urlencoded_value = urlencoded_layer.get_field_value("value")
        print ("We got the value {0}".format(urlencoded_value))
        f.write(urlencoded_value)
    except:
        print("Couldn't get layer")
      

capture = pyshark.LiveCapture(interface = 'br0', 
               bpf_filter = 'host 128.11.138.31',
               display_filter = 'http.request.uri contains "/systems/0817W002796/status"')


capture.apply_on_packets(print_callback, timeout=50000)
