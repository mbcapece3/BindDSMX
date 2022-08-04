/*Spektrum Binding Protocol:
 Must send a specified number of falling pulses within 200ms of powering on
 3 Internal DSM2 22ms
 4 External DSM2 22ms
 5 Internal DSM2 11ms
 6 External DSM2 11ms 
 7 Internal DSMx 22ms
 8 External DSMx 22ms
 9 Internal DSMx 11ms (UNIVERSAL INTERNAL)
 10 External DSMx 11ms 
*/

//Pin Assignments
static const uint8_t receiverVcc = 0;
static const uint8_t switchSignal = 15;
static const uint8_t receiverSignal = 10;
static const uint8_t numBindPulses = 9;  //Use Universal


void setup() {
  // put your setup code here, to run once:

  pinMode(switchSignal, INPUT);   //Switch imput to read when reciever is powered on. Use External 10K Pulldown Resistor
  
  pinMode(receiverVcc, OUTPUT);   //Reciever Power
  pinMode(receiverSignal, OUTPUT);  //Reciever Signal

  Serial.begin(9600);

  digitalWrite(receiverVcc, HIGH);    //Power On
  digitalWrite(receiverSignal, HIGH);   //Allows for falling pulses

  delay(5000);

}

void loop() {
  // Use a physical switch to power on reciever and begin pulses immediately

  if (digitalRead(switchSignal)){
    Serial.println("High");
    delay(100);   //Ensure reciever powered on before delivering pulses
    
    for(uint8_t pulseCount = 0; pulseCount < numBindPulses; pulseCount++){      //Deliver Falling Pulses
    digitalWrite(receiverSignal, LOW);
    delayMicroseconds(120);
    digitalWrite(receiverSignal, HIGH);
    delayMicroseconds(120);
    }

    Serial.println("Pulses Sent");
    delay(15000); //Power on transmitter in bind mode within this delay period
  }

}
