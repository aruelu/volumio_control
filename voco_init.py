#volumioをbluetoothリモコンで操作するための設定ファイル
#
#DEVICE  デバイスを指定する（不要な物は記載しない）
#
#CTL　押されたボタンとコマンドの関連付け（必ず複数設定する）
#[コマンド名,Type,Code,X移動量,Y移動量,H移動量,value]
#
#コマンド名：prev volup play voldw next shutdown voltog
#Type：evdev.ecodes.EV_KEY evdev.ecodes.EV_REL etc
#Code：evdev.ecodes.BTN_LEFT evdev.ecodes.BTN_RIGHT etc
#
#X移動量、Y移動量、H移動量：各ボタンの判別のための移動量（イベント発生直前の状態）
#　　　　　　　　　　　　　　指定なしの場合、""
#                           BLE-M3の場合、直前のXY移動量によりボタンの判別が可能
#
#value： ボタンの場合1:down 0:up マウスイベントの場合の移動量
#
#定数は、include/uapi/linux/input-event-codes.hを参照

import evdev

# デバイスの指定
DEVICE = "/dev/input/event2"
#DEVICE = ('/dev/input/event3', '/dev/input/event2','/dev/input/event6')

#ボタンとコマンドの関連付け
CTL = (["prev",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,40,280,"",1],
        ["volup",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,60,200,"",1],
        ["play",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,160,-381,"",1],
        ["voldw",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,60,-316,"",1],
        ["next",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,-82,280,"",1],
        ["shutdown",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,10,-31,"",1],
        ["voltog",evdev.ecodes.EV_KEY,evdev.ecodes.KEY_M,"","","",1],
        ["play",evdev.ecodes.EV_KEY,evdev.ecodes.KEY_SPACE,"","","",1],
        ["play",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_LEFT,"","","",1],
        ["volup",evdev.ecodes.EV_KEY,evdev.ecodes.KEY_UP,"","","",1],
        ["voldw",evdev.ecodes.EV_KEY,evdev.ecodes.KEY_DOWN,"","","",1],
        ["next",evdev.ecodes.EV_KEY,evdev.ecodes.KEY_RIGHT,"","","",1],
        ["next",evdev.ecodes.EV_KEY,evdev.ecodes.BTN_RIGHT,"","","",1],
        ["prev",evdev.ecodes.EV_KEY,evdev.ecodes.KEY_LEFT,"","","",1],
        ["volup",evdev.ecodes.EV_REL,evdev.ecodes.REL_WHEEL,"","","",1],
        ["voldw",evdev.ecodes.EV_REL,evdev.ecodes.REL_WHEEL,"","","",-1])