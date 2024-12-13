set number
set relativenumber
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
set showtabline=2
let &t_SI = "\e[6 q"
let &t_EI = "\e[2 q"

call plug#begin('~/.vim/plugged')
Plug 'tribela/vim-transparent'
Plug 'preservim/nerdtree'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'ryanoasis/vim-devicons'
Plug 'chrisbra/csv.vim'
Plug 'vim-airline/vim-airline'
call plug#end()

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'ycm-core/YouCompleteMe'
call vundle#end()

autocmd VimEnter * NERDTree | vertical resize 30
inoremap <c-t> <Esc>:NERDTreeToggle<cr>:vertical resize 30<cr>
nnoremap <c-t> <Esc>:NERDTreeToggle<cr>:vertical resize 30<cr>
nnoremap <m-Right> <Esc>:bnext <cr>
inoremap <m-Right> <Esc>:bnext <cr>
nnoremap <m-Left> <Esc>:bprevious <cr>
inoremap <m-Left> <Esc>:bprevious <cr>
nnoremap <m-S-down> <Esc>:Bclose <cr>
inoremap <m-S-down> <Esc>:Bclose <cr>

let NERDTreeShowHidden=1
let g:ycm_autoclose_preview_window_after_completion=1
let g:airline#extensions#tabline#enabled = 1
colorscheme molokai_cubos

autocmd VimLeave * !echo -ne "\e[6 q"

