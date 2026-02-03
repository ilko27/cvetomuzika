Python and arduino project to make LED strips react to live music. The PC's audio is rerouted to an input channel using VB-Cable. Sounddevice then uses the input channel and applies a low pass filter at 250Hz to isolate the bass frequencies. The RMS value of the bass amplitude is used for the intensity of the LED lights.

The protocol used is:
```
[0x01][0x03][R_VALUE][G_VALUE][B_VALUE][CHECKSUM]
```
Where 0x01 is the byte marking start of sequence, 0x03 is length of sequence, the next three bytes are the values for RGB of the led strips and the checksum is XOR-ing the RGB values.


The adruino uses three MOSFETs for each color.
