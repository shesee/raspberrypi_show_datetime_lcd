import time
from lcd_enums import lcd_cmd, lcd_cmd_param, lcd_reg_addr, lcd_addr, cmd_delay,write_delay
from smbus2 import SMBus


def busyloop(sec:float):
    '''タイトループによるマイクロ秒単位の待機 
    Args:
        sec: float 待機時間 秒の浮動小数点
    '''
    st = time.perf_counter()
    while time.perf_counter() - st < sec:
        pass

def lcd_delay(sec:float):
    '''LCDの動作を待機する
    Args:
        sec: float 待機時間 ミリ秒以上の場合はsleep それ以下はタイトループを使う
    '''
    if sec > 0.001:
        print("sleep " + str(sec))
        time.sleep(sec)
    else:
        print("busyloop " + str(sec))
        busyloop(sec)


def lcd_command(i2c:SMBus, cmd:lcd_cmd, prm:int):
    '''AQM0802 液晶にコマンドを送付する
    Args:
        i2c: SMBus i2cライブラリ
        cmd: lcd_cmd コマンドデータ
        prm: int コマンドパラメーター
    '''
    print("cmd " + str(lcd_cmd+prm))
    i2c.write_byte_data(lcd_addr, lcd_reg_addr.lcd_command, cmd + prm)
    lcd_delay(cmd_delay[cmd])


def writeMessage(i2c:SMBus, message:str):
    '''AQM0802 液晶に表示文字列を送付する
    Args:
        i2c: SMBus i2cライブラリ
        message: str 表示データ(ASCIIコード)
    '''
    charcode_list = []
    for message_char in message:
        charcode_list.append(ord(message_char))
    i2c.write_i2c_block_data(lcd_addr, lcd_reg_addr.lcd_data, charcode_list)
    lcd_delay(write_delay)
