import sys

filename = sys.argv[1]

config_table = [] 

#Task HW4

with open(filename, "r") as conf:  
    for line in conf:  
        words = line.split()
        if words[0] == '!':
            continue
        print(line.rstrip())

#Task HW4a:

print("\nTask HW4a: ")
ignore = ["duplex", "alias", "configuration"]
with open(filename, "r") as conf:  
    for line in conf:  
        words = line.split()
        
        if (words[0] == '!'):
            continue
        if any(word in ignore for word in words):
                    continue
        print(line.strip())

#Task HW4b:

destinationFile = sys.argv[2]

print("\nTask HW4b: resulting lines are stored in :" +destinationFile)
ignore = ["duplex", "alias", "configuration"]
with open(filename, "r") as conf, open(destinationFile, "w") as dest_conf:  
    for line in conf:  
        words = line.split()
        
        if (words[0] == '!'):
            continue
        if any(word in ignore for word in words):
                    continue
        dest_conf.write(line)
