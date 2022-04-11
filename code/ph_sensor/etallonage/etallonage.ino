/*
 # This sample code is used to test the pH meter V1.0.
 # Editor : YouYou
 # Ver    : 1.0
 # Product: analog pH meter
 # SKU    : SEN0161
*/
#define SensorPin A1
#define Offset 0.38
#define LED 13
#define samplingInterval 20
#define printInterval 800
#define ArrayLenth  40
int pHArray[ArrayLenth];
int pHArrayIndex=0;

void setup(void) {
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
  Serial.println("pH meter experiment!");
}

void loop(void) {
  static unsigned long samplingTime = millis();
  static unsigned long printTime = millis();
  static float pHValue,voltage;
  
  if(millis()-samplingTime > samplingInterval)  {
      pHArray[pHArrayIndex++]=analogRead(SensorPin);
      if(pHArrayIndex==ArrayLenth)  pHArrayIndex=0;
      voltage = avergearray(pHArray, ArrayLenth)*5.0/1024;
      pHValue = 3.5*voltage+Offset;
      samplingTime=millis();
  }
  if(millis() - printTime > printInterval)  {
    Serial.print("Voltage:");
    Serial.print(voltage,2);
    Serial.print("    pH value: ");
    Serial.println(pHValue,2);
    digitalWrite(LED,digitalRead(LED)^1);
    printTime=millis();
  } 
}
  
double avergearray(int* arr, int number) {
  int i;
  int max,min;
  double avg;
  long amount=0;
  
  if(number <= 0) {
    Serial.println("Error number for the array to avraging!/n");
    return 0;
  }
  
  if(number < 5) {
    for(i=0; i<number; i++) {
      amount+=arr[i];
    }
    avg = amount/number;
    return avg;
  } 
  else {
    if(arr[0] < arr[1]) { min = arr[0]; max=arr[1]; }
    else { min=arr[1]; max=arr[0]; }
    
    for(i=2; i<number; i++) {
      if(arr[i]<min) {
        amount+=min;
        min=arr[i];
      } 
      else {
        if(arr[i]>max) {
          amount+=max;
          max=arr[i];
        } 
        else {
          amount+=arr[i];
        }
      }
    }
    
    avg = (double)amount/(number-2);
  }
  
return avg; 
}
