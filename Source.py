#Source Script for web server AC/DC control using RPi
#Py_script #Python_3.x

from flask import Flask
import RPi.GPIO as GPIO

app=Flask(__name__)
@app.route('/')
def hello():
  print("Home automation using web server")
@app.route('/gpio/<state>')
def switch(state):
  a = int(state)
  if(a==1):
    GPIO.output(16,GPIO.LOW)
    val = 'On'
  else:
    GPIO.output(16,GPIO.HIGH)
    val = 'Off'
  return val

if __name__=('__main__')
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(16,GPIO.OUT)
  app.run(host = '0.0.0.0',port = 8086)
  
 
  
