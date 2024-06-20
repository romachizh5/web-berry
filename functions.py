import gpiod
import serial
import json

ser = serial.Serial('dev/ttyACM1', 9600, timeout=1)
ser.flush()

nasos_PIN = 7
hectare1_PIN = 8
hectare2_PIN = 25
hectare3_PIN = 24
chip = gpiod.Chip('gpiochip4')
nasos_line = chip.get_line(nasos_PIN)
hectare1_line = chip.get_line(hectare1_PIN)
hectare2_line = chip.get_line(hectare2_PIN)
hectare3_line = chip.get_line(hectare3_PIN)
nasos_line.request(consumer="NASOS", type=gpiod.LINE_REQ_DIR_OUT)
hectare1_line.request(consumer="HECTARE1", type=gpiod.LINE_REQ_DIR_OUT)
hectare2_line.request(consumer="HECTARE2", type=gpiod.LINE_REQ_DIR_OUT)
hectare3_line.request(consumer="HECTARE3", type=gpiod.LINE_REQ_DIR_OUT)
def start_auto_poliv():
    print("start auto")


def stop_auto_poliv():
    print("stop auto")


def open_nasos():
    print("open nasos")
    nasos_line.set_value(1)


def close_nasos():
    print("close nasos")
    nasos_line.set_value(1)


def hectare1_open():
    print("hectare1 open")
    hectare1_line.set_value(1)


def hectare1_close():
    print("hectare1 close")
    hectare1_line.set_value(0)


def hectare2_open():
    print("hectare2 open")
    hectare2_line.set_value(1)


def hectare2_close():
    print("hectare2 close")
    hectare2_line.set_value(0)


def hectare3_open():
    print("hectare3 open")
    hectare3_line.set_value(1)


def hectare3_close():
    print("hectare3 close")
    hectare3_line.set_value(0)


def vlag():
    print("Влажность")
    vlag = ser.readline().decode('utf-8').split()
    while True:
        if ser.in_waiting > 0:
            vlag = ser.readline().decode('utf-8').split()
            vlag_dict = {}
            for i, item in enumerate(vlag):
                vlag_dict[f"v{i+1}"] = item
            with open('static/vlag.json', w) as f:
                f.write("")
                json.dump(vlag_dict, f)
            print(vlag_dict)
            vlag = []
            break