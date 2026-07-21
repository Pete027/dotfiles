#pete .config

import os
import platform
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

###User Config
##Autorun
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

##Floating Dialog Windows
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

mod = "mod4"
myTerm = "ghostty"
myEditor ="micro"
myVisual = "subl"
terminal = guess_terminal()

# A function for hide/show all the windows in a group
@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

keys = [
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "space", lazy.layout.next(), desc="Move window focus to other window"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "m", minimize_all(), desc="Toggle hide/show all windows on current group"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    #Key([mod], "Tab", lazy.screen.next_group(), desc="Move to next group."),
    #Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Move to previous group."),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #Launch App's
    Key([mod], "Return", lazy.spawn("ghostty"), desc="Launch terminal"),
    Key([mod, "control"], "Return", lazy.spawn("foot"), desc="Launch terminal2"),
    #Key([mod], "b", lazy.spawn("librewolf --wayland")), #for Wayland
    Key([mod], "b", lazy.spawn("librewolf")), #fox Xorg
    Key([mod], "n", lazy.spawn("nautilus")),
    Key([mod], "v", lazy.spawn("subl")),
    #Key([mod], "b", lazy.spawn("blender")),
    #Key([mod], "l", lazy.spawn("lutris")),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout."),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "1234567890"]

groups = [                                                          
    Group("1", label = "", matches=[Match(wm_class=[""])]),
    Group("2", label = "", matches=[Match(wm_class=[""])]),
    Group("3", label = ""), #matches=[Match(wm_class=["ghostty"])]),
    Group("4", label = "", matches=[Match(wm_class=[""])]),
    Group("5", label = ""),
    Group("6", label = ""),
    Group("7", label = "󰐡"),
    Group("8", label = "󰣙"),
    Group("9", label = ""),
    Group("0", label = ""),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#4FC3F7", "#263238"], border_width=1, margin = 1),
    #layout.Max(),
    #Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    layout.Bsp(border_focus = "#4FC3F7", border_normal = "#263238", border_width=1, margin = 1),
    #layout.Matrix(),
    layout.MonadTall(border_focus = "#4FC3F7", border_normal = "#263238", border_width=1, margin = 1),
    layout.MonadWide(border_focus = "#4FC3F7", border_normal = "#263238", border_width=1, margin = 1),
    #layout.RatioTile(),
    #layout.Tile(),
    layout.TreeTab(border_focus = "#4FC3F7", border_normal = "#263238", border_width=1, margin = 1),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font = "FiraCodeNerdFont",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                #widget.init_widgets_screen(
                #   opacity = 0.7,
                #    size = 20
                #),
                widget.GroupBox(
                    active = "#FBFAFD",
                    inactive = "#78767C",
                    borderwidth = 1,
                    padding = 5,
                    block_highlight_text_color = "4FC3F7",
                    highlight_method = 'line',
                    hide_unused = True,
                    #highlight_color = "#4FC3F7",
                    scroll = True,
                    rounded = False,
                    center_aligned= True,
                    disable_drag= True
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4FC3F7",
                ),
                widget.Prompt(
                    fontsize = 16,
                    cursor = True,
                    padding = 5,
                    prompt = '~ ❱❱',
                    #prompt = '~ ❯❯❯',
                ),
                #widget.TextBox(
                 #text = '|',
                 #font = "FiracodeNerd",
                 #foreground = "#4FC3F7",
                 #padding = 0,
                 #fontsize = 14
                 #),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4FC3F7",
                ),
                widget.LaunchBar(
                    progs = [("", "ghostty", "Ghostty terminal"),
                             ("", "nautilus", "Nautilus file manager"),
                             ("", "librewolf", "Librewolf web browser"),
                    ],
                    fontsize = 18,
                    padding = 5,
                    foreground = "#ffd700",
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4FC3F7",
                ),
                 widget.Sep(
                    linewidth = 1,
                    padding = 5,
                    foreground = "#4FC3F7",
                ),
                widget.WindowName(
                max_chars=30),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ba5264", "#7452ba"),
                    },
                    name_transform = lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.CPU(
                    foreground = "#E9524A",
                    padding = 5,
                    format = '  Cpu: {load_percent}%',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                    ),
                widget.Memory(
                    foreground = "#F1AE1B",
                    padding = 5,
                    format = '{MemUsed: .0f}{mm}', 
                    fmt = '  Mem: {}',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e free')},
                    ),
                widget.DF(
                 update_interval = 60,
                 foreground = "#59C837",
                 padding = 5, 
                 partition = '/',
                 #format = '[{p}] {uf}{m} ({r:.0f}%)',
                 format = '{uf}{m} free',
                 fmt = '  Disk: {}',
                 visible_on_warn = False,
                 ),
                 widget.Battery(
                    foreground = "#FF51D3",
                    #fontsize = 13,
                    battery = 0,
                    update_interval = 60,
                    format = 
                    #'{char} {percent:2.0%} {hour:d}:{min:02d}',
                    '⛽ {percent:2.0%} {char}',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e battop')},
                ),
                #widget.Volume(
                 #foreground = "#1F75CB",
                 #padding = 3,
                 #emoji = True,
                 #check_mute_string = '[off]', 
                 #check_mute_command = None,
                 #device = 'default',
                 #fmt = '   Vol: {}',
                 #),

                #widget.HDD(device='nvme0n1'),
                #widget.Net(format='U {up} D {down}'),
                #widget.CheckUpdates(distro='Arch'),
                #widget.TextBox(text="", padding=0),
                #widget.PulseVolume(padding=5),
                #widget.Spacer(length= 5),
                widget.Sep(
                    linewidth = 1,
                    padding = 3,
                    foreground = "#FFFFFF"
                    ),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'ua'], 
                    update_interval=1
                    ),
                widget.Sep(
                    linewidth = 1,
                    padding = 3,
                    foreground = "#FFFFFF"
                    ),
                #widget.Clock(format="%d-%m-%Y %a %H:%M"),
                widget.Clock(
                 foreground = "#16A085",
                 font = "FiraMonoNerdFont-Bold",
                 padding = 1, 
                 mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('notify-date')},
                 ## Uncomment for date and time 
                 # format = "⧗  %a, %b %d - %H:%M",
                 ## Uncomment for time only
                 #format = "⧗  %I:%M %p",
                 format = "<b> %a %H:%M </b>",
                 ),
                #widget.Spacer(length= 5),
                
                widget.Systray(),
                #widget.StatusNotifier(),
                widget.QuickExit(default_text='✘'),
                widget.Spacer(length = 8),
            ],
            24,
            border_width=[3, 7, 3, 7],  # Draw top and bottom borders
            border_color=["215578", "215578", "215578", "215578"],  # Borders are magenta
            margin= 3,
            background="#212121",
            #opacity="0,5",
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
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
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="imv"),
        Match(wm_class="mpv"),
        Match(wm_class="librewolf"),
        Match(wm_class="stacer"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = False

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "Qtile"
