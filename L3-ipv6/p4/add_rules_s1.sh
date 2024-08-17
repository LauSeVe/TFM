#!/bin/bash

simple_switch_CLI << EOF
table_add ipv6_dst_exact forward_ipv6 2001:db8:b57:6601::bef6:4118 => 22:33:44:55:66:11 22:33:44:55:66:01 1
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6602::/64 =>  22:33:44:55:66:12 22:33:44:55:66:22 2
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6603::/64 => 22:33:44:55:66:13 22:33:44:55:66:33 3
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6604::/64 => 22:33:44:55:66:14 22:33:44:55:66:44 4
EOF
