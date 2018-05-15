from __future__ import print_function

try:
    ip_addr = raw_input("Please enter an IP address: ")

except NameError:
    ip_addr = input("Please enter an IP address: ")

octects = ip_addr.split(".")

print()
print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(*octects))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(int(octects[0])), bin(int(octects[1])),
                                        bin(int(octects[2])), bin(int(octects[3]))))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(int(octects[0])), hex(int(octects[1])),
                                        hex(int(octects[2])), hex(int(octects[3]))))
print("-" * 60)
print()