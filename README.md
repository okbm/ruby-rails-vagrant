vagrant fabric
====
vagrantをfabricでセットアップしてみる

## Description

| インストール | version |
|:-----------|:------------|
| mysql      |5.5.40|
| redis      |2.2.12|
| ruby       |2.1.0|
| rails      |4.2|

## Requirement

以下をインストール(macのみでしか検証してません！！)

- virualbox
  - [Downloads – Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- vagrant
  - [Download Vagrant - Vagrant](https://www.vagrantup.com/downloads.html)
- fabric
```
$ easy_install pip
$ pip install fabric cuisine
$ pip install paramiko==1.10
```

## Install

```
$ vagrant up
$ fab main
```

