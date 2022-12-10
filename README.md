# TOC

- [TOC](#toc)
- [ReunionLog](#reunionlog)
  - [About repository](#about-repository)
    - [Purpose](#purpose)
    - [About me](#about-me)
    - [The guild](#the-guild)
  - [About WarcraftLogs and  OAuth 2](#about-warcraftlogs-and--oauth-2)
    - [WarcraftLogs](#warcraftlogs)
    - [OAuth](#oauth)
- [Requirements](#requirements)
- [Build or install](#build-or-install)
  - [Build](#build)
  - [Install Package](#install-package)
- [How-To](#how-to)
- [Disclaimer](#disclaimer)


# ReunionLog

## About repository

### Purpose

The main purpose of this small code sample is to access the data of **WarcraftLogs** by their own API. This is being done
through a python package which used ```PyPi``` as distributor. 

Then our purpose is downloading the date to output specific values in a ```.csv``` file extension.

> This is our purpose. The purpose of this package is not to create a ```.csv``` file but to give functionality to gain all the data of the **WarcraftLog**.

### About me

This is a repository maintained by me *Nickgismokato* on the request of the guild who want to use this data gained from WarcraftLogs.

### The guild

The guild in world of warcraft is the guild **Reunion**. This guild is not unaware of the code i create and maintain. Though most of the members is unaware, the officers of the guild know of this.

## About WarcraftLogs and  OAuth 2

### WarcraftLogs

[WarcraftLogs](https://www.warcraftlogs.com) is a website where guilds and individuals can put up there logs from raids, dungeons, etc. from the popular game [World Of Warcraft](https://worldofwarcraft.com).

> This repository will not contain the function to upload logs. How to to it can be found [here](https://www.warcraftlogs.com/help/start).

### OAuth

**WarcraftLogs** uses **OAuth 2.0** for API authentication. 

More can be read at [WarcraftLogs APIv2](https://www.warcraftlogs.com/api/docs).

# Requirements
These are the following python packages needed to use the python script. *Be aware of changes*

| Package | Link | Version | Pip Command |
| :--- | :----: | :---: | :--- |
| requests | [Link](https://pypi.org/project/requests/) | $\geq$ 2.27 | ```$ pip install requests```|
| gql-query-builder | [Link](https://pypi.org/project/gql-query-builder/) | 0.1.7 | ```$ pip install gql-query-builder ``` |
|  | | |

***More to come!***

# Build or install
## Build
There is no reason to build this repository. You can just clone the repository by the following command:
```bash
$ git clone https://github.com/nickgismokato/ReunionLog.git
```
More can be found at [Github docs](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)


## Install Package
To install the Python package, it requires ```pip``` to install.

The command for installing the package is:
```bash
$ pip install ReunionLog
```

# How-To
See [Wiki](https://github.com/nickgismokato/ReunionLog/wiki)

# Disclaimer
The functionality of the functions of this package is bound to change. This is because the **WarcraftLogs API** is in a BETA state as of writing this.

> This package will only be maintained as long as the guild need it. An update of this github will be given when this package no longer is maintained.

