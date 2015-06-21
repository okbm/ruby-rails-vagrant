# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.decorators import task
from fabric.contrib import files
from fabric.colors import red, green
from cuisine import run
import cuisine

env.hosts = ['vagrant@192.168.56.101']
#env.port = 2222
env.user = 'vagrant'
env.password = 'vagrant'
env.forward_agent = True

@task
def update_packages():
    puts(green('update packages'))
    sudo("apt-get update")

# 使いそうなツール
@task
def setup_devtools():
    puts(green('Installing Devtools'))
    packages = '''
        vim curl wget build-essential tmux screen zsh make sqlite3 tig tree locate git-core python-software-properties
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

# アプリケーション
@task
def setup_packages():
    puts(green('Installing Packages'))

    sudo ("rm -rf /var/www")
    sudo ("ln -fs $HOME /var/www")

    # rbenv
    run('git clone https://github.com/sstephenson/rbenv.git ~/.rbenv');
    run('git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build');
    run('echo \'export PATH="$HOME/.rbenv/bin:$PATH"\' >> ~/.bash_profile');
    run('echo \'eval "$(rbenv init -)"\' >> ~/.bash_profile');
    run('source ~/.bash_profile');

    # ruby
    run('rbenv install 2.1.0');
    run('rbenv global 2.1.0');

    # rails
    run('echo \'install: --no-rdoc --no-ri\' >> ~/.gemrc');
    run('echo \'update : --no-rdoc --no-ri\' >> ~/.gemrc');

    run('gem install rubygems-update')
    run('update_rubygems')

    run('gem install rails --version 4.2.0')

    # other
    cuisine.package_ensure('mysql-server-5.5')
    cuisine.package_ensure('redis-server')

    # nvm
    run("git clone https://github.com/creationix/nvm.git ~/.nvm")

@task
def setup_original():
    puts(green('setup original'))

    # ssh
    run('echo "Host github.com" > $HOME/.ssh/config');
    run('echo "     HostName github.com" >> $HOME/.ssh/config');
    run('echo "     User git" >> $HOME/.ssh/config');
    run('echo "     StrictHostKeyChecking no" >> $HOME/.ssh/config');
    run('chmod 600 $HOME/.ssh/config');

    # dotfiles
    run('git clone git@github.com:okbm/dotfiles.git');
    run('WORK=$HOME/');

@task
def main():
    update_packages()
    setup_devtools()
    setup_packages()
    setup_original()

    puts(green('finish script'))
