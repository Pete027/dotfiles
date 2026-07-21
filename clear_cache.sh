#!/usr/bin/env bash

# Очищення кешу pacman та AUR-помічників
# -Scc видаляє всі кешовані пакети, що не встановлені
sudo pacman -Scc --noconfirm
yay -Scc --noconfirm
paru -Scc
rm -rf /var/cache/pacman/pkg/*

# Очищення кешу LibreWolf (тільки папки Cache, а не всього профілю)
find "$HOME/.cache/librewolf" -type d -name "cache2" -exec rm -rf {} + 2>/dev/null

# Очищення кешу Helium (якщо шлях вірний для вашої версії)
if [ -d "$HOME/.cache/net.imput.helium/Default/Cache" ]; then
    rm -rf "$HOME/.cache/net.imput.helium/Default/Cache/*"
fi

echo "✅ System and Browser cache cleared!"
