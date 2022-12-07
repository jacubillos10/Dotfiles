set number
set mouse=a
set numberwidth=1
set clipboard=unamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
set laststatus=2
set backspace=2

set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'ycm-core/YouCompleteMe'
Plugin 'rafi/awesome-vim-colorschemes'

call vundle#end()
filetype plugin indent on

set ttymouse=sgr
"transparente
"colorscheme abstract
"colorscheme archery
"transparente y por defecto
"colorscheme elflord
"colorscheme meta5
"colorscheme orbital
"transparente
colorscheme purify
"transparente y por defecto *****
"colorscheme delek
"colorscheme desert
"colorscheme evening
"colorscheme industry
"*****
"colorscheme koehler
"colorscheme morning
"colorscheme murphy
"colorscheme peachpuff
"colorscheme ron
"colorscheme shine
"*****
"colorscheme slate
"colorscheme torte
"*****
"colorscheme zellner
set shell=alacritty
