#!/bin/python3
import psutil

def get_disk_usage():
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')

    # Print the results
    print(f"Total: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"Used: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"Free: {disk_usage.free / (1024 ** 3):.2f} GB")
    print(f"Percentage: {disk_usage.percent}%")

# Check if percentage is higher than 90%
     # Check if percentage is higher than 90%
    if disk_usage.percent > 90:
        # Print warning message in red
        print("\033[91mDisk Usage High!\033[0m")  # \033[91m is ANSI escape code for red text
    else:
        print("Disk usage OKAY!")
# Call the function
get_disk_usage()
