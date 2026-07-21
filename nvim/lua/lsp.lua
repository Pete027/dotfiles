vim.lsp.enable({
  "bashls",
  "emmet_ls",
  "pyright",
  "lua_ls",
  "clangd",
})

vim.diagnostic.config({ virtual_text = true })


vim.api.nvim_create_autocmd('LspAttach', {
    callback = function(args)
        vim.o.signcolumn = 'yes:1'
        local client = assert(vim.lsp.get_client_by_id(args.data.client_id))
        if client:supports_method('textDocument/completion') then
            vim.o.complete = 'o,.,w,b,u'
            vim.o.completeopt = 'menu,menuone,popup,noinsert'
            vim.lsp.completion.enable(true, client.id, args.buf)
            --vim.keymap.set('i', '<C-Space>', function()
            --vim.lsp.completion.get()
        end--)
    end
--end    
})