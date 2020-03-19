import telnetlib


def main_menu():
    print("MAIN MENU ")
    print("1: Manage Inventory list")
    print("2: Collect device info")
    option_selected = int(input("Select an option: "))
    if option_selected == 1:
        device_management_menu()
    elif option_selected == 2:
        TELNET_CONNECTION()
    else:
        pass

def list_devices():
    file = "device_list.csv"
    readed = pd.read_csv(file)
    print(readed)

def add_device_info():
    hostname = input("Hostname: ")
    ip_address = input("IP Address: ")
    port = input("Port: ")
    protocol = input("Protocol (TELNET/SSH): ")
    vendor = input("Vendor: ")
    device = (hostname, ip_address, port, protocol, vendor)
    return device

def add_device_function(device):
    with open(r'device_list.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(device)

def collect_device_info():

def device_management_menu():
    "This function is used to manage the Device List"
    print("DEVICE LIST MANAGEMENT\n")
    print("1: List all devices")
    print("2: Add device")
    list_option = int(input("Select an option: "))

    if list_option == 1:
        list_devices()
    elif list_option == 2:
        add_device_info()
        add_device_function(device)
    else:
        pass
    return