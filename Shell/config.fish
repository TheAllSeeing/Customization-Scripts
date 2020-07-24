#CONFIGURATIONS

#PATH ADDITIONS
set -gx PATH $PATH ~/bin
set -gx PATH $PATH ~/.emacs.d/bin

#FOLDER VARIABLES
set -x APPS /usr/share/applications/
set -x GITHUB ~/Documents/GitHub

#FILE VARIABLES
set -x FISHRC ~/.config/fish/config.fish
set -x BASHRC /home/atai/.bashrc
set -x EMACS_CONFIG ~/.emacs.d/modules/private/atai/init.el

#ALIASES
alias leave="exit"
alias please="sudo"
alias to-pdf="soffice --headless --convert-to pdf"
alias wifi="nmcli radio wifi"
alias resource="source $FISHRC"
