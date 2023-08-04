Kinesis Advantage360を使って同時打鍵するためのスクリプトです。

設定例はこちら

https://github.com/hananirawataru/Adv360-Pro-ZMK/tree/oyainput-romanmode-qwerty-mac

---
具体的な設定方法

1. writer_combos_macros_file.pyを実行して得られる以下の2ファイルをconfig/以下に追加します。

（この同時打鍵の組み合わせは、親指シフトの実装になります）

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
