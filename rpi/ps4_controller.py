#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Playstation 4 Controller
# in Python. Simply plug your PS4 controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the PS4 controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2015 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

import os
import pprint
import pygame

import json
import paho.mqtt.client as mqtt

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):      
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        pygame.event.clear()
        while True:
            #for event in pygame.event.get():
            if True == True:
                
                event = pygame.event.poll()
                #pygame.event.clear()
                if event.type == pygame.JOYAXISMOTION:
                    self.axis_data[event.axis] = round(event.value,2)
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.button_data[event.button] = True
                elif event.type == pygame.JOYBUTTONUP:
                    self.button_data[event.button] = False
                elif event.type == pygame.JOYHATMOTION:
                    self.hat_data[event.hat] = event.value

                    #print(event.value)
                    if event.value[0] == -1:
                        cmd = { "cmd": "turn", "payload": ["left",event.value[0]] };
                        str2 = { "dest": command_topic, "payload": cmd };
                        client.publish(command_topic,"'" + json.dumps(str2) + "'")
                    elif event.value[0] == 1:
                        cmd = { "cmd": "turn", "payload": ["right",event.value[0]] };
                        str2 = { "dest": command_topic, "payload": cmd };
                        client.publish(command_topic,"'" + json.dumps(str2) + "'")
                    elif event.value[1] == 1:
                        cmd = { "cmd": "go", "payload": ["forward",event.value[1]] };
                        str2 = { "dest": command_topic, "payload": cmd };
                        client.publish(command_topic,"'" + json.dumps(str2) + "'")
                    elif event.value[1] == -1:
                        cmd = { "cmd": "go", "payload": ["reverse",event.value[1]] };
                        str2 = { "dest": command_topic, "payload": cmd };
                        client.publish(command_topic,"'" + json.dumps(str2) + "'")
                    else:
                        #cmd = { "cmd": "stop", "payload": [] };
                        pass
                    
                    #str2 = { "dest": command_topic, "payload": cmd };
                    print(str2)

                # Insert your code on what you would like to happen for each event here!
                # In the current setup, I have the state simply printing out to the screen.
                
                #os.system('clear')
                #pprint.pprint(self.button_data)
                #pprint.pprint(self.axis_data)
                #pprint.pprint(self.hat_data)


if __name__ == "__main__":


    # Edit below to include your AIO account details.
    USERNAME  = 'ppirrip'
    KEY       = '2aca2c25b0374611b25b22a5fdfbcc3d'

    # Adafruit IO MQTT service details.
    SERVER    = 'io.adafruit.com'
    PORT      = 1883
    KEEPALIVE = 3600  # One minute

    # topics
    connection_topic = USERNAME + '/feeds/aiidex.connected'
    response_topic = USERNAME + '/feeds/aiidex.response'
    command_topic = USERNAME + '/feeds/aiidex.command'

    # Create MQTT client and connect to Adafruit IO.
    client = mqtt.Client()
    client.username_pw_set(USERNAME, KEY)
    #client.on_connect = on_connect
    #client.on_disconnect = on_disconnect
    #client.on_message = None #on_message
    client.connect(SERVER, port=PORT, keepalive=KEEPALIVE)

    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
