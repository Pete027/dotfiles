sudo xbps-install -Su
sudo xbps-install void-repo-nonfree void-repo-multilib void-repo-multilib-nonfree
sudo xbps-install -Su fish-shell mc tmux micro htop git wget curl
sudo xbps-install base-devel
---
chsh -l 
chsh -s /bin/fish or chsh -s /usr/bin/fish
---
micro .config/fish/config.fish
--
alias xi='doas xpbs-install'
---
sudo xbps-install vsv dbus
sudo ln -s /etc/sv/dbus /var/service
sudo  vsv
____

## Install & set doas
sudo micro /etc/xbps.d/10-ignore.conf
---
ignorepkg=sudo
---
sudo xbps-install opendoas
sudo micro /etc/doas.conf
---
permit persist root as root
permit persist pt as root
---
doas xbps-remove sudo
or
doas xbps-remove -F sudo
---
doas ln -s /usr/bin/doas /usr/bin/sudo
or 
su - 
ln -s /usr/bin/doas /usr/bin/sudo
exit
#void

xdg-desktop-portal-wlr