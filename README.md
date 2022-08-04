# BindDSMX
## Overview
The goal of this project was to put an spm9645 Spektrum Satellite Reciever into bind mode without the use of a standard reciever or niche hardware. The binding protocol for Spektrum DSM2/DSMx remote recievers is as follows: 


Within 200ms of powering on, the reciever must recieve a number of falling pulses over the signal pin. The number of pulses determines the communication protocol type as shown in the tables below. If the satellite reciever is to be used as the main reciever, then it should use one of the 'Internal' protocols. There can only be 1 'Internal' reciever. It is recommended to use 9 pulses because if the hardware is unable to support 11ms communication, it will automatically bind as 22ms. See manufacturers documentation for more information:

[Remote Reciever Interfacing Documentation](https://www.spektrumrc.com/ProdInfo/Files/Remote%20Receiver%20Interfacing%20Rev%20A.pdf)

##### DSMX Bind Modes:
|Pulses |Mode     |Protocol |Type|
|-------|---------|---------|----|
|7      |Internal |DSMx     |22ms|
|8      |External |DSMx     |22ms|
|9      |Internal |DSMx     |11ms|
|10     |External |DSMx     |11ms|

##### DSM2 Bind Modes (not recommended):
|Pulses |Mode     |Protocol |Type|
|-------|---------|---------|----|
|3      |Internal |DSM2     |22ms|
|4      |External |DSM2     |22ms|
|5      |Internal |DSM2     |11ms|
|6      |External |DSM2     |11ms|

## Software
Test
## Hardware
Test
![BindCircuit](https://user-images.githubusercontent.com/104041016/182746055-f7c7d6db-a366-4edc-8f20-23109ccb1560.png)
