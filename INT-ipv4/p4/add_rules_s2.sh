#!/bin/bash

simple_switch_CLI << EOF
table_add ipv4_dst forward_ipv4 135.41.1.0/24 => 22:33:44:55:66:21 22:33:44:55:66:12 1
table_add ipv4_dst forward_ipv4 135.41.2.1/32 => 22:33:44:55:66:22 22:33:44:55:66:02 2
table_add ipv4_dst forward_ipv4 135.41.3.0/24 => 22:33:44:55:66:23 22:33:44:55:66:32 3
table_add ipv4_dst forward_ipv4 135.41.4.0/24 => 22:33:44:55:66:24 22:33:44:55:66:42 4
table_add swtrace add_swtrace => 2
set_queue_rate 50
set_queue_depth 100
EOF


