valid_ip = False
while not valid_ip:
    ip_address = input("Enter an IP address (e.g., 10.0.1.1): ")

    # Split the IP address into octets
    octets = ip_address.split(".")

    # Check if the IP address has 4 octets
    #if values are not seperated by ".", octets will be less hten 4
    if len(octets) != 4:
        print("Invalid IP address, please try again")
        continue
    
    
    # Check each octet for valid range and type
    for octet in octets:
        # Check if octet is numeric
        if not octet.isdigit():
            valid_ip = False
            break
        # Check if octet is within range 0-255
        octet_value = int(octet)
        if octet_value < 0 or octet_value > 255:
            valid_ip = False
            break
        valid_ip = True
    
    if valid_ip:
        break
    else:
        print("Invalid IP address. Please try again.")
        
# Check the type of IP address based on the first octet
if octets[0] == "255" and octets.count("255") == 4:
    print("local broadcast")
elif octets[0] == "0" and octets.count("0") == 4:
    print("unassigned")
elif 1 <= int(octets[0]) <= 126:
    print("unicast class A")
elif 128 <= int(octets[0]) <= 191:
    print("unicast class B")
elif 192 <= int(octets[0]) <= 223:
    print("unicast class C")
elif 224 <= int(octets[0]) <= 239:
    print("multicast")
else:
    print("unused")
              
        
        




