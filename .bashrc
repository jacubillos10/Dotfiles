# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

unset rc

alias ls='eza --group-directories-first -lhg'
alias cp='cp --verbose'
alias eject='eject --verbose'
alias neofetch='fastfetch'

parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\]<\W>\[\033[33m\]$(parse_git_branch)\[\033[01;31m\]\$ \[\033[37m\]'
. "$HOME/.cargo/env"

export VISUAL=vim
export EDITOR="$VISUAL"
export HSA_OVERRIDE_GFX_VERSION=10.3.0
export C_INCLUDE_PATH="$C_INCLUDE_PATH:/usr/include/python3.12:/home/cubos/.local/lib/python3.12/site-packages/numpy/_core/include"
export THESIS_PATH="/home/cubos/Proyectos/RUSpectroscopy_Tools"
export LEARNING_C_PATH="/home/cubos/Documents/Cubos2.0/C_open_edg/Aprendiendo_C"
export KAGGLE_PATH="/home/cubos/Documents/Cubos2.0/ML/kaggle"
