# XIAO RP2040 MacroButtonJP

### ボタンを押すと一連のキーコードを送出する"マクロボタン"である。
RP2040がCircuitPythonで簡単にキーコードを送出できるので試してみた。日本語キーボード環境での"INTERNATIONALコード"が難しかった。

### 使用機材  
- [Seeed Studio XIAO RP2040](https://wiki.seeedstudio.com/XIAO-RP2040/)
- [Grove Shield for Seeed Studio XIAO](https://wiki.seeedstudio.com/Grove-Shield-for-Seeeduino-XIAO-embedded-battery-management-chip/)
- [M5Stack UNIT Key](https://docs.m5stack.com/en/unit/key)

### 環境  
"M5Stack UNIT Key"を"Grove Shield for Seeed Studio XIAO"のGroveコネクタ"0/1/3V3/GND"に接続する。  
[Seeed Studio XIAO RP2040](https://circuitpython.org/board/seeeduino_xiao_rp2040/)から"CircuitPython"をダウンロードして、コピーする(2022/9/17ではRelease7.3.3)。  
"Seeed Studio XIAO RP2040"をPCに接続すると、"CIRCUITPY"ドライブとして認識される。  
ダウンロードした"CircuitPython"の"lib"フォルダから、必要となる以下のファイルを"CIRCUITPY"ドライブの"lib"フォルダへコピーする。  
- "adafruit_hid"フォルダ
- "neopixel.mpy"ファイル

"lib/keycode_jp.py"ファイルを"CIRCUITPY"ドライブの"lib"フォルダへコピーする。  
"code.py"ファイルを"CIRCUITPY"ドライブの"ルート"フォルダへコピーする。  
