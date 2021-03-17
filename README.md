<!-- Stephen Bowen 2021 -->
# A Raspberry Pi for Spot

The Raspberry Pi is a small, arm-based computer that is capable of running a custom installation of [Ubuntu Linux for Raspberry Pi](https://ubuntu.com/download/raspberry-pi). The [Raspberry Pi Model 4B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) is the recommended model for the purpose of this project for its on-device wireless networking support.

This guide will help the user set up a networked "brain" for Spot that allows for Spot to be controlled natively through the [Boston Dynamics Spot SDK](https://github.com/boston-dynamics/spot-sdk) on a small and portable device that can easily be attached to and powered by Spot. This allows the user to execute programs without having a standalone device connected to Spot. The networking capabilities also allow for Spot to be controlled through either a local network or the internet.

## Setting up the Raspberry Pi Environment
Before a fresh Raspberry Pi can be used with Spot, several pieces of software must be installed and initialized. This guide will outline how to complete these steps using the GUI on the Raspberry Pi. A monitor and necessary peripherals are required.

### Downloading and Installing the custom Ubuntu OS
The most up-to-date version of the custom OS can be found [HERE](CHRIS).

Raspberry Pi provides the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) for installing a .img file to a microSD card that is used as the boot drive for a Raspberry Pi.

Using the [Raspberry Pi Imager](https://www.raspberrypi.org/software/), choose the [custom OS](https://www.raspberrypi.org/software/) as the 'Operating System' to install and a properly-sized (at least 32GB) microSD card as the 'SD Card'. The user should be aware that all data previously stored on the prospective microSD card will be lost during the imaging process. Click the 'Write' button to begin the process and go grab a cup of coffee. The imaging process should last around 30-40 minutes.

### First boot on the Raspberry Pi
Once the imaging process has completed, place the microSD card in a Raspberry Pi and boot into the GUI. On first boot, the OS will ask the user for a default password (Rob0t577) then force the user to create their own password which will then be the system's password.

After the password has been reset and the user has access to the desktop, open terminal and run the 'wifi_settings.py' script using the following command:
>sudo python3 ~/Desktop/wifi_settings.py

The 'wifi_settings.py' script sets the WiFi networking preferences and restarts the system to apply them. After a successful reboot, it is recommended to verify the Raspberry Pi has an active internet connection before moving to the next step.
