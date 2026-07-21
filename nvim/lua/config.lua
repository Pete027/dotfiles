--//Options
vim.loader.enable()
vim.opt.encoding = "UTF-8"
vim.g.have_nerd_font = true
vim.opt.mouse = "a"
vim.opt.confirm = true
--vim.cmd([[set mouse=]])
vim.opt.winborder = "rounded"
vim.opt.clipboard = "unnamedplus"
vim.opt.inccommand = "split"                       -- Preview substitutions
vim.opt.swapfile = false
vim.opt.undofile = true
vim.opt.undodir = vim.fn.expand("~/.vim/undodir")
vim.opt.completeopt = 'menu,menuone,fuzzy,noinsert'
--Line number
vim.opt.number = true                              -- Line numbers
vim.opt.relativenumber = true
vim.opt.cursorline = true
vim.opt.wrap = false                               -- Don't wrap lines
--Set tabs & indentation
vim.opt.tabstop = 2                                -- Tab width
vim.opt.shiftwidth = 2                             -- Indent width
vim.opt.softtabstop = 2                            -- Soft tab stop
vim.opt.smarttab = true                            -- Smart auto-tab
vim.opt.smartindent = true                         -- Smart auto-indenting
-- Search settings
vim.opt.ignorecase = true                          -- Case insensitive search
vim.opt.smartcase = true                           -- Case sensitive if uppercase in search
vim.opt.hlsearch = false                           -- Don't highlight search results 
vim.opt.incsearch = true                           -- Show matches as you type
-- Visual settings
vim.opt.termguicolors = true                       -- Enable 24-bit colors
vim.opt.signcolumn = "yes"                         -- Always show sign column
vim.opt.cmdheight = 0                     
vim.opt.colorcolumn = "100"
-- New 
vim.opt.splitbelow = true
vim.opt.splitright = true
vim.opt.laststatus = 3
vim.opt.isfname:append("@-@")
--//Plugins options
vim.pack.add({
    { src = "https://github.com/catppuccin/nvim" },
    { src = "https://github.com/sphamba/smear-cursor.nvim" },
    { src = "https://github.com/neovim/nvim-lspconfig" },
    { src = "https://github.com/nvim-treesitter/nvim-treesitter"},
    { src = "https://github.com/mason-org/mason.nvim" },
    { src = "https://github.com/nvim-lualine/lualine.nvim" },
    { src = "https://github.com/nvim-tree/nvim-tree.lua" },
    { src = "https://github.com/nvim-tree/nvim-web-devicons" },
    { src = "https://github.com/nvim-telescope/telescope.nvim" },
    { src = "https://github.com/nvim-telescope/telescope-ui-select.nvim" },
    { src = "https://github.com/nvim-lua/plenary.nvim" },
})
--//Theme
require("catppuccin").setup({transparent_background = true})
vim.cmd.colorscheme("catppuccin-macchiato")
--//UI2
require("vim._core.ui2").enable({
    enable = true,
    targets = "cmd",
    winborder = "rounded",
})
--//Plugins options
require("smear_cursor").toggle()
require("lualine").setup()
require("lspconfig")
require("mason").setup({
    firewall = {
    enabled = true,
    auto_managed = true
  }
})
require("nvim-tree").setup()
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1
require("telescope").setup({
    defaults = {
        preview = { treesitter = true },
        color_devicons = true,
        sorting_strategy = "ascending",
        borderchars = {
            "", -- top
            "", -- right
            "", -- bottom
            "", -- left
            "", -- top-left
            "", -- top-right
            "", -- bottom-right
            "", -- bottom-left
        },
        path_displays = { "smart" },
        layout_config = {
            height = 100,
            width = 400,
            prompt_position = "top",
            preview_cutoff = 40,
        }
    }
})
require("telescope").load_extension("ui-select")
--Auticommands
vim.api.nvim_create_autocmd('FileType', {
    callback = function() pcall(vim.treesitter.start) end,
})

vim.api.nvim_create_autocmd('TextYankPost', {
    callback = function() vim.highlight.on_yank() end,
})

