#!/bin/bash

simple_switch_CLI << EOF
table_add ipv4_dst forward_ipv4 135.41.1.0/24 => 22:33:44:55:66:41 22:33:44:55:66:14 1
table_add ipv4_dst forward_ipv4 135.41.2.0/24 => 22:33:44:55:66:42 22:33:44:55:66:24 2
table_add ipv4_dst forward_ipv4 135.41.3.0/24 => 22:33:44:55:66:43 22:33:44:55:66:34 3
table_add ipv4_dst forward_ipv4 135.41.4.1/32 => 22:33:44:55:66:44 22:33:44:55:66:04 4
table_add swtrace add_swtrace => 4
set_queue_rate 50
set_queue_depth 100
EOF


