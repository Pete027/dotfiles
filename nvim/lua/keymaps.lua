vim.g.mapleader = " "
vim.g.maplocalleader = " "
local map = vim.keymap.set
map("i", "<C-c>", "<Esc>")
--vim.keymap.set('n', '<leader>e', ':Explore<CR>')
map("n", "<leader>ps", '<cmd>lua vim.pack.update()<CR>')
map('n', '<leader>o', ':update<CR>:source<CR>')
--vim.keymap.set("n", "<space><space>x", "<cmd>source %<CR>")
map("n", "<leader>xx", "<cmd>source %<CR>")
map("n", "<leader>x", ":.lua<CR>")
map("v", "<leader>x", ":lua<CR>")
--Tree
map('n', '<leader>e', ':NvimTreeToggle<CR>')
-- Telescope
local builtin = require("telescope.builtin")
map("n", "<leader>ff", builtin.find_files, {})
map("n", "<leader>fg", builtin.live_grep, {})
map("n", "<leader>fb", builtin.buffers, {})
map("n", "<leader>fh", builtin.help_tags, {})
--Tabs
map({ "n", "t" }, "<leader>t", "<Cmd>tabnew<CR>")
map({ "n", "t" }, "<leader>c", "<Cmd>tabclose<CR>")
map({ "n", "t" }, "<leader>n", "<Cmd>tabnext<CR>")

map({ "n" }, "<leader>sk", builtin.keymaps)