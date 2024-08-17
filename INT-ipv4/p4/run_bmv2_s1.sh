#!/bin/bash

p4c --target bmv2 --arch v1model --std p4-16 ~/program.p4 -o ~

sudo simple_switch -i 1@enp7s0 -i 2@enp9s0 -i 3@enp8s0 -i 4@enp10s0 ~/program.json --log-console