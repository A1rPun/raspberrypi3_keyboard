#!/usr/bin/python3
import os
import json
from src import main


if __name__ == "__main__":
    config_file = "./config.json"
    config = json.load(open(config_file, "r"))

    # Try to get mac address
    if config["MAC_ADDRESS"] == "":
        address = os.popen("hciconfig hci0 | awk '/BD Address: /{print $3}'").read()
        print(f"Got mac address: {address}")
        config["MAC_ADDRESS"] = address

    # Ask for mac address as fallback
    if config["MAC_ADDRESS"] == "":
        config["MAC_ADDRESS"] = input(f"What is the MAC address of the device?:\n> ").strip() or config["MAC_ADDRESS"]
        print(f"The mac address of the bluetooth device is: {config["MAC_ADDRESS"]}")

    # Ask for device name
    config["ALIAS"] = input(f"What is the name of the device? (Default: {config["ALIAS"] or "none"}):\n> ").strip() or config["ALIAS"]
    print(f"The name of the bluetooth device is: {config["ALIAS"]}")
    # Save and run
    json.dump(config, open(config_file, "w"), indent=2)
    main.main()
