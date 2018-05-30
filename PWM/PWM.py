#!/usr/bin/env python3
# -*- Coding: utf-8 -*-

# command args
# [1] pin number (GPIOn)
# [2] ���� [ms]
# [3] �p���X��[ms]
# >python3 pi_servo.py 18 20 2

import sys
import wiringpi

args = sys.argv
argc = len( args )

if argc != 4 :
        print("error : invalid arguments")
        print("ex.) python3 pi_servo.py 18 20 2")
        quit()

pwm_pin = int( args[1] )
interval = float( args[2] )
pulse = float( args[3] )

"""
PWM�́A�ȉ��̎��Ő��藧��

[PWM���g��] = 19.2MHz / [Clock] / [Range]
[Duty��] = [Duty] / [Range]

wiringpi�ł́A[Range] = 1024�ŌŒ肵�A[Clock]��[Duty]
��2�̃p�����[�^��PWM�𐧌䂷��

[Range] = 1024
[PWM���g��] = 18750 / [Clock]
[Duty��] = [Duty] / 1024
"""

range = 1024
duty_ratio = pulse / interval
hz = 1 / ( interval * 0.001 )
clock = int( 18750 / hz )
duty = int( duty_ratio * range )

print("pin = ", pwm_pin, " interval[ms] = ", interval, " pulse[ms] = ", pulse )
print("clock = ", clock, " duty=", duty, " duty_ratio=", duty_ratio )

# �����ݒ�
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( pwm_pin, wiringpi.GPIO.PWM_OUTPUT )
wiringpi.pwmSetMode( wiringpi.GPIO.PWM_MODE_MS )

# Clock��Duty��ݒ肵��PWM�𐶐�����
wiringpi.pwmSetClock( clock )
wiringpi.pwmWrite( pwm_pin, duty )
