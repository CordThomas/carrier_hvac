import xml.etree.ElementTree as ET

xml = '<status version="1.7"><localTime>2018-07-04T10:57:39</localTime><oat>85</oat><mode>off</mode><cfgem>F</cfgem><cfgtype>heatcool</cfgtype><vacatrunning>off</vacatrunning><filtrlvl>0</filtrlvl><uvlvl>100</uvlvl><humlvl>100</humlvl><ventlvl>100</ventlvl><humid>off</humid><oprstsmsg>idle</oprstsmsg><zones><zone id="1"><name>ZONE 1</name><enabled>on</enabled><currentActivity>manual</currentActivity><rt>77.0</rt><rh>51</rh><fan>off</fan><htsp>58.0</htsp><clsp>78.0</clsp><hold>on</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="2"><name>Zone 2</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="3"><name>Zone 3</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="4"><name>Zone 4</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="5"><name>Zone 5</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="6"><name>Zone 6</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="7"><name>Zone 7</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone><zone id="8"><name>Zone 8</name><enabled>off</enabled><currentActivity>away</currentActivity><rt/><rh>51</rh><fan>off</fan><htsp>60.0</htsp><clsp>80.0</clsp><hold>off</hold><otmr/><zoneconditioning>idle</zoneconditioning><damperposition>15</damperposition></zone></zones></status>'

root = ET.fromstring(xml)

print("Full XML {0}".format(root.findall(".")))
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

print(enabled)
