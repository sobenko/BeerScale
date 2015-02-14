// Load cells are linear. So once you have established two data pairs, you can interpolate the rest.

float analogValueAverage[6] = {0,0,0,0,0,0};
int kegActive[6] = {1,0,1,0,0,0}; 

// How often do we do readings?
long time = 0; //
int timeBetweenReadings = 200; // We want a reading every 200 ms;

int led = 13;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
}

void loop() {
  digitalWrite(led, HIGH);
  int analogValues[5];
  for (int i =0; i<=5; i++){
   analogValues[i] = analogRead(i);
   // running average - We smooth the readings a little bit
  analogValueAverage[i] = 0.99*analogValueAverage[i] + 0.01*analogValues[i];
  }
  
  // Is it time to print?
  if(millis() > time + timeBetweenReadings){
    for (int i=0; i<=5; i++){
      if(kegActive[i]){ 
        Serial.print(analogValueAverage[i]);
        Serial.print(";");
      }
    }
    Serial.println();
    time = millis();
  }
 
  digitalWrite(led, LOW);
}
