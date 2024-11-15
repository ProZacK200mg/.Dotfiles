import os
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from libqtile.utils import guess_terminal
import colors

from typing import List  # noqa: F401

mod = "mod4"
terminal = guess_terminal()

keys = [
	# Switch between windows in current pane
	Key([mod], "k", lazy.layout.down()),
	Key([mod], "j", lazy.layout.up()),
	Key([mod], "space", lazy.layout.next()),

	# Run a program
	Key([mod], "r", lazy.spawncmd()),
	Key([mod], "Return", lazy.spawn(terminal)),
	Key([mod], "b", lazy.group['5'].toscreen(), lazy.spawn('waterfox')),
	Key([mod], "c", lazy.group['2'].toscreen(), lazy.spawn('code')),

	# Toggle between different layouts as defined below
	Key([mod], "Tab", lazy.next_layout()),
	Key([mod], "w", lazy.window.kill()),

	# Resize windows
	Key([mod, "shift"], "l", lazy.layout.grow()),
	Key([mod, "shift"], "h", lazy.layout.shrink()),
	Key([mod, "shift"], "n", lazy.layout.reset()),
	Key([mod, "shift"], "m", lazy.layout.maximize()),

	# Swap panes of split stack
	Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
	Key([mod, "shift"], "space", lazy.layout.flip()),

	# Move windows up or down in current stack
	Key([mod, "control"], "k", lazy.layout.shuffle_down()),
	Key([mod, "control"], "j", lazy.layout.shuffle_up()),

	# Restart Qtile, Log out, or Turn off computer
	Key([mod, "control"], "r", lazy.restart()),
	Key([mod, "control"], "l", lazy.shutdown()),
	Key([mod, "control"], "q", lazy.spawn('poweroff')),

	# Volume/Brightness Controls
	Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +1%')),
	Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -1%')),
	Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
	Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl -qd intel_backlight set 1%+')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl -qd intel_backlight set 1%-')),]


groups = [
	Group('1',label='1 : term'),
	Group('2',label='2 : code'),
	Group('3',label='3 : gui'),
	Group('4',label='4 : gfx'),
	Group('5',label='5 : web'),
]

for i in groups:
	keys.extend([
		Key([mod], i.name, lazy.group[i.name].toscreen()),
		Key([mod, "shift"], i.name, lazy.window.togroup(i.name,switch_group=True)),
	])

colors = colors.Twilight

layout_theme = {
	"border_width": 2,
	"margin": 10,
	"border_focus": colors[4],
	"border_normal": colors[0],
}

layouts = [
	layout.MonadTall(**layout_theme),
	layout.Floating(**layout_theme),
    layout.Matrix(**layout_theme),
]

widget_defaults = dict(
	font = 'SourceCodeVF',
	fontsize = 16,
	padding = 3,
	foreground = colors[0],
	background = colors[0],
)

extension_defaults = widget_defaults.copy()

screens = [
	Screen(
		top=bar.Bar(
			[

			widget.GroupBox(
				active = colors[1],
				inactive = colors[8],
				rounded = False,
				highlight_method = 'line',
				highlight_color = colors[0],
				this_current_screen_border = colors[4],),

			widget.Prompt(
				prompt = '$ ',
				foreground = colors[2],
				record_history = False,),

#            widget.WindowName(
#				foreground = colors[1]),

			widget.Spacer(
				decorations=[
                	PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.Net(
				format = '{down} \u2193\u2191{up}',
				interface = 'wlan0',
				background = colors[7],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.CurrentLayoutIcon(
				background = colors[5],),

			widget.Spacer(
				length = 1,
				background=colors[5],
				decorations=[
                	PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.CheckUpdates(
				background = colors[3],
				fmt = '↻ {}',
				colour_no_updates = colors[0],
				no_update_string = '0',
				update_interval = 1,
				display_format = '{updates}',
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.TextBox(
				fontsize = 11,
                text = 'Disk',
				background = colors[8],),

			widget.DF(
				visible_on_warn = False,
                partition='/home/prozack200mg/',
                format = '{uf} {m}',
				background = colors[8],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.TextBox(
				fontsize = 11,
                text = 'CPU',
				background = colors[6],),

            widget.CPU(
                format='{load_percent}%',
				background = colors[6],),

			widget.TextBox(
				fontsize = 11,
				text = 'Mem',
				background = colors[6],),

			widget.Memory(
				format = '{MemUsed:.0f}{mm}',
                measure_mem='G',
				update_interval = 1,
				background = colors[6],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.PulseVolume(
                fmt = '♬ {}',
				background = colors[2],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.Backlight(
				backlight_name = 'intel_backlight',
				format = '☀ {percent:.0%}',
				background = colors[4],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.Battery(
				update_delay = 0.1,
            	not_charging_char='',
				format = '{char} {percent:2.0%}',
				background = colors[7],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.Systray(
				icon_size = 20,
				background = colors[8],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),

			widget.Clock(
				format = '%a, %b %d, %Y at %I:%M %p',
				background = colors[6],
				decorations=[
                    PowerLineDecoration(
						path = 'forward_slash',)],),
								# rounded_left
								# arrow_right
								# rounded_right
								# forward_slash
								# zig_zag

			],
			24,
		),
	),
]

# Drag floating layouts.
mouse = [
	Drag([mod], "Button1", lazy.window.set_position_floating(),
		 start=lazy.window.get_position()),
	Drag([mod], "Button3", lazy.window.set_size_floating(),
		 start=lazy.window.get_size()),
	Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
#main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
#	{'wmclass': 'confirm'},
#	{'wmclass': 'dialog'},
#	{'wmclass': 'download'},
#	{'wmclass': 'error'},
#	{'wmclass': 'file_progress'},
#	{'wmclass': 'notification'},
#	{'wmclass': 'splash'},
#	{'wmclass': 'toolbar'},
	Match(wm_class = 'confirmreset'),  # gitk
	Match(wm_class = 'makebranch'),  # gitk
	Match(wm_class = 'maketag'),  # gitk
	Match(title = 'branchdialog'),  # gitk
	Match(title = 'pinentry'),  # GPG key password entry
	Match(wm_class = 'ssh-askpass'),  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize=False
wl_input_rules = None

@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser('~')
	subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
