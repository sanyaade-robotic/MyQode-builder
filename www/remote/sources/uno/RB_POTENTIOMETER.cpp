#include "RB_POTENTIOMETER.h"


/*

*/

RB_POTENTIOMETER::RB_POTENTIOMETER(void)
{
	
	
	
}

RB_POTENTIOMETER::RB_POTENTIOMETER(uint8_t port):RB_Port(port)
{
	
	_SigPin = RBPort[port].dat;
}

void RB_POTENTIOMETER::SetPin(uint8_t sigpin)
{
    _SigPin = sigpin;
}


uint16_t RB_POTENTIOMETER::GetPotentiometer(void)
{
	
	 pinMode(_SigPin,INPUT);
	 uint16_t value = analogRead(_SigPin);
	 return value;
}

uint16_t  RB_POTENTIOMETER::  GetPotentiometerValue(void)
{
    int i = 0;
    uint16_t Value[10];
    uint16_t max = 0,min =0;
    uint32_t sum = 0;
    uint16_t return_value = 0;
    for(i=0;i<10;i++) 
       {
          Value[i] = GetPotentiometer();
          if(Value[i]>max)
             max = Value[i];
          if(Value[i]<min)
             min = Value[i];
          sum += Value[i];
       }
     sum = sum-max-min;
     return_value = sum/8;
     return return_value;
}