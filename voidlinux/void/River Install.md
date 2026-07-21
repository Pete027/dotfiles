> xi = doas xbps-install
> doas = sudo

## 1
xi -S dbus wlroots seatd polkit elogind xorg-minimal xorg-fonts xdg-desktop-portal-wlr xorg-server-xwayland
--
doas ln -s /etc/sv/dbus/ var/service
doas ln -s /etc/sv/polkitd/ var/service
doas ln -s /etc/sv/seatd/ var/service
doas vsv
## 2
xi -S mesa-dri pipewire wireplumber brightnessctl Thunar mousepad lightdm lightdm-gtk-greeter plymouth NetworkManager network-manager-applet waylock
--
doas ln -s /etc/sv/lightdm/ var/service
## 2.1
xi -S ghostty fastfetch dpkg 
## 3
xi -S wlr-randr wl-clipboard gvfs xdg-utils noto-fonts-ttf noto-fonts-emoji font-fira-ttf font-fira-otf
## 4 
xi -Suv
xi river yambar fuzzel mako foot 

### River
mkdir -p ~/.config/river
micro ~/.config/river/init
--
#!/bin/env sh
# Keyboard layout
riverctl keyboard-layout us ua

# Terminal (Foot Terminal)
riverctl map normal Super Return spawn foot

# Terminal (Ggostty Terminal)
riverctl map normal Super+Shift Return spawn ghostty

# Close focused window
riverctl map normal Super Q close

# Exit system
riverctl map normal Super+Shift Q close

# App launcher
riverctl map normal Super D spawn fuzzel

# File manager
riverctl map normal Super E spawn thunar

# Start status bar
yambar &

# Background color (dark)
riverctl background-color 0x1e1e2e

--
chmod +x ~/.config/river/init

### Yambar
mkdir ~/.config/yambar
micro ~/.config/yambar/config.yml
--
bar:
  height: 26
  location: top
  background: 1e1e2eff
  foreground: cdd6f4ff

  right:
    - clock:
        content:
          - string: {text: "{date}"}
          - string: {text: "{time}"}

### Mako
mkdir .config/mako/
micro .config/mako/config
--
font=monospace 14
background-color=#282828
border-radius=8
border-size=4
border-color=#a89984
width=400
height=100
padding=20
default-timeout=2500

[urgency=critical]
border-color=#cc241d

[urgency=low]
border-color=#d79921
---
add to .config/river/init
--
exec dbus-daemon --session --address=unix:path=$XDG_RUNTIME_DIR/bus &
exec mako &

### LightDM
doas micro /usr/share/wayland-sessions/river.desktop
--
[Desktop Entry]
Name=River
Comment=Dynamic Wayland compositor
Exec=river
Type=Application

### Runtime DIR
doas touch /etc/profile.d/set_xdg_runtime_dir.sh
doas micro /etc/profile.d/set_xdg_runtime_dir.sh
--
#!/bin/env bash

if [ -z "$XDG_RUNTIME_DIR" ]; then
	export $XDG_RUNTIME_DIR=/run/user/$(id -u)
	mkdir -p "$XDG_RUNTIME_DIR"
	chmod 0700 "$XDG_RUNTIME_DIR"
fi		
--
chmod +x /etc/profile.d/set_xdg_runtime_dir.sh
sh /etc/profile.d/set_xdg_runtime_dir.sh

#river

dbus-run-session river

> man river
> man riverctl
> man rivertile
