
import xml.etree.ElementTree as ET
import csv
import sys

def parse_nmap_xml(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['IP', 'Hostname', 'Port', 'Protocol', 'State', 'Service', 'Version', 'Product'])

        for host in root.findall('host'):
            ip = host.find('address[@addrtype="ipv4"]')
            ip_addr = ip.get('addr') if ip is not None else 'N/A'

            hostname_elem = host.find('hostnames/hostname')
            hostname = hostname_elem.get('name') if hostname_elem is not None else 'N/A'

            ports = host.find('ports')
            if ports is not None:
                for port in ports.findall('port'):
                    port_id = port.get('portid')
                    protocol = port.get('protocol')
                    state_elem = port.find('state')
                    state = state_elem.get('state') if state_elem is not None else 'N/A'
                    service_elem = port.find('service')
                    service = service_elem.get('name') if service_elem is not None else 'N/A'
                    product = service_elem.get('product') if service_elem is not None and service_elem.get('product') else 'N/A'
                    version = service_elem.get('version') if service_elem is not None and service_elem.get('version') else 'N/A'

                    writer.writerow([ip_addr, hostname, port_id, protocol, state, service, version, product])

    print(f"Done! Created {csv_file}")

if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("Usage: python3 nmap_xml_to_csv.py input.xml output.csv")
    else:
        parse_nmap_xml(sys.argv[1], sys.argv[2])
