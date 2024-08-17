#!/bin/bash

simple_switch_CLI << EOF
table_add ipv4_dst forward_ipv4 135.41.1.1/32 => 22:33:44:55:66:11 22:33:44:55:66:01 1
table_add ipv4_dst forward_ipv4 135.41.2.0/24 =>  22:33:44:55:66:12 22:33:44:55:66:21 2
table_add ipv4_dst forward_ipv4 135.41.3.0/24 => 22:33:44:55:66:13 22:33:44:55:66:31 3
table_add ipv4_dst forward_ipv4 135.41.4.0/24 => 22:33:44:55:66:14 22:33:44:55:66:41 4
EOF


