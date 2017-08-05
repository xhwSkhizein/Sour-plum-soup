#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# deploy.py - a simple deploy script
# create by hongv @ 2017-08-05

"""
#### 1. shell environment check
* should working in a project dir
* support python2.7 (maybe later upgrade to python3)
* server authority verification

#### 2. project build info config
* (maybe later) detect project form
* build
* (maybe later) deploy service info config (like server role)
* server ip list should config(maybe later) or as a command args

#### 3. restart and rollback
* server health check(like free disk space, memory usage?...etc)
* backup server old version, use soft link to control version, change the soft link when need rollback
* if need restart service,
 - close server traffic gracefully
 - gracefully shutdown current
 - check new service health, (maybe later) regist hook for different service
 - open server traffic gracefully

    90oA*(((((9)))))

"""

import sys


if len(sys.args) < 2:
    print("Usage: deploy.py 10.0.1.1 10.0.1.2 [ip-list] [restart]")
    sys.exit("current version need server ip list as args")
