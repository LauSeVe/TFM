#!/bin/bash

simple_switch_CLI << EOF
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6601::/64 => 22:33:44:55:66:31 22:33:44:55:66:13 1
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6602::/64  => 22:33:44:55:66:32 22:33:44:55:66:23 2
table_add ipv6_dst_exact forward_ipv6 2001:db8:b57:6603::bef6:4118 => 22:33:44:55:66:33 22:33:44:55:66:03 3
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6604::/64  => 22:33:44:55:66:34 22:33:44:55:66:43 4
EOF
