#!/bin/bash

simple_switch_CLI << EOF
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6601::/64 => 22:33:44:55:66:41 22:33:44:55:66:14 1
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6602::/64 => 22:33:44:55:66:42 22:33:44:55:66:24 2
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6603::/64 => 22:33:44:55:66:43 22:33:44:55:66:34 3
table_add ipv6_dst_exact forward_ipv6 2001:db8:b57:6604::bef6:4118 => 22:33:44:55:66:44 22:33:44:55:66:04 4
EOF
