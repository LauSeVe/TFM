#!/bin/bash

simple_switch_CLI << EOF
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6601::/64 => 22:33:44:55:66:21 22:33:44:55:66:12 1
table_add ipv6_dst_exact forward_ipv6 2001:db8:b57:6602::bef6:4118 => 22:33:44:55:66:22 22:33:44:55:66:02 2
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6603::/64 => 22:33:44:55:66:23 22:33:44:55:66:32 3
table_add ipv6_dst_lpm forward_ipv6 2001:db8:b57:6604::/64 => 22:33:44:55:66:24 22:33:44:55:66:42 4
EOF
