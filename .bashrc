#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='exa --group-directories-first'
alias ll='ls -lhg'
alias la='ls -lhag'
alias grep='grep --color=auto'
#PS1='[\u@\h \W]\$ '
. ~/.git-prompt.sh
GIT_PS1=SHOWDIRTYSTATE=1
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\] '
export PATH="/usr/local/bin:/usr/bin:/usr/sbin:/usr/local/sbin:/home/cubos/.local/bin:/var/lib/snapd/snap/bin:/home/cubos/discord:/opt/cuda/bin"
