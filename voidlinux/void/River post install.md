//Clear cache VoidLinux
doas xbps-remove -O
--
Check cache size
doas du -sh /var/cache/xbps
--
Clean manually
doas rm -rf /var/cache/xbps/*
---
//Install last linux kernel
xi -Su linux-mainline linux-mainline-headers linux-firmware
doas reboot
---
//Choise locale, add change language
micro /etc/default/libc-locale
--
un_US.UTF-8 UTF-8
uk_UA.UTF-8 UTF-8
--
doas xbps-reconfigure -f glibc-locales
---
micro ~/.config/fish/config.fish
--
if status is-login
    set -gx XKB_DEFAULT_LAYOUT "us,ua"
    set -gx XKB_DEFAULT_OPTIONS "grp:alt_shift_toggle"
end
--
doas reboot
---
//Screenshots
xi -S grim flameshot swaybg
---
mkdir .config/flameshot/
micro .config/flameshot/flameshot.ini
--
UseGrimAdapter=true

//Fuzzel
mkdir .config/fuzzel/
micro .config/fuzzel/fuzzel.ini
--
dpi-aware=no
font=FiraMono-rerular:size=14
icon-theme=Papirus-Dark
prompt="❯  "
width=45
fields=name,generic,comment,categories,filename,keywords
terminal=foot -e
show-actions=yes
exit-on-keyboard-focus-loss=no

[colors]
background=08052bdd
text=e3e3eaff
prompt=ff7f7fff
# placeholder=ffd966ff
input=ff7f7fff
match=FFE57Fff
selection-match=ffe57fff
selection=44475add
selection-text=ffffffff
# counter=93a1a1ff
border=7f3fbf55
---
//Void-packages
doas xpbs-install xtools
git clone https://github.com/void-linux/void-packages.git
cd void-packages
./xbps-src binary-bootstrap
--
cd void-packages
copy package repository (git clone) to /srcpkgs (void-packages/srcpkgs)
./xbps-src pkg <package_name>
xi <package_name> 
 -- but packages not found 
doas xi <package_name> (this xi in packages xtools)
---
//Custom XBPS binary repository created by Jake@Linux.
https://codeberg.org/JakeAtLinux/void-repo/src/branch/main
https://forum.jpedmedia.com/

helium-browser
librewolf-bin
gofer
---
//River update to 4.5
llvm >=21.x (but maybe no need, if edit 'zig/temples' file )
--
zig 16.x
cd /void-packages
micro srcpkgs/zig/template (edit version, llvm, checkum)
XBPS_MAKEJOBS=2 ./xbps-src pkg zig  (if bild error then XBPS_MAKEJOBS=1)
--
river 4.5
---
//River update to 3.0.12 in manual
/zig 15.x
https://ziglang.org/download/0.15.2/zig-x86_64-linux-0.15.2.tar.xz
cd ~/Downloads
tar -xf zig-x86_64-linux-0.15.2.tar.xz -C ~/.local/share/
mkdir -p ~/.local/bin
ln -s ~/.local/share/zig-x86_64-linux-0.15.2/zig ~/.local/bin/zig
fish_add_path ~/.local/bin
zig version
which zig
--
/river 3.0.12
https://codeberg.org/river/river/releases/download/v0.3.12/river-0.3.12.tar.gz
cd ~/Downloads
tar -xf river-0.3.12.tar.gz
cd river-0.3.12
xi -S wlroots0.19 wlroots0.19-devel
zig build -Doptimize=ReleaseFast --prefix ~/.local
---
//lightdm custom
xi -S lightdm-gtk-greeter-settings
micro /etc/lightdm/lightdm-gtk-greeter-settings.conf (edit file in manual)
--
[greeter]
background=/usr/share/backgrounds/pictures.jpg
theme-name=WhiteSur-Dark
icon-theme-name=WhiteSur-dark
indicators=~host;~spacer;~clock;~session;~power
clock-format=%H:%M:%S
---
#river #void

