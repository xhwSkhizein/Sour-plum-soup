# Sour-plum-soup

a simple deploy script write in python.

## Features Support

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

#### [Plz Tell me what else Any Requirements, advice, tips..  ](https://github.com/xhwSkhizein/Sour-plum-soup/issues/new)





----

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With my naught cat coding is difficult!!!

 oh~ maybe she just want to leave some message to you guys: ol []'=v b'
