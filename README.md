# Raspberry Pi 3 Keyboard

## Step 1: Installation

Only need to do this once

### Step 1.1: Update your Raspberry Pi

```
$ apt get update
$ apt get full-upgrade
```

If you get mirror errors, fully replace your mirror file with the latest mirror file.

### Step 1.2: Get git and this repository

```
$ apt get git
$ git clone https://github.com/A1rPun/raspberrypi3_keyboard
$ cd raspberrypi3_keyboard
```

### Step 1.3: Install the needed packages to run this program

```
$ ./install/install.sh
```

## Step 2: Run the program

Need to run this every time you power on the Raspberry Pi and want to use this program

```
$ ./setup.py
```

## Step 3: Usage

Input:  
q = quit  
m = simple mouse input  
any other string = send text as keys

## Uninstall

```
$ ./install/uninstall.sh
```

## Sources

- https://impythonist.wordpress.com/2014/02/01/emulate-a-bluetooth-keyboard-with-the-raspberry-pi/
- https://github.com/thanhlev/keyboard_mouse_emulate_on_raspberry
- https://gist.github.com/scientificRat/be2bbac0769bfa04820bc73edc009bdf
- https://github.com/AnesBenmerzoug/Bluetooth_HID

## Alternatives

- https://github.com/quaxalber/bluetooth_2_usb
