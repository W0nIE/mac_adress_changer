import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change its MAC-addr")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("MessageError")
    if not options.new_mac:
        parser.error("MessageError")
    return options


def change_mac(interface, new_mac)
    print("[+] Changing address for " + interface + " to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
