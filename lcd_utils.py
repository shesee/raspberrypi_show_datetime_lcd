import time
from lcd_enums import lcd_cmd, lcd_cmd_param, lcd_reg_addr, lcd_addr, cmd_delay,write_delay
from smbus2 import SMBus

def busyloop(sec:float):
    st = time.perf_counter()
    while time.perf_counter() - st < sec:
        pass


def lcd_delay(sec:float):
    if sec > 0.001:
        time.sleep(sec)
    else:
        busyloop(sec)


def command(i2c:SMBus, cmd):
    i2c.write_byte_data(lcd_addr, lcd_reg_addr.lcd_command, cmd)
    lcd_delay(cmd_delay[cmd])


def writeMessage(i2c:SMBus, message:str):
    charcode_list = []
    for message_char in message:
        charcode_list.append(ord(message_char))
    i2c.write_i2c_block_data(lcd_addr, lcd_reg_addr.lcd_data, charcode_list)
    lcd_delay(write_delay)
