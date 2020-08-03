#!/bin/fish

#CONFIGURATIONS
set -gx JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
function git --wraps hub --description 'Alias for hub, which wraps git to provide extra functionality with GitHub.'
    hub $argv
end


#DIRECTORY VARIABLES
set -x APPS /usr/share/applications/
set -x GITHUB ~/Documents/GitHub
set -x DRIVE ~/Code-Steel\ \(ORG\)/ACCESS.prj/Drive/
set -x SCHOOL ~/Documents/School
set -x ORG /home/atai/Calendar
set -x BIN ~/Code-Orange\ \(TECH\)/AUTOMATE.prj/
set -x EMACS_HOME ~/.emacs.d/
set -x PHONE /run/user/1000/gvfs/mtp:host=SAMSUNG_SAMSUNG_Android_R58MC0KYREJ/Phone
set -x REPORT ~/LifeManagement/Progress\ Reports
set -x ARCHIVES "Code-Steel (ORG)/ARCHIVES.prj"
set -x ACCESS /home/atai/Code-Steel\ \(ORG\)/ACCESS.prj
set -x REPORT ~/Code-Steel\ \(ORG\)/FORMALIZE.prj/Progress\ Reports
set -x MEDIA ~/Code-Azure\ \(REST\)/Media
set -x FRC $DRIVE/Code-Orange\ \(TECH\)/FRC.prj/EverGreen\ \#7112/
set -x SCREENSHOTS /home/atai/Code-Steel\ \(ORG\)/ACCESS.prj/Pictures/Screenshots


#PATH ADDITIONS
set -gx PATH $PATH $BIN/*
set -gx PATH $PATH $ENACS_HOME/bin
set -gx PATH $PATH ~/.sync
set -gx PATH $PATH $JAVA_HOME/bin
set -gx PATH $PATH ~/.apps/tmsu-x86_64-0.7.5/bin
set -gx PATH $PATH /snap/bin
set -gx PATH $PATH /usr/local/homebrew/bin
set -gx PATH $PATH /home/atai/.local/share/syncthing

#FILE VARIABLES
set -x FISHRC ~/.config/fish/config.fish
set -x BASHRC /home/atai/.bashrc
set -x EMACSRC ~/.emacs.d/init.el
set -x DOOMRC ~/.doom.d/init.el

#ALIASES
alias leave="exit"
alias please="sudo"
alias to-pdf="soffice --headless --convert-to pdf"
alias resource="source $FISHRC"
alias open="xdg-open"
alias del="rmtrash"
alias edit="emacs"
# alias top="htop"
alias dangerous_help="mdless '/home/atai/.local/share/omf/themes/dangerous/README.md'"
alias mv='mv -i'
alias cp='cp -i'


#FUNCTIONS
function exa
	if [ $PWD = "/home/atai" ]
		if test -n "$argv"
			if [ $argv[1] = "-a" ]
				/usr/bin/exa $argv
			else
				/usr/bin/exa -I "snap|wpilib|*.lyx~|*.lyx#" $argv
			end
		else
			/usr/bin/exa -I "snap|wpilib|*.lyx~|*.lyx#" $argv
		end
	else if [ $PWD = "$MEDIA/Books" ]
		if [ -n "$argv" ]
			if [ "$argv" = '-a' ]
				/usr/bin/exa $argv
			else
				/usr/bin/exa -I "metadata*|*.lyx~|*.lyx#" $argv
			end
		else
			/usr/bin/exa -I "metadata*|*.lyx~|*.lyx#" $argv
		end
	else
		if [ -n "$argv" ]
			if [ $argv[1] = "-a" ]
				/usr/bin/exa $argv
			else
				/usr/bin/exa -I "*.lyx~|*.lyx#" $argv
			end
		else
			/usr/bin/exa -I "*.lyx~|*.lyx#" $argv
		end
	end
		
end


function ls
	if [ $PWD = "/home/atai" ] # Specific Directory Filters
		if test -n "$argv"
			if [ $argv[1] = "-a" ] # If argument is not null and applies everythin
				/usr/bin/ls --color=auto -F $argv
			else
				/usr/bin/ls --color=auto -F -I snap -I wpilib -I "*.lyx~" -I "*.lyx#" $argv
			end
		else
			/usr/bin/ls --color=auto -F -I snap -I wpilib -I "*.lyx~" -I "*.lyx#" $argv
		end

	else if [ $PWD = "$MEDIA/Books" ]
		if [ -n "$argv" ]
			if [ "$argv" = '-a' ]
				/usr/bin/ls --color=auto -F $argv
			else
				/usr/bin/ls --color=auto -F -I "metadata*" -I "*.lyx~" -I "*.lyx#" $argv
			end
		else
			/usr/bin/ls --color=auto -F -I "metadata*" -I "*.lyx~" -I "*.lyx#" $argv
		end

	else # General filters
		if test -n "$argv"
			if [ $argv[1] = "-a" ] #If argument is not null and wants to apply everything
				/usr/bin/ls --color=auto -F $argv
			else
				/usr/bin/ls --color=auto -F -I "*.lyx~" -I "*.lyx#" $argv
			end
		else
			/usr/bin/ls --color=auto -F -I "*.lyx~" -I "*.lyx#" $argv
		end
	end
		
end



#THEMES
