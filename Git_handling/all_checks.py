#!/usr/bin/python3
import os
import sys
def check_reboot():
    """Returns True is the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
    #This is a file that's created on our computer when some software requires a reboot.

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)g
    if disk_full():
        print("Disk Full.")
        sys.exit()
    print("Everything OK.")
    sys.exit(0)

main()