alias h='history'
alias cd..='cd ..'
alias lsl='ls -lh'
PATH=$PATH:~/bin
export PATH

PS1='\u@\h:\w $ '

#Useful Aliases:
alias e='einstein'
alias vi='nvim'

#Branch shower
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "

#Neovim
exportBin()
{
  [ ! -d "$HOME/bin" ] && mkdir -p "$HOME/bin"
  for dir in $(find $HOME/bin -type d -name bin)
  do
    export PATH="${PATH}${PATH+:}${dir}"
  done
}
exportBin

#Commands for fzf
fuzzy_find_file()
{
  echo "$(find ${1:-.} -type f -print | fzf)"
}

fuzzy_find_directory()
{
  echo "$(find ${1:-.} -type d -print | fzf)"
}

fcd()
{
  cd `fuzzy_find_directory $@`
}

fvi()
{
  nvim `fuzzy_find_file $@`
}

# fuzzy path
fpath()
{
  echo "$(fuzzy_find_directory $@)"
}
