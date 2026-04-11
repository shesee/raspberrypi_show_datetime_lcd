#!/usr/bin/env python
from smbus2 import SMBus
import time
from datetime import datetime
from lcd_enums import lcd_cmd, lcd_cmd_param
from lcd_utils import lcd_command, writeMessage

i2c = SMBus(1) # 1 is bus number



# LCD の初期化
def init ():
        #初期化
        lcd_command(i2c, lcd_cmd.lcd_function_set, lcd_cmd_param.lcd_function_set_data_width + lcd_cmd_param.lcd_function_set_lines)
        #拡張コマンド
        lcd_command(i2c, lcd_cmd.lcd_function_set, lcd_cmd_param.lcd_function_set_data_width + lcd_cmd_param.lcd_function_set_lines + lcd_cmd_param.lcd_function_set_ext)
        #周波数セット
        lcd_command(i2c, lcd_cmd.lcd_ext_osc_freq, lcd_cmd_param.lcd_ext_osc_freq_normal)
        #コントラスト下位
        lcd_command(i2c, lcd_cmd.lcd_ext_contrast, lcd_cmd_param.lcd_ext_contrast_normal)
        #コントラスト上位 
        lcd_command(i2c, lcd_cmd.lcd_ext_pwiccn, lcd_cmd_param.lcd_ext_pwiccn_boost + lcd_cmd_param.lcd_ext_pwiccn_contrast_3V)
        #増幅率
        lcd_command(i2c, lcd_cmd.lcd_ext_follower, lcd_cmd_param.lcd_ext_follower_on + lcd_cmd_param.lcd_ext_follower_pow_normal)
        #基本コマンド
        lcd_command(i2c, lcd_cmd.lcd_function_set, lcd_cmd_param.lcd_function_set_data_width + lcd_cmd_param.lcd_function_set_lines)
        #ディスプレイオン
        lcd_command(i2c, lcd_cmd.lcd_display, lcd_cmd_param.lcd_display_on)
        #クリア
        lcd_command(i2c, lcd_cmd.lcd_clear,0)
 
  
#main
init ()
while 1:

        dt = datetime.now()

        line1 = dt.strftime('%y/%m/%d')
        line2 = dt.strftime('%H:%M:%S')

        lcd_command(i2c, lcd_cmd.lcd_set_ddram_address, lcd_cmd_param.lcd_set_ddram_address_line1)
        writeMessage(i2c, line1)
        lcd_command(i2c, lcd_cmd.lcd_set_ddram_address, lcd_cmd_param.lcd_set_ddram_address_line2)
        writeMessage(i2c, line2)

        time.sleep(0.3)
