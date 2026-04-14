#!/usr/bin/env python
from smbus2 import SMBus
import time
from datetime import datetime
from lcd_enums import lcd_cmd, lcd_cmd_param
from lcd_utils import lcd_command, lcd_writeMessage

i2c = SMBus(1) #Raspberry pi のi2cバスの1番を指定

# AQM0802 LCD の初期化
def init ():
        #初期化
        lcd_command(i2c, lcd_cmd.lcd_function_set, lcd_cmd_param.lcd_function_set_data_width + lcd_cmd_param.lcd_function_set_lines)
        #拡張コマンド切り替え
        lcd_command(i2c, lcd_cmd.lcd_function_set, lcd_cmd_param.lcd_function_set_data_width + lcd_cmd_param.lcd_function_set_lines + lcd_cmd_param.lcd_function_set_ext)
        #周波数セット
        lcd_command(i2c, lcd_cmd.lcd_ext_osc_freq, lcd_cmd_param.lcd_ext_osc_freq_typical)
        #コントラスト下位
        lcd_command(i2c, lcd_cmd.lcd_ext_contrast, lcd_cmd_param.lcd_ext_contrast_typical)
        #コントラスト上位 
        lcd_command(i2c, lcd_cmd.lcd_ext_pwiccn, lcd_cmd_param.lcd_ext_pwiccn_boost + lcd_cmd_param.lcd_ext_pwiccn_contrast_3V)
        #増幅率
        lcd_command(i2c, lcd_cmd.lcd_ext_follower, lcd_cmd_param.lcd_ext_follower_on + lcd_cmd_param.lcd_ext_follower_pow_typical)
        #基本コマンド切り替え
        lcd_command(i2c, lcd_cmd.lcd_function_set, lcd_cmd_param.lcd_function_set_data_width + lcd_cmd_param.lcd_function_set_lines)
        #ディスプレイオン
        lcd_command(i2c, lcd_cmd.lcd_display, lcd_cmd_param.lcd_display_on)
        #クリア
        lcd_command(i2c, lcd_cmd.lcd_clear,lcd_cmd_param.lcd_noparam)
 
  
# メインループ

prevline2 = ""

init ()
while 1:

        dt = datetime.now()

        line1 = dt.strftime('%y/%m/%d')
        line2 = dt.strftime('%H:%M:%S')
        if line2 != prevline2:
                #一行目
                lcd_command(i2c, lcd_cmd.lcd_set_ddram_address, lcd_cmd_param.lcd_set_ddram_address_line1)
                lcd_writeMessage(i2c, line1)
                #二行目
                lcd_command(i2c, lcd_cmd.lcd_set_ddram_address, lcd_cmd_param.lcd_set_ddram_address_line2)
                lcd_writeMessage(i2c, line2)
        prevline2 = line2
        time.sleep(0.25)
