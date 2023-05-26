command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

# using split, extract vlans from list1
vlan_list1 = command1.split("vlan ")[1].split(",")
#  using split, extract vlans from list2
vlan_list2 = command2.split("vlan ")[1].split(",")

# convert them to set
vlan_set1 = set(vlan_list1)
vlan_set2 = set(vlan_list2)

# Find the intersection of the two sets
result = list(vlan_set1.intersection(vlan_set2))

# Print the result
print(result)