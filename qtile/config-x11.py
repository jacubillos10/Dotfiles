# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from datetime import date 
import os

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of creen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod],"m",lazy.spawn("wofi --show drun")),
    Key([mod],"e", lazy.spawn("Thunar")),
    Key([mod,"shift"],"m",lazy.spawn("wofi --show run")),
    Key([],"Print",lazy.spawn("scrot /home/cubos/Pictures/screenshots/screenshot_at_"+str(date.today())+".png")),
    #Key([],"XF86AudioRaiseVolume",lazy.spawn("pactl -- set-sink-volume 0 +10%")),
    #Key([],"XF86AudioLowerVolume",lazy.spawn("pactl -- set-sink-volume 0 -10%")),
    #Key([],"XF86AudioMute",lazy.spawn("pactl -- set-sink-volume 0 0%")),
    #Key([mod,"shift"],"p",lazy.spawn("brightnessctl set +10%")),
    #Key([mod,"shift"],"o",lazy.spawn("brightnessctl set 10%-")),
]

groups = [Group(i) for i in [" ","󰈹 "," " ,"󰙯","󰓓 "," ", "", "󰄻", ""]]
#El ícno que quiero poner como WS1 es  . Para el WS2 ws  . Para el WS3 es  

for i,group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                actual_key,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                actual_key,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
#fin for 

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=5, 
        margin = [5, 5, 5, 5],
        border_focus = '#DDEE40',
        border_on_single = False),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="monospace",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    font='monospace',
                    padding=1,
                ), 
                widget.GroupBox(
                    #background=["#080025","250008"],
                    #foreground=["#00cdcd","#00cdcd"],
                    highlight_method="block",
                    font="Ubuntu Nerd Font",
                    fontsize=20,
                    margin_y=3,
                    #margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    rounded=True,
                    active=['#ffff00','#00ffff'],
                    inactive=['#00ffff','#ff00ff'],
                    highlight_color=['#000000','#160030'],
                    disable_drag=True,
                    this_current_screen_border=['#000000','#9a00ff'],
                    #border_width=1,
                    #other_current_screen_border=["#ff0000","#ff0000"],
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=["#00ffff","#00ffff"],
                    fontsize=12,
                    font="Ubuntu Nerd Font Bold"
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
               # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"), 
                widget.Systray(), #Aquí en systray se ponen los íconos, por ejemplo del wifi
                widget.CurrentLayoutIcon(
                    font="Ubuntu Nerd Font Bold",
                    #fontsize=12,
                ),
                widget.Volume(
                    #emoji = True,
                    fmt = 'Vol:{}',
                    foreground = ['#ffff00','#00ff00'],
                    font = 'Ubuntu Nerd Font Bold',
                ), 
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    foreground=['#00ff00','#00ffff'],
                    font="UbuntuMono Nerd Font",
                    fontsize=13,
                ),
                #widget.QuickExit(),
            ],
            24,
            opacity=0.85,
            background=["#5000b3","#000000"], #Color morado cool: #140028 
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    font='monospace',
                    padding=1,
                ), 
                widget.GroupBox(
                    #background=["#080025","250008"],
                    #foreground=["#00cdcd","#00cdcd"],
                    highlight_method="block",
                    font="Ubuntu Nerd Font",
                    fontsize=20,
                    margin_y=3,
                    #margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    rounded=True,
                    active=['#ffff00','#00ffff'],
                    inactive=['#00ffff','#ff00ff'],
                    highlight_color=['#000000','#160030'],
                    disable_drag=True,
                    this_current_screen_border=['#000000','#9a00ff'],
                    #border_width=1,
                    #other_current_screen_border=["#ff0000","#ff0000"],
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground=["#00ffff","#00ffff"],
                    fontsize=12,
                    font="Ubuntu Nerd Font Bold"
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
               # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"), 
                widget.Systray(), #Aquí en systray se ponen los íconos, por ejemplo del wifi
                widget.CurrentLayoutIcon(
                    font="Ubuntu Nerd Font Bold",
                    #fontsize=12,
                ),
                widget.Volume(
                    #emoji = True,
                    fmt = 'Vol:{}',
                    foreground = ['#ffff00','#00ff00'],
                    font = 'Ubuntu Nerd Font Bold',
                ), 
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    foreground=['#00ff00','#00ffff'],
                    font="UbuntuMono Nerd Font",
                    fontsize=13,
                ),
                #widget.QuickExit(),
            ],
            24,
            opacity=0.85,
            background=["#5000b3","#000000"], #Color morado cool: #140028 
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"

comandos_ejecutar = ["nm-applet &"]

for j in range(len(comandos_ejecutar)):
    os.system(comandos_ejecutar[j])
#fin for
