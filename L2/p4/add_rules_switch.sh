#!/bin/bash

simple_switch_CLI << EOF
table_add ether_src forward 22:33:44:55:66:01 => 22:33:44:55:66:12 22:33:44:55:66:02 2 
table_add ether_src forward 22:33:44:55:66:02 => 22:33:44:55:66:11 22:33:44:55:66:01 1 
EOF


