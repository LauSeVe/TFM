#!/bin/bash

simple_switch_CLI << EOF
table_add ipv4_dst forward_ipv4 135.41.1.0/24 => 22:33:44:55:66:31 22:33:44:55:66:13 1
table_add ipv4_dst forward_ipv4 135.41.2.0/24 => 22:33:44:55:66:32 22:33:44:55:66:23 2
table_add ipv4_dst forward_ipv4 135.41.3.1/32 => 22:33:44:55:66:33 22:33:44:55:66:03 3
table_add ipv4_dst forward_ipv4 135.41.4.0/24 => 22:33:44:55:66:34 22:33:44:55:66:43 4
EOF


