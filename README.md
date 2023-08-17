Kinesis Advantage360を使って親指シフト入力するためのファイル類です。

設定例はこちら↓

https://github.com/hananirawataru/Adv360-Pro-ZMK/tree/oyainput-romanmode-qwerty-mac

ファームウエアを直接ダウンロードしたい方はこちら↓

https://github.com/hananirawataru/Adv360-Pro-ZMK/actions/runs/5635442004


---
具体的な設定方法は以下になります。

1. 以下の2ファイルをconfig/以下に追加します。
(writer_combos_macros_file.pyを実行すると得られるファイルです)

```
combos.keymap

macros.dtsi
```


2. config/adv360.keymapを以下の様に変更

変更前
```
/ {
        behaviors {
          #include "macros.dtsi"
```

変更後
```
    / {
        #include "combos.keymap"

        behaviors {
          #include "macros.dtsi"
```


3. boards/arm/adv360/adv360_left_defconfigに以下の一行を追加
```
CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=50
```

4. boards/arm/adv360/adv360_right_defconfigに以下の一行を追加
```
CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=50
