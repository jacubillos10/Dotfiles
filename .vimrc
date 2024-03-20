set number
set mouse=a
set numberwidth=1
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
set laststatus=2
set backspace=2
set nocompatible
set noexpandtab
set tabstop=4
set shiftwidth=4

call plug#begin('~/.vim/plugged')
Plug 'tribela/vim-transparent'
Plug 'preservim/nerdtree'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'sonph/onehalf', { 'rtp': 'vim' }
call plug#end()

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'ycm-core/YouCompleteMe'
call vundle#end()

"autocmd VimEnter * NERDTree | vertical resize 15
inoremap <c-b> <Esc>:NERDTreeToggle<cr>:vertical resize 30<cr>
nnoremap <c-b> <Esc>:NERDTreeToggle<cr>:vertical resize 30<cr>

let g:ycm_autoclose_preview_window_after_completion=1

colorscheme molokai_cubos
