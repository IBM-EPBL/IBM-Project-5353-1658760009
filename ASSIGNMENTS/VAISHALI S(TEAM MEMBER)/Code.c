int baselineTemp = 0;
int celsius = 0;
int pinSensor =2;
int pinLed =12;
int pinBuzzer =13;
int pirSensor =0;
int tempSensor=A0;

void setup()
{
  pinMode(pinSensor, INPUT);
  pinMode(tempSensor, INPUT);
  Serial.begin(9600);
  pinMode(pinLed, OUTPUT);
  pinMode(pinBuzzer, OUTPUT);
 
}

void loop()
{
  baselineTemp = 20;
  
  celsius = map(((analogRead(tempSensor) - 20) * 3.04), 0, 1023, -40, 125);
  
  Serial.print(celsius);
  Serial.println(" C, ");
  pirSensor = digitalRead(pinSensor);
  
  if (pirSensor == HIGH && celsius >= baselineTemp + 40)
  {
  
    digitalWrite(pinLed, HIGH);
    tone(pinBuzzer, 1000,500);
  
  }
  
  else {
    
    digitalWrite(pinLed, LOW);
  }
  
  delay(10);
}
