import ipaddress

hostValues = {}
hostName = ""
ipAddress = ''
nodes = ''


def writeDictionary(host, ip, iteration):
    # Method to create a data dictionary of hostname entries
    for i in range(iteration):
        hostValues[host + str(i+1)] = ip + i
        print(hostValues)


def getHostValues():
    print("Enter hostname of a node in the cluster excluding the number "
          "from the end of the hostname i.e. cbtcnb-smscapp-")

    hostName = input("Please Enter Hostname ")
    print("Enter the first IP address in the cluster ")

    if any(char.isdigit() for char in hostName):
        return print("Error Please enter correct format of hostname")

    ipAddress = ipaddress.ip_address(input("Please Enter First IP Address of Cluster "))
    print("Enter the number of nodes ")

    nodes = input("Please enter the number of nodes ")
    print(nodes, hostName, ipAddress)

    writeDictionary(hostName, ipAddress, int(nodes))


def openHostFile():
    # Method to Open Hosts file
    print("Opening File for editing")
    file = '/etc/hosts'
    f = open(file, "w+")
    return f


def writeHostFile():
    # Method to write Hostnames to file
    #for i in range(len(hostValues)):
     for key, values in hostValues.items():
        HostsFile.write(key + ' ' + str(values) + "\n")


if __name__ == '__main__':
    print("Writing HostNames to /etc/hosts on nodes")
    getHostValues()
    HostsFile = openHostFile()
    writeHostFile()
    HostsFile.close()


