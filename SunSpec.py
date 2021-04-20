import sunspec.core.client as client
import time

d = client.SunSpecClientDevice(device_type=client.TCP,
        slave_id=126, ipaddr='129.21.177.6', ipport=8221,
        tls=False)
print (d.models)

while True:
        d.inverter.read()
        print(d.inverter)
        time.sleep(5)

