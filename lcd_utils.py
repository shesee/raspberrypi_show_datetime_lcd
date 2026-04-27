import time
from lcd_enums import lcd_cmd, lcd_cmd_param, lcd_reg_addr, lcd_addr, cmd_delay, write_delay
from smbus2 import SMBus

''' Raspberry pi だとマイクロ秒単位のスリープが可能なので削除
def busyloop(sec:float):
    st = time.perf_counter()
    while time.perf_counter() - st < sec:
        pass
'''

def lcd_delay(sec:float):
    '''LCDの動作を待機する
    Args:
        sec: float 待機時間
    '''
    #print("sleep %f" % sec)
    time.sleep(sec)


def lcd_command(i2c:SMBus, cmd:lcd_cmd, prm:int):
    '''AQM0802 液晶にコマンドを送付する
    Args:
        i2c: SMBus i2cライブラリ
        cmd: lcd_cmd コマンドデータ
        prm: int コマンドパラメーター
    '''
    #print("cmd %x" % (cmd+prm))
    i2c.write_byte_data(lcd_addr, lcd_reg_addr.lcd_command, cmd + prm)
    lcd_delay(cmd_delay[cmd])


def lcd_writeMessage(i2c:SMBus, message:str):
    '''AQM0802 液晶に表示文字列を送付する
    Args:
        i2c: SMBus i2cライブラリ
        message: str 表示データ(ASCIIコード+半角カナ AQM0802の資料を参照のこと)
    '''
    charcode_list = []
    for message_char in message:
        charcode_list.append(ord(message_char))
    i2c.write_i2c_block_data(lcd_addr, lcd_reg_addr.lcd_data, charcode_list)
    lcd_delay(write_delay)
