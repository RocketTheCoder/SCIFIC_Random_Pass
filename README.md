# SCIFIC_Random_Pass
int Input = A0;
int SensorVal = 0;
void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  Serial.println("smoke sensor by Monish");
 
  
}

void loop() {

  SensorVal = analogRead(Input);
  Serial.println(SensorVal);
  delay(1000);
  if(SensorVal>200){
  Serial.println("TOO MUCH SMOKE!"); 
 digitalWrite(2,HIGH);delay(2000);
  digitalWrite(2,LOW);delay(2000);
  }
  }
