#!/usr/bin/python3
import os
def check_reboot():
    """Returns True is the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
    #This is a file that's created on our computer when some software requires a reboot.

def main():
    pass

print(check_reboot())