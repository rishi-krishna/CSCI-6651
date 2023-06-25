import re

#get_ip_from_cfg function that expects the name of the file 
def get_ip_from_cfg(filename):
    ip_dict = {}
    with open(filename, 'r') as f:
        config = f.read()

        #regular expression to find interface
        interface_pattern = r'interface (\S+)'

        #regular expression to find ip address
        ip_pattern = r'ip address (\d+\.\d+\.\d+\.\d+) (\d+\.\d+\.\d+\.\d+)'
        interfaces = re.findall(interface_pattern, config)
        for interface in interfaces:
            regex = r'interface {}\n([\s\S]+?)!'.format(interface)
            interface_config = re.search(regex, config, re.MULTILINE)
            if interface_config:
                matches = re.findall(ip_pattern, interface_config.group(1))
                if matches:
                    ip_dict[interface] = matches[0]
    return ip_dict

# calling method with txt file
result = get_ip_from_cfg('config_r1.txt')
print(result)
