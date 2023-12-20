# import necesssary libraries
import dpkt
import socket
import pygeoip

# make sure database in folder
gi = pygeoip.GeoIP('GeoLiteCity.dat')


'''
implement geo location method:
- find geo locations for each IP address
- convert into KML format
'''
def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('x.xxx.xxx.xxx') # replace with your IP address
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        )%(dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''

'''
implement loop method:
- loop over captured network data (pcap)
- extract source and destination of IP addresses of each captured network packet
'''
def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts


'''
implement main method:
- open captured data 
- create header and footer of KML file (to upload to Google Maps)
- add styling
'''
def main():
    f = open('wireshark_data.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
    '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
    print(kmldoc)

# execute
if __name__ == '__main__':
    main()