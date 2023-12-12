def read_oui_file(filename):
    oui_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            if '(hex)' in line:
                parts = line.strip().split('(hex)')
                mac = parts[0].strip()
                manufacturer = parts[1].strip()
                oui_dict[mac] = manufacturer
    return oui_dict

def match_oui_to_mac(filename, oui_dict):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                mac_address = parts[1]
                oui = mac_address[:8].upper()  # Extract the first 6 characters (OUI)
                manufacturer = oui_dict.get(oui, 'Unknown')
                print(f'MAC Address: {mac_address}, OUI: {oui}, Manufacturer: {manufacturer}')


    oui_dict = read_oui_file(oui_filename)
    match_oui_to_mac(arp_scan_filename, oui_dict)
