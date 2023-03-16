# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # Most of our keybindings are in sxhkd file - except these
    
    
    # SUPER + FUNCTION KEYS

    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod], "q", lazy.window.kill()),


    # SUPER + SHIFT KEYS

    ([mod, "shift"], "q", lazy.window.kill()),
    ([mod, "shift"], "r", lazy.restart()),


    # QTILE LAYOUT KEYS
    ([mod], "n", lazy.layout.normalize()),
    
    # Toggle between different layouts as defined below
    ([mod], "space", lazy.next_layout()),
    ([mod, "shift"], "space", lazy.prev_layout()),

    # CHANGE FOCUS
    ([mod], "Up", lazy.layout.up()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "Left", lazy.layout.left()),
    ([mod], "Right", lazy.layout.right()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    
    
    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),


    # RESIZE UP, DOWN, LEFT, RIGHT
    ([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    ([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    ([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    ([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    ([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    ([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    ([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    ([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    ([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    ([mod, "mod1"], "k", lazy.layout.flip_up()),
    ([mod, "mod1"], "j", lazy.layout.flip_down()),
    ([mod, "mod1"], "l", lazy.layout.flip_right()),
    ([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    ([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    ([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    ([mod, "shift"], "Left", lazy.layout.swap_left()),
    ([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    ([mod, "shift"], "space", lazy.window.toggle_floating()),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),
    
    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
]]
