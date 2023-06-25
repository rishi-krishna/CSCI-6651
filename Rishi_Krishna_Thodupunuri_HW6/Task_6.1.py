import re

#get_ip_from_cfg function that expects the name of the file 
def get_ip_from_cfg(filename):
    ip_addresses = []
    with open(filename, 'r') as f:
        config = f.read()

        #regular expression to find ip address
        ip_pattern = r'ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)'
        matches = re.findall(ip_pattern, config)
        for match in matches:
            ip_addresses.append(match)
    return ip_addresses

# calling method with txt file
result = get_ip_from_cfg('config_r1.txt')
print(result)
