# Path additions
set -gx PATH $PATH ~/.emacs.d/bin

# Configs
thefuck --alias | source

# Variales
set -x FISHRC ~/.config/fish/config.fish
set -x EMACRC ~/.emacs.d/modules/private/atai/init.el
set -x EMACS ~/.emacs.d
set -x GITHUB ~/Documents/GitHub
set -x EXERCISES ~/gdrive/Studies/School/Exercise

# aliases
alias cdapp='cd /usr/share/applications'
alias res='ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0'
alias wonderdraft=/opt/Wonderdraft/Wonderdraft.x86_64
alias please=sudo
alias wifi="nmcli radio wifi"
alias inkscape="flatpak run org.inkscape.Inkscape"
alias studio="/opt/android-studio-preview/bin/studio.sh"
alias resource="source ~/.config/fish/config.fish"
alias open-origin="google-chrome (git config --get remote.origin.url)"
