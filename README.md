# Bluetooth listener raspberry

1.- Setup raspberry bluetooth

In this file: /etc/systemd/system/dbus-org.bluez.service

Change this line

```
ExecStart=/usr/libexec/bluetooth/bluetoothd
```

For this

```
ExecStart=/usr/libexec/bluetooth/bluetoothd -C
ExecStartPost=/usr/bin/sdptool add SP
```

Now reboot raspberry

2.- Make bluetooth discoverable

Execute the next commands in raspberry terminal

```
bluetoothctl
    power on
    discoverable on
```

3.- Turn on watching bluetooth serial

Execute command

```
sudo rfcomm watch hci0
```

4.- Connect your bluetooth app program

5.- Execute python script and enjoy :)

```
python bluetooth_listener.py
```
