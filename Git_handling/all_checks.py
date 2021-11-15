#!/usr/bin/python3
import os
def check_reboot():
    """Returns True is the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")
    #This is a file that's created on our computer when some software requires a reboot.

def main():
    pass

main()