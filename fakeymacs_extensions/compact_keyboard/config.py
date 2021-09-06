﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

####################################################################################################
## 60% US キーボードのキー不足（Delete キー、Backquote キー不足）の対策を行う
####################################################################################################

define_key(keymap_global, "C-A-Back", self_insert_command("C-A-Delete"))

if not is_japanese_keyboard:
    define_key(keymap_global, "S-Back", keymap.defineMultiStrokeKeymap("S-Back"))

    for mod1 in ["", "W-"]:
        for mod2 in ["", "A-"]:
            for mod3 in ["", "C-"]:
                for mod4 in ["", "S-"]:
                    mkey  = mod1 + mod2 + mod3 + mod4
                    mkey1 = mkey + "Back"
                    mkey2 = mkey + "BackQuote"
                    define_key(keymap_global, "S-Back " + mkey1, self_insert_command(mkey2))

    # 拡張機能 vscode_key が有効な場合の追加設定
    try:
        # 拡張機能 vscode_key は有効か？
        fc.keymap_vscode

        def is_vscode_target(window):
            if (window.getProcessName() in fc.vscode_target and
                window.getClassName() == "Chrome_WidgetWin_1"):
                return True
            else:
                return False

        def define_key_v(window_keymap, keys, command):
            define_key3(window_keymap, keys, command, lambda: is_vscode_target(keymap.getWindow()))

        define_key_v(keymap_global, "S-Back C-S-Back", getKeyCommand(fc.keymap_vscode, "C-S-BackQuote"))
        define_key_v(keymap_global, "S-Back C-Back",   getKeyCommand(fc.keymap_vscode, "C-BackQuote"))

    except:
        pass
