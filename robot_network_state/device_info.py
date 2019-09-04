# Used to input the devices and expected network state to be used as a list in a loop within Robot

##### Network properties #####
network_state = [{"DC1-N9K-SPINE2": {"bgp_neigh": 3, "ospf_neigh": 3, "up_int": 9}},
                {"DC1-N9K-SPINE1": {"bgp_neigh": 3, "ospf_neigh": 3, "up_int": 9}},
                {"DC1-N9K-LEAF1": {"bgp_neigh": 2, "ospf_neigh": 3, "up_int": 28}},
                {"DC1-N9K-LEAF2": {"bgp_neigh": 2, "ospf_neigh": 3, "up_int": 28}},
                {"DC1-CSR-XNET1": {"bgp_neigh": 4, "ospf_neigh": 1, "up_int": 6}}]

# Used for profiling script, for some reason BGP fails again.
features = "config;interface;ospf"

# Formats the network properties into lists for each element that are then used as variables in robot
devices = []
bgp_neigh = []
ospf_neigh = []
up_int = []
for each_device in network_state:
    for name, values in each_device.items():
        # Creates a list of devices
        devices.append(name)
        # Creates a list of number of BGP peers
        bgp_neigh.append(values["bgp_neigh"])
        # Creates a list of number of OSPF neighbors
        ospf_neigh.append(values["ospf_neigh"])
        # Creates a list of number of upp interfaces
        up_int.append(values["up_int"])
