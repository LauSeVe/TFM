#!/usr/bin/env python3
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager
import subprocess

class Downloader():
    def __init__(self):
        self.slice_name = "INT_ipv4"

    def download(self, node_name, file):
        try:     
            fablib = fablib_manager()
            slice = fablib.get_slice(name=self.slice_name)
            node = slice.get_node(name=node_name)
            scp_pre_command = (node.get_ssh_command()).split(" ")
            scp_pre_command[0] = 'scp'
            scp_pre_command[5] = scp_pre_command[5].split("@")
            scp_pre_command[5] = scp_pre_command[5][0] + "@[" + scp_pre_command[5][1] + "]:~/" + file
            scp_pre_command.append("./graphs")
            scp_file = ' '.join(scp_pre_command)
            print(scp_file)
            subprocess.run(scp_file, shell=True, capture_output=True, text=True)

        except Exception as e:
            print(f"Exception: {e}")
