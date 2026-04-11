from enum import Enum

class lcd_reg_addr(Enum):  # AQM0802 LCDレジスタアドレス
    lcd_command = 0x00
    lcd_data = 0x40


class lcd_cmd(Enum):  # AQM0802 LCDコマンド
    lcd_clear = 0x01  # LCDクリア
    lcd_home = 0x02  # リターンホーム
    lcd_entry_mode = 0x04  # エントリーモード
    lcd_display = 0x08  # ディスプレイ制御 通常 0x08+0x04=0x0C
    lcd_function_set = 0x20  # 通常 0x20+0x10+0x08=0x38 もしくは0x39(拡張インストラクション)
    lcd_set_ddram_address = 0x80  # DDRAM アドレスの指定
    lcd_ext_osc_freq = 0x10  # 下三ビットで周波数指定 通常 0x10+0x04 = 0x14
    lcd_ext_pwiccn = 0x50  # 下二ビットでコントラスト上位二ビット指定 通常 0x50+0x04+0x02 = 0x56
    lcd_ext_follower = 0x60  # 下三ビットで増幅率指定 通常 0x60+0x08+0x04= 0x6c
    lcd_ext_contrast = 0x70  # 下四ビットでコントラスト下位四ビット指定 通常0x70+0x00=0x70


class lcd_cmd_param(Enum):  # AQM0802 LCDコマンドのパラメーター
    lcd_entry_cur_dir = 0x02  # カーソル方向 増加/減数
    lcd_entry_shift = 0x01  # シフトのON/OFF
    lcd_display_on = 0x04  # ディスプレイオン
    lcd_display_cursor = 0x02  # カーソルオン
    lcd_display_cursol_pos = 0x01  # カーソル点滅オン
    lcd_function_set_data_width = 0x10  # 8bit/4bit
    lcd_function_set_lines = 0x08  # 2ライン/1ライン
    lcd_function_set_dh_font = 0x04  # 二倍高フォント使用
    lcd_function_set_ext = 0x01  # 拡張インストラクション
    lcd_set_ddram_address_line1 = 0x00  # 一行目
    lcd_set_ddram_address_line2 = 0x40  # 二行目
    lcd_ext_osc_freq_bias = 0x08  # 1/4bias / 1/5bias
    lcd_ext_osc_freq_normal = 0x04
    lcd_ext_pwiccn_icon = 0x08  # Icon
    lcd_ext_pwiccn_boost = 0x04  # Boost
    lcd_ext_pwiccn_contrast_3V = 0x02  # 3V電源時のコントラスト
    lcd_ext_follower_on = 0x08  # 増幅オン
    lcd_ext_follower_pow_normal = 0x04  # 通常の幅率
    lcd_ext_contrast_normal = 0x00  # 通常の値

lcd_addr=0x3e #AQM0802 LCD I2Cアドレス

usec_sec = 1000000 #一秒のマイクロ秒
# コマンドの実行時間から計算するディレイ(秒(マイクロ秒から換算)) 380kHzの場合の実行時間の二倍程度
cmd_delay = {lcd_cmd.lcd_clear:2000/usec_sec,
             lcd_cmd.lcd_home:2000/usec_sec,
             lcd_cmd.lcd_entry_mode:50/usec_sec,
             lcd_cmd.lcd_display:50/usec_sec,
             lcd_cmd.lcd_function_set:50/usec_sec,
             lcd_cmd.lcd_set_ddram_address:50/usec_sec,
             lcd_cmd.lcd_ext_osc_freq:50/usec_sec,
             lcd_cmd.lcd_ext_pwiccn:50/usec_sec,
             lcd_cmd.lcd_ext_follower:50/usec_sec,
             lcd_cmd.lcd_ext_contrast:50/usec_sec}

#データ出力のディレイ(マイクロ秒)
write_delay = 50/usec_sec