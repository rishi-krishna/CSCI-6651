ip_network = input("Enter the IP network (e.g: 10.1.1.0/24): ")

ip_parts, mask = ip_network.split('/')
ip_parts = ip_parts.split('.')
mask = int(mask)

# Print Network
print("Network:")
for part in ip_parts:
    print(f"{part:<10}", end="")
print()
for part in ip_parts:
    print(f"{int(part):08b} ", end="")
print()

# Print Mask
binary_mask = "1" * mask + "0" * (32 - mask)
print("Mask:")
print(f"/{mask}")
for i in range(0, 32, 8):
    mask_part = binary_mask[i:i + 8]
    print(f"{int(mask_part, 2):<10}", end="")
print()
for i in range(0, 32, 8):
    mask_part = binary_mask[i:i + 8]
    print(f"{mask_part} ", end="")
print()



