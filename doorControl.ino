#define ledPin 13
int io;      

void setup() 
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() 
{
  if(Serial.available() > 1)
  {
    io = Serial.read();
    io == 1 ? digitalWrite(ledPin,1) : digitalWrite(ledPin,0);
  }
}
