#!/bin/bash

`which mysqldump` -uroot -pmHealth365_sites_1019 chanzhi > chanzhi_backup/chanzhi-`date +"%Y%m%d-%H:%M"`.sql
