# Portable setup

For experiments that requires participant to freely move during EEG recording, a portable miniPC is available at the platform.

## Configuration

The configuration step must be done once and allows to configure the network settings of the mini Pc for later use.

For this configuration step, you will need a HDMI screen and a keyboard.

- Start the mini PC
- Open the `nmtui`
- Choose the network you want to connect to during your experiment.
- Make sure to tick the `Connect automatically` setting (press `space` to tick/untick settings)
- Save your changes
- Get the mini PC IP address:
    ```bash
    ifconfig
    ```


## Acquisitions.


### EEGO

- Connect the eego amplifier to the miniPC using the USB cable
- Start the eego amplifier

### Connect though ssh

- Connect to the mini PC via ssh:
    On the host machine (for example your laptop) open a terminal and type:
    ```
    ssh eeg@[IP_ADDRESS]
    ```
    where ``[IP_ADDRESS]`` is the IP address of the mini PC obtained in the previous steps.

    Make sure the host machine is on the same network as the miniPC.

### Start EEG acquisition

-  Start the EEG acquisition:

    ```bash
    ./eegosports &
    ```

    An LSL stream is created and should be broadcasting the EEG data over the network.