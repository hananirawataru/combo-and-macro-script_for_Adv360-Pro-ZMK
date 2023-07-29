Kinesis Advantage360を使って同時打鍵するためのスクリプトです。

writer_combos_macros_file.pyを実行して得られる以下の2ファイルをconfig/に追加します。

*combos.keymap
*macros.dtsi

（この同時打鍵の組み合わせは、親指シフトの実装になります）


加えて以下の設定をすることで、同時打鍵で入力ができます。

1. config/adv360.keymapを以下の様に変更

変更前
    / {
        behaviors {
          #include "macros.dtsi"

変更後
    / {
        #include "combos.keymap"

        behaviors {
          #include "macros.dtsi"


2. boards/arm/adv360/adv360_left_defconfigに以下の一行を追加

CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=50


4. boards/arm/adv360/adv360_right_defconfigに以下の一行を追加

CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=50
