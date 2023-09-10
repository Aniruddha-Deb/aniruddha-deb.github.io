---
title: Setting up my Mac (again)
publishDate: '2020-10-14T22:48:00'
categories: Programming
tags:
- Programming
slug: mac-system-setup
---

This was also published on [GitHub](https://github.com/Aniruddha-Deb/SystemSetup). 
The GitHub version is more up-to-date, and I won't be updating this one as 
frequently.

# System Setup Log

My MacBook battery started to swell around a year back, and the machine 
became unusable 6 months ago and was put into temporary hibernation. Post my 
exams, I did a battery replacement and the computer was out of the hospital 
today, with a fresh operating system and a formatted disk. The last time I set 
this machine up, I did a halfhearted job of logging the process. This time, I've
done it properly :)

## The Procedure

- User Settings
	- System came with my home directory set as 'aniruddadeb' and User name as 
	  'Anirudda Deb'
	- Create a new admin account, log out of current account and into admin account
	- In admin account, rename home directory to 'Sensei' (or whatever name), 
	  and then in Preferences->Users and Groups, unlock and ctrl-click on your 
	  account for 'advanced settings'
	- In advanced settings, change the name to your name and name of the home 
	  directory to the name of your home directory. Make sure user name is same 
	  as that of home directory.
	- Restart, log back in and delete admin account.
	- Set the computer HostName, LocalHostName and ComputerName to MacBook-Pro:
	  
```bash
sudo scutil --set HostName MacBook-Pro  
sudo scutil --set LocalHostName MacBook-Pro  
sudo scutil --set ComputerName MacBook-Pro  
dscacheutil -flushcache  
<restart>
```

- System Prefs
	- Resolution of 1440x900 (Displays)
	- Uncheck natural scroll direction (Trackpad->Scroll and Zoom)
	- Use F1, F2 as function keys (Keyboard)
	- Don't show input menu in menu bar (Keyboard->Input Sources)
	- Dark Mode  
	![dark side meme](res/darkside.jpeg)
	- Change computer name to MacBook-Pro (Sharing)

- Google Chrome:
	- Download, drag and drop
	- Sign in and sync stuff

- Sublime Text
	- Download, drag and drop

- Content
	- Transfer personal files from HDD
	- Screen background to `hackerfx_img.jpg`

- Things 3
	- Install from Mac App Store
	- Sign in and sync tasks
	
- iTerm 2
	- Download, drag and drop

By now, the system should be looking pretty good. Catalina uses `zsh` rather than 
bash, and clang rather than gcc, so porting some stuff over will be tricky, but 
we'll get to that in a minute.

- Git
	- download mac installer from `git-scm.com`
	- ctrl-click and click 'open' (security won't let you click to open)
	- follow installer guidelines
	? Will xcode command line tools eat this up?

\<DON'T DO THIS!\>

- Python
	- Download latest stable installer from web
	- Double click and install <br>
	! Don't do this because this does not install python properly; you have to 
	  hack around it and do a ton of exports and stuff. I had to uninstall
	  python after this, using instructions from [here](https://stackoverflow.com/questions/3819449/how-to-uninstall-python-2-7-on-a-mac-os-x-10-6-4/3819829#381982)9
	  and [here](https://superuser.com/questions/276840/uninstalling-python-3-on-a-mac). 
	  Best way to install is to use `brew` (this keeps the python updated) and 
	  `pyenv`, so first install `brew`.

\</DON'T DO THIS!\>

- XCode Command Line Tools
	- GCC, `clang`, `make` etc etc
	- Download from developer.apple.com, mount, use .pkg installer
	- It's a 400 MB download and takes 2.54 GB of space on the system.
	* This doesn't eat up git (`git --version` still gives git 2.27, so yay!)

- Homebrew
	- Needed for practically everything :P
	- visit brew.sh and copy-paste the installation command
	- Again, a huge download here (350 MB)

- Python
	- Use `pyenv` to download and install python, as shown in the article https://opensource.com/article/19/5/python-3-default-mac
	- In short, do the following:
```bash
brew install pyenv
pyenv install 3.9.0 # replace with latest python version
pyenv global 3.9.0 # set 3.9.0 as global version
pyenv version # double check version
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc # voodoo magic that allows pyenv to work
exit
```
and now do `python -V` and `pip -V` to verify that python 3.9.0 is loaded

- Vim
	- Copy `.vim` and `.vimrc` from previous system
	- check if clipboard copy/paste is enabled: `vim --version | grep clipboard`, 
	  a + sign appears if clipboard is enabled

- ZSH
	- edit `.zprofile` and add `export CLICOLOR=1` for coloured output from commands
	- add prompt tweaks `PS1='%F{green}%n@%m:%f %F{blue}%~%f %% '`

- iTerm2
	- Tweak profile; first, create a new profile
	- Change background color to `333333`, foreground to `dddddd` and other colors
	  to pastel colours

- Mail
	- Log in to google
	- Configure signatures, calendars, mail folders etc

- Projects
	- This is the meaty part. Start with the blog:
```bash
git clone --select-branch --branch source https://github.com/Aniruddha-Deb/aniruddha-deb.github.io 
mv aniruddha-deb.github.io blog
cd blog
virtualenv venv
source venv/bin/activate
echo "venv" > .gitignore
pip install -r requirements.txt
```

then whip up this article. I ran into a small hiccup while using `make html`: 
the version of Pelican that `pip` installed was 4.5.0, and that broke with the 
old Flex theme. I had made some modifications to the theme (MathJax) and didn't 
want to lose them by upgrading. So, I downgraded pelican to 4.2.0 and then made
the files. Takeaway is use `make html DEBUG=1` for debugger output. Do a `make serve`
to check out formatting, after which do `make github` to push to github pages, which is what
you're reading now (this article has been made from the mac :)

for further updates, refer to the repository linked above.
